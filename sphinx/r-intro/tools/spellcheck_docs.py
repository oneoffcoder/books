from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"


def export_docs(target: Path) -> None:
    for path in SOURCE.glob("*.rst"):
        shutil.copy2(path, target / path.name)

    shutil.copy2(SOURCE / "conf.py", target / "conf.py")

    for path in SOURCE.glob("*.ipynb"):
        notebook = json.loads(path.read_text())
        markdown = "\n\n".join(
            "".join(cell.get("source", []))
            for cell in notebook.get("cells", [])
            if cell.get("cell_type") == "markdown"
        )
        (target / f"{path.stem}.md").write_text(markdown)


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp_dir:
        temp_source = Path(tmp_dir) / "source"
        temp_source.mkdir()
        export_docs(temp_source)

        result = subprocess.run(
            ["codespell", str(temp_source)],
            cwd=ROOT,
            check=False,
        )

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
