all: env requirements lint script

env:
	python -m venv ./env

activate:
	. ./env/bin/activate

requirements: activate
	pip install --quiet --upgrade pip
	pip install --quiet --requirement requirements.txt

lint: activate
	flake8 --exit-zero --ignore=E128,E501  *.py
	pylint --exit-zero *.py

local: activate
	python tags.py --local

script: activate
	python -O script.py

clean:
	rm -vf meta.json

freeze: activate
	flask freeze

.PHONY: all env activate requirements lint local freeze clean script
