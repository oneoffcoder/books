# Robotics Programming with Makeblock

This directory contains the Sphinx source for the `Robotics Programming with Makeblock` book.

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
- `source/`: book chapters and static assets used in the rendered pages
- `media/`: supporting media files
- `list-images.py`: helper script for working with image assets
