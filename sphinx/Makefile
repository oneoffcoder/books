PROJECTS = \
	datascience \
	docker \
	excel \
	java-intro \
	makeblock \
	python-dothis \
	python-intro \
	pytorch-intro \
	r-intro \
	scikit-intro \
	scratch \
	spark-intro \
	tello

PYTHON ?= python3
PARALLEL_JOBS ?=
PARALLEL_RUNNER := $(PYTHON) tools/parallel_make.py

.NOTPARALLEL:
.PHONY: clean build

clean:
	@$(PARALLEL_RUNNER) $(if $(PARALLEL_JOBS),--jobs $(PARALLEL_JOBS)) clean $(PROJECTS)

build:
	@$(PARALLEL_RUNNER) $(if $(PARALLEL_JOBS),--jobs $(PARALLEL_JOBS)) build $(PROJECTS)
