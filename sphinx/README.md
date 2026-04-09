![One-Off Coder Logo](../logo.png "One-Off Coder")

# Sphinx Books

This directory contains the Sphinx-based books in this repository.

Most books now follow the same pattern:

- a local `Makefile`
- a local `pyproject.toml`
- a local `uv.lock`
- `uv`-managed Python dependencies

Examples include `python-intro`, `python-dothis`, `r-intro`, `datascience`, `scikit-intro`, and the other Sphinx book directories that include a `Makefile`.

# Root Commands

From [`sphinx/Makefile`](/Users/super/git/oneoffcoder/books/sphinx/Makefile):

```bash
make clean
make build
```

These fan out across all Sphinx book projects under `sphinx/` that are wired into the root makefile.

# Per-Book Workflow

Change into a specific book directory first.

```bash
cd sphinx/python-intro
```

Install or update that book's dependencies:

```bash
env -u VIRTUAL_ENV uv sync
```

Build that book:

```bash
make build
```

Clean that book:

```bash
make clean
```

For books that support local autobuild:

```bash
make live
```

# Notes

- Do not use the old `build.sh`, `clean.sh`, `autobuild.sh`, or `make.bat` workflow. The books have been moved to makefile-driven builds.
- Some directories under `sphinx/` are not active Sphinx books yet, such as `csharp` and `keras`. They are not part of the root `make build` / `make clean` flow.
