FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Novosibirsk

RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir poetry

RUN poetry install --no-interaction --no-ansi --no-root --no-directory --without dev,test

COPY app/ ./app

RUN mkdir logs
