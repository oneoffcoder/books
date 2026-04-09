UV ?= uv
UV_CMD := env -u VIRTUAL_ENV $(UV)
SPHINXBUILD ?= $(UV_CMD) run sphinx-build
SPHINXAUTOBUILD ?= $(UV_CMD) run sphinx-autobuild
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
	$(UV_CMD) sync

install: sync

format:
	$(UV_CMD) run ruff format $(SOURCEDIR)/conf.py

spellcheck:
	$(UV_CMD) run codespell $(SOURCEDIR)

lint:
	$(UV_CMD) run ruff check $(SOURCEDIR)/conf.py
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
