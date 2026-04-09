UV ?= uv
SPHINXBUILD ?= $(UV) run sphinx-build
SPHINXAUTOBUILD ?= $(UV) run sphinx-autobuild
SPHINXOPTS ?=
SOURCEDIR := source
BUILDDIR := build
PORT ?= 8000
HOST ?= 0.0.0.0

.DEFAULT_GOAL := help

.PHONY: help sync install format lint spellcheck clean build check html live linkcheck doctest

help:
	@printf "Targets:\n"
	@printf "  sync        Install/update dependencies with uv\n"
	@printf "  install     Alias for sync\n"
	@printf "  format      Format local Python files\n"
	@printf "  lint        Run Python lint and docs spellcheck\n"
	@printf "  spellcheck  Run codespell over the docs tree\n"
	@printf "  build       Alias for html\n"
	@printf "  check       Run lint and html build\n"
	@printf "  html        Build the HTML site\n"
	@printf "  live        Run sphinx-autobuild locally\n"
	@printf "  linkcheck   Check external links\n"
	@printf "  doctest     Run Sphinx doctests\n"
	@printf "  clean       Remove build artifacts\n"

sync:
	$(UV) sync

install: sync

format:
	$(UV) run ruff format $(SOURCEDIR)/conf.py tools/spellcheck_docs.py

spellcheck:
	$(UV) run python tools/spellcheck_docs.py

lint:
	$(UV) run ruff check $(SOURCEDIR)/conf.py tools/spellcheck_docs.py
	$(MAKE) spellcheck

build: html

check: lint html

html:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

live:
	$(SPHINXAUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)/html" -b html --host $(HOST) --port $(PORT)

linkcheck:
	$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck" $(SPHINXOPTS)

doctest:
	$(SPHINXBUILD) -b doctest "$(SOURCEDIR)" "$(BUILDDIR)/doctest" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"
