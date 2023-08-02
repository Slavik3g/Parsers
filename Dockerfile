FROM python:3.11.1

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip && pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . /app
