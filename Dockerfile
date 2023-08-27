FROM python:3.11-slim

ENV PATH="/root/.local/bin:${PATH}" VERSION=${VERSION}

WORKDIR /app

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    ca-certificates libpq5 curl build-essential libpq-dev postgresql-client \
    && curl -sSL https://install.python-poetry.org/ | POETRY_VERSION=1.6.1 python3.11 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3.11 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV VIRTUAL_ENV="/opt/venv"

COPY poetry.lock pyproject.toml ./

RUN pip install pip --upgrade
RUN poetry install --only main --no-directory --no-root

COPY ./ ./

RUN poetry install --only main

RUN useradd --create-home app
USER app

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "-c", "gunicornconfig.py" ]
CMD ["example_app.__main__:app"]
