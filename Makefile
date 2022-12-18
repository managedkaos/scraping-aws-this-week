all: env requirements lint script

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

script:
	python -O script.py

clean:
	rm -vf meta.json

freeze:
	flask freeze

.PHONY: all env requirements lint local freeze clean script
