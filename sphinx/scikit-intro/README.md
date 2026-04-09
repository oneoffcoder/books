# Scikit, No Tears

This directory contains the Sphinx source for the `Scikit, No Tears` book.

The book is primarily notebook-backed and covers classical machine learning workflows, visualization, preprocessing, and ecosystem tooling.

## Requirements

- `uv`
- Python 3.13+
- Docker for full notebook execution, including the `rpy2` chapter

## Setup

Install the project dependencies and create the local virtual environment:

```bash
make sync
```

## Common Commands

Build the HTML site:

```bash
make build
```

Run the full local verification pass:

```bash
make check
```

Execute every public notebook in the Python 3.13 check container:

```bash
make notebook-check
```

Start the live-reloading docs development server:

```bash
make live
```

Run formatting and lint checks:

```bash
make format
make lint
```

Check external links:

```bash
make linkcheck
```

Run Sphinx doctests:

```bash
make doctest
```

Remove build artifacts:

```bash
make clean
```

## Output

The generated HTML site is written to:

```text
build/html
```

## Project Files

- `pyproject.toml`: Python dependencies and tool configuration
- `Makefile`: primary developer entrypoint
- `source/`: notebook-backed chapters and supporting files
- `scripts/modernize_notebooks.py`: notebook API migration helper used for the Python 3.13 refresh
