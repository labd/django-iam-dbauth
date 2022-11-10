.PHONY: install test upload docs format

install:
	pip install -e .[docs,test]

test:
	py.test

retest:
	py.test -vvv --lf

coverage:
	py.test --cov=django_iam_dbauth --cov-report=term-missing --cov-report=html

docs:
	$(MAKE) -C docs html

release:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

format:
	isort --profile black src tests
	black -t py310 src/ tests/
