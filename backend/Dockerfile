FROM python:3.10-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y libgdal-dev

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.3.1

RUN pip install fastapi; pip install uvicorn

COPY backend_routes.py ./backend_routes.py

CMD ["uvicorn", "backend_routes:app", "--reload", "--port=8000", "--host", "0.0.0.0"]