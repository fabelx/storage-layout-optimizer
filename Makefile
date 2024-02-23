VERSION=0.0.4
NAME = sl_optimizer
PIP = pip3
PYTHON = python
TWINE = twine
COVERAGE = coverage

.PHONY: all
all: clean install-dev test

.PHONY: info
info:
	@echo "${NAME} version: ${VERSION}"

.PHONY: clean
clean:
	@echo "Cleaning up distutils files"
	rm -rf dist
	rm -rf build
	rm -rf **/*.egg-info
	@echo "Cleaning up pytest files and .coverage"
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .benchmarks

.PHONY: build
build:
	$(PYTHON) -m build

.PHONY: install
install:
	$(PIP) install .

.PHONY: install-dev
install-dev:
	$(PIP) install .[dev]

.PHONY: install-test
install-test:
	$(PIP) install .[test]

.PHONY: install-lint
install-lint:
	$(PIP) install .[lint]

.PHONY: install-local-editable
install-local-editable:
	$(PIP) install -e .

.PHONY: install-twine
install-twine:
	$(PIP) install twine

.PHONY: uninstall
uninstall: clean
	$(PIP) freeze --exclude-editable | xargs $(PIP) uninstall -y

.PHONY: twine-check
twine-check: install-twine
	$(TWINE) check dist/*

# .pyirc must exist and contain the API-token
# https://packaging.python.org/en/latest/specifications/pypirc/
.PHONY: deploy
deploy: install-twine build
	$(TWINE) upload --skip-existing --repository pypi dist/*

# .pyirc must exist and contain the API-token
# https://packaging.python.org/en/latest/specifications/pypirc/
.PHONY: deploy-dev
deploy-dev: install-twine build
	$(TWINE) upload --skip-existing --repository testpypi dist/*

.PHONY: test
test: install-test unit

.PHONY: unit
unit:
	pytest --cov=$(NAME) --ignore=tests/benchmark tests -p no:warnings

.PHONY: benchmark
benchmark:
	pytest tests/benchmark -p no:warnings --capture=no

.PHONY: coverage
coverage:
	$(COVERAGE) report --rcfile=".coveragerc"

.PHONY: format
format:
	isort .
	black .

.PHONY: lint
lint: black isort flake8

.PHONY: black
black:
	black . --check

.PHONY: isort
isort:
	isort . --check-only

.PHONY: flake8
flake8:
	flake8 --toml-config pyproject.toml src/$(NAME)/
	flake8 --toml-config pyproject.toml tests/
