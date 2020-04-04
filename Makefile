.PHONY = mypy black

mypy:
	mypy --disallow-untyped-calls pyhtml/

black:
	black -S -l 160 pyhtml tests
