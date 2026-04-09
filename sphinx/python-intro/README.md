# Python, No Tears

This directory contains the Sphinx source for the `Python, No Tears` book.

This edition is updated for Python 3.13.

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

Start live-reloading docs development server:

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
- `source/`: Sphinx chapters, examples, and supporting assets
- `uv.lock`: locked dependency set for reproducible local installs
