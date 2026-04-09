# PyTorch, No Tears

This directory contains the Sphinx source for the `PyTorch, No Tears` book.

The book is notebook-heavy and includes a `tensorboard/` directory under `source/` for TensorBoard-related outputs and references.

## Requirements

- `uv`
- Python 3.11+

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
- `source/`: notebook-backed chapters and supporting docs content
- `source/tensorboard/`: TensorBoard-related supporting files
