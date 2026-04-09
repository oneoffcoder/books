from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"


def normalize_lines(value: Any) -> Any:
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return [str(item) for item in value]
    return value


def normalize_output(output: dict[str, Any]) -> dict[str, Any]:
    normalized: dict[str, Any] = {}
    for key in sorted(output):
        value = output[key]
        if key == "data" and isinstance(value, dict):
            normalized[key] = {data_key: value[data_key] for data_key in sorted(value)}
        else:
            normalized[key] = normalize_lines(value)
    return normalized


def normalize_cell(cell: dict[str, Any]) -> dict[str, Any]:
    normalized: dict[str, Any] = {}
    ordered_keys = ["cell_type", "execution_count", "metadata", "outputs", "source"]

    for key in ordered_keys:
        if key not in cell:
            continue
        value = cell[key]
        if key == "outputs":
            normalized[key] = [normalize_output(output) for output in value]
        elif key == "metadata" and isinstance(value, dict):
            normalized[key] = {meta_key: value[meta_key] for meta_key in sorted(value)}
        else:
            normalized[key] = normalize_lines(value)

    for key in sorted(cell):
        if key not in normalized:
            normalized[key] = cell[key]

    return normalized


def normalize_notebook(notebook: dict[str, Any]) -> dict[str, Any]:
    normalized: dict[str, Any] = {
        "cells": [normalize_cell(cell) for cell in notebook.get("cells", [])],
        "metadata": {},
    }

    for key in sorted(notebook.get("metadata", {})):
        value = notebook["metadata"][key]
        if isinstance(value, dict):
            normalized["metadata"][key] = {meta_key: value[meta_key] for meta_key in sorted(value)}
        else:
            normalized["metadata"][key] = value

    for key in ("nbformat", "nbformat_minor"):
        if key in notebook:
            normalized[key] = notebook[key]

    for key in sorted(notebook):
        if key not in normalized:
            normalized[key] = notebook[key]

    return normalized


def dump_notebook(notebook: dict[str, Any]) -> str:
    return json.dumps(notebook, indent=1, ensure_ascii=False) + "\n"


def iter_notebooks() -> list[Path]:
    return sorted(SOURCE.glob("*.ipynb"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if any notebook would change")
    args = parser.parse_args()

    changed: list[Path] = []

    for path in iter_notebooks():
        current = path.read_text()
        normalized = dump_notebook(normalize_notebook(json.loads(current)))

        if current != normalized:
            changed.append(path)
            if not args.check:
                path.write_text(normalized)

    if args.check and changed:
        for path in changed:
            print(path.relative_to(ROOT))
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
