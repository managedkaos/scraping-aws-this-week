all: env requirements lint script freeze

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

script: activate
	python -O script.py

clean:
	rm -vf meta.json

freeze: activate
	flask freeze

.PHONY: all env activate requirements lint freeze clean script
