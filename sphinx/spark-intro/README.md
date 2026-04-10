# Spark, No Tears

This directory contains the Sphinx source for the `Spark, No Tears` book.

The book is primarily notebook-backed and covers Spark fundamentals including RDDs, DataFrames, Spark SQL, streaming, and machine learning.

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

Execute every notebook in the local Spark Docker check image:

```bash
docker build -t book-spark-intro-check:local ../../docker/spark-intro-check
make notebooks
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
- `source/`: notebook-backed chapters and supporting docs files
- `../../docker/spark-intro-check/`: Docker image and runner for end-to-end notebook execution
