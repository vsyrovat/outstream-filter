.PHONY: fmt test

fmt:
	black .

test:
	pytest -v