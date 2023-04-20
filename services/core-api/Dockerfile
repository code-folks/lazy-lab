# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.11.3
FROM python:$PYTHON_VERSION-slim-buster as dependencies

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_RUNTIME=/runtime/app

ENV APP_ROOT=$APP_RUNTIME
ENV POETRY_VERSION=1.4.2 \
    POETRY_VIRTUALENVS_CREATE=false

# Install updates and poetry
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && pip install "poetry==$POETRY_VERSION" \
    && useradd -U runtime_user
# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /runtime/
WORKDIR /runtime

# Project initialization:
RUN poetry install --no-interaction --no-ansi --no-root --no-dev

FROM dependencies as base
# Copy Python code to the Docker image
USER runtime_user:runtime_user
COPY --chown=runtime_user:runtime_user app $APP_RUNTIME
WORKDIR $APP_RUNTIME
RUN chmod +x ./docker/*.sh

CMD ["docker/container_bootstrap.sh", "uvicorn", "--host", "0.0.0.0", "--reload", "--loop", "uvloop", "--port", "8000", "--root-path", "/api", "--server-header", "lazy_lab.asgi:application" ]

FROM base as dev
USER root:root
# Dev env has the automigration included
ENV AUTOMIGRATE=True
RUN poetry install --no-interaction --no-ansi --no-root --only dev
