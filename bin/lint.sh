#!/bin/bash

black --check --diff --target-version py37 .
flake8 --exclude __init__.py --max-line-length 88 .
isort --atomic --check --force-single-line-imports --lines-after-imports 2 --lines-between-types 1 --line-length 88 --profile black .
