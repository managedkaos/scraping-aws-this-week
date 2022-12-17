all: env requirements lint meta.json

env:
	python -m venv ./env

requirements:
	pip install --quiet --upgrade pip
	pip install --quiet --requirement requirements.txt

lint:
	flake8 --exit-zero --ignore=E128,E501  *.py
	pylint --exit-zero *.py

local:
	python tags.py --local

meta.json:
	python script.py

freeze:
	flask freeze

.PHONY: all env requirements lint local freeze
