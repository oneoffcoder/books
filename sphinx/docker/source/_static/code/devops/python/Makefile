.PHONY: init clean lint test
.DEFAULT_GOAL := build

init:
	pip install -r requirements.txt

lint:
	python -m flake8 ./pydemo

test: clean lint
	nosetests tests

build: test
	python setup.py bdist_egg

install: build
	python setup.py install

publish: build
	python setup.py sdist upload -r pypi

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -fr build/
	rm -fr dist/
	rm -fr pydemo.egg-info/
	rm -fr coverage/
	rm -f .coverage
	rm -f .noseids
