.PHONY: install test run

install:
	pip install -r requirements.txt -r requirements-dev.txt

test:
	pytest tests/ -v

run:
	uvicorn app.main:app --reload