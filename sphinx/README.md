![One-Off Coder Logo](../logo.png "One-Off Coder")

# Intro

A collection of online books for data science, computer science and coding!

# Build

Install dependencies.

```bash
pip install sphinx sphinx_rtd_theme sphinxcontrib-bibtex sphinx-autobuild
```

Then run.

```bash
./build.sh
```

## Autobuild

```bash
python -m sphinx_autobuild java-intro/source java-intro/build -b html -p 8000 -B
python -m sphinx_autobuild python-intro/source python-intro/build -b html -p 8001 -B
python -m sphinx_autobuild pytorch-intro/source pytorch-intro/build -b html -p 8002 -B
python -m sphinx_autobuild scikit-intro/source scikit-intro/build -b html -p 8003 -B
python -m sphinx_autobuild spark-intro/source spark-intro/build -b html -p 8004 -B
```

Then go to [http://localhost:8000](http://localhost:8000).