PY=python

.PHONY: setup lint test serve-api serve-ui format docker-build

setup:
	$(PY) -m pip install -e .[dev]

lint:
	ruff check . && black --check . && isort --check-only .

format:
	black . && isort .

test:
	pytest -q --maxfail=1 --disable-warnings

serve-api:
	uvicorn api.main:app --reload --port 8001

serve-ui:
	streamlit run ui/App.py

docker-build:
	docker build -t data-app-api -f docker/Dockerfile.api .
	docker build -t data-app-ui -f docker/Dockerfile.ui .
