![One-Off Coder Logo](../logo.png "One-Off Coder")

# Intro

A collection of online books for data science, computer science and coding!

# Build

Install dependencies.

```bash
pip install \
    sphinx \
    sphinx_rtd_theme \
    sphinxcontrib-bibtex \
    sphinx-autobuild \
    sphinxcontrib-blockdiag \
    sphinx-sitemap \
    nbsphinx -U

conda install -c conda-forge pandoc ipython -y
```

To build.

```bash
./build.sh
```

To clean.

```bash
./clean.sh
```

## Autobuild

```bash
./autobuild.sh
```

Then go to 
* [java](http://localhost:8000)
* [python](http://localhost:8001)
* [pytorch](http://localhost:8002)
* [scikit](http://localhost:8003)
* [spark](http://localhost:8004)
* [datascience](http://localhost:8005)
* [python-dothis](http://localhost:8006)
* [scratch](http://localhost:8007)
* [docker](http://localhost:8008)

To kill the `autobuild`.

```bash
./kill-autobuild.sh
```