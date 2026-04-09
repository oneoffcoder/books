#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from joblib import Parallel, delayed
from tqdm import tqdm


@dataclass
class Result:
    project: str
    target: str
    returncode: int
    log_path: Path
    output: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run per-book make targets in parallel and summarize results."
    )
    parser.add_argument("target", help="Make target to run in each project directory.")
    parser.add_argument("projects", nargs="+", help="Project directories relative to sphinx/.")
    parser.add_argument(
        "--jobs",
        type=int,
        default=None,
        help="Maximum concurrent jobs. Defaults to CPU count and is capped at CPU count.",
    )
    parser.add_argument(
        "--logs-dir",
        default=".parallel-logs",
        help="Directory for captured project logs, relative to sphinx/.",
    )
    parser.add_argument(
        "--tail-lines",
        type=int,
        default=20,
        help="Number of trailing log lines to show for failed projects.",
    )
    return parser.parse_args()


def cpu_bound_jobs(requested: int | None) -> int:
    cores = os.cpu_count() or 1
    if requested is None:
        return cores
    if requested < 1:
        raise ValueError("--jobs must be at least 1")
    return min(requested, cores)


def normalize_projects(projects: Iterable[str], root: Path) -> list[str]:
    normalized = []
    for project in projects:
        project_path = root / project
        if not project_path.is_dir():
            raise FileNotFoundError(f"project directory not found: {project_path}")
        normalized.append(project)
    return normalized


def run_project(root: Path, logs_dir: Path, project: str, target: str) -> Result:
    project_dir = root / project
    log_path = logs_dir / f"{project}-{target}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    command = ["make", "-C", project, target]
    proc = subprocess.run(
        command,
        cwd=root,
        text=True,
        capture_output=True,
    )
    output = proc.stdout + proc.stderr
    log_path.write_text(output)
    return Result(
        project=project,
        target=target,
        returncode=proc.returncode,
        log_path=log_path,
        output=output,
    )


def tail_lines(text: str, n: int) -> str:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return "(no output captured)"
    return "\n".join(lines[-n:])


def summarize(results: list[Result], tail_count: int) -> None:
    succeeded = [r for r in results if r.ok]
    failed = [r for r in results if not r.ok]

    print("\nSummary")
    print(f"  succeeded: {len(succeeded)}")
    print(f"  failed: {len(failed)}")

    if succeeded:
        print("\nSuccessful projects:")
        for result in succeeded:
            print(f"  - {result.project}")

    if failed:
        print("\nFailed projects:")
        for result in failed:
            print(f"  - {result.project} (exit {result.returncode})")
            print(f"    log: {result.log_path}")
            print("    tail:")
            for line in tail_lines(result.output, tail_count).splitlines():
                print(f"      {line}")


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    logs_dir = (root / args.logs_dir / args.target).resolve()
    logs_dir.mkdir(parents=True, exist_ok=True)

    try:
        jobs = cpu_bound_jobs(args.jobs)
        projects = normalize_projects(args.projects, root)
    except (ValueError, FileNotFoundError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(
        f"Running target '{args.target}' for {len(projects)} project(s) "
        f"with up to {jobs} parallel job(s)."
    )

    results: list[Result] = []
    work = (
        delayed(run_project)(root, logs_dir, project, args.target)
        for project in projects
    )
    generator = Parallel(
        n_jobs=jobs,
        prefer="threads",
        return_as="generator_unordered",
    )(work)

    with tqdm(total=len(projects), unit="project") as progress:
        for result in generator:
            results.append(result)
            status = "OK" if result.ok else f"FAIL ({result.returncode})"
            tqdm.write(f"[{status}] {result.project} -> {result.log_path}")
            progress.update(1)

    results.sort(key=lambda item: item.project)
    summarize(results, args.tail_lines)
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
