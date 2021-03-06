#!/usr/bin/env bash

set -e
set -x

bash ./scripts/lint.sh
# Check README.md is up to date
poetry run python ./scripts/docs.py verify-readme
export PYTHONPATH=./docs_src
poetry run pytest --cov=fastapi --cov=tests --cov=docs/src --cov-report=term-missing --cov-report=xml tests ${@}
