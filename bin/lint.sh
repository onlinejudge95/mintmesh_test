#!/bin/bash

black --check --diff --target-version py37 .
flake8 --exclude __init__.py --max-line-length 88 .
