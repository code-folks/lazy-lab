# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=python:3.10
ARG RUNTIME_DIR=/runtime/app
ARG PROJECT_DIR=app

FROM $PYTHON_VERSION-slim-buster

ENV POETRY_VERSION=1.4 \
    POETRY_VIRTUALENVS_CREATE=false

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR $RUNTIME_DIR
COPY poetry.lock pyproject.toml $RUNTIME_DIR/

# Project initialization:
RUN poetry install --no-interaction --no-ansi --no-root --no-dev

# Copy Python code to the Docker image
COPY $PROJECT_DIR $RUNTIME_DIR/$PROJECT_DIR/

CMD [ "python", "handy_scan/foo.py"]

