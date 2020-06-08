init:
	pip install -r requirements.txt

init-dev:
	pip install -r dev-requirements.txt

testox:
	tox

testloc:
	py.test

.PHONY: init init-dev test
