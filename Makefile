# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

clean:
	-find . -name '*.pyc' -delete
	-find . -name '__pycache__' -delete

deps:
	pip install -r requirements.txt

docs: clean
	(cd docs && make html)

run: clean
	python run.py

bot_id: clean
	python -m scripts.print_bot_id

tests: clean
	python run_tests.py

flake8:
	flake8 .

.PHONY: help
help:
	@echo "\nPlease call with one of these targets:\n"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F:\
        '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}'\
        | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs | tr ' ' '\n' | awk\
        '{print "    - "$$0}'
	@echo "\n"
