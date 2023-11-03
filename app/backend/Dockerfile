FROM python:3.11.1-slim as base

RUN pip install -U pip
RUN pip install poetry~=1.6.0

WORKDIR /app

COPY poetry.lock pyproject.toml ./
COPY cookbook/__init__.py ./cookbook/__init__.py
RUN poetry config virtualenvs.create false && poetry install --without dev --no-root --no-ansi --no-interaction

COPY cookbook/ ./


#
# ---- Dev Base ----
#
FROM base AS dev
RUN poetry install --only dev --no-ansi --no-interaction
COPY ./tests/ /app/tests
COPY ["./lint.sh", "./.flake8", "/app/"]


#
# ---- Release ----
#
FROM base AS release
CMD ["gunicorn", "cookbook.main:app", "--bind", "0.0.0.0:3001"]
