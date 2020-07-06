init:
	python setup.py develop

init-dev: init
	pip install supercell[test]

testox:
	tox

testloc:
	py.test

.PHONY: init init-dev test
