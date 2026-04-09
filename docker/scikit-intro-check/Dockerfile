FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    UV_LINK_MODE=copy

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        git \
        libgomp1 \
        r-base \
        r-base-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip uv

WORKDIR /workspace

COPY sphinx/scikit-intro/pyproject.toml /workspace/pyproject.toml
COPY sphinx/scikit-intro/uv.lock /workspace/uv.lock
COPY sphinx/scikit-intro/source/_runtime.py /workspace/_runtime.py

RUN uv sync --frozen --no-dev --group notebook
RUN uv pip install --python /workspace/.venv/bin/python autoviz
RUN uv pip install --python /workspace/.venv/bin/python --upgrade xgboost
RUN uv pip install --python /workspace/.venv/bin/python --upgrade shap
RUN uv pip install --python /workspace/.venv/bin/python "pandas<3"

RUN .venv/bin/python - <<'PY'
from _runtime import ensure_nltk_data
ensure_nltk_data()
PY

WORKDIR /workspace
