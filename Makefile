.PHONY = mypy black test readme

test:
	py.test tests/

mypy:
	mypy --disallow-untyped-calls pyhtml/

black:
	black -S -l 160 pyhtml tests

readme:
	python README.py
