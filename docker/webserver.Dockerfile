FROM python:3.11-slim-buster

WORKDIR /webserver

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

RUN pip install --upgrade pip

RUN pip install poetry

COPY ./webserver/pyproject.toml .

COPY ./webserver/poetry.lock .

RUN poetry install --no-dev

COPY ./webserver/ .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
