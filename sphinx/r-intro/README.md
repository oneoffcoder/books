# R, No Tears

This directory contains the Sphinx source for the `R, No Tears` book.

## Requirements

- `uv`
- Python 3.11+

## Setup

Install the project dependencies and create the local virtual environment:

```bash
make sync
```

This uses `uv` and creates a local `.venv` automatically.

## Common Commands

Build the HTML site:

```bash
make build
```

Run the full local verification pass:

```bash
make check
```

Start the live-reloading docs development server:

```bash
make live
```

Build the minimal Docker image used for notebook execution:

```bash
make docker-build
```

Execute all `r-intro` notebooks end-to-end inside Docker:

```bash
make docker-notebooks
```

Run a single notebook while debugging:

```bash
make docker-notebooks NOTEBOOKS=classification.ipynb
```

Executed notebooks are written to:

```text
build/executed-notebooks
```

Run formatting and lint checks:

```bash
make format
make lint
```

Normalize notebook JSON formatting:

```bash
make notebook-format
make notebook-check
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
- `tools/`: local docs maintenance scripts
- `source/`: Sphinx content and configuration
