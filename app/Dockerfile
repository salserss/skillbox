FROM python:latest

RUN apt update && apt install -y postgresql-client

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements_prod.txt .


RUN pip install -r requirements_prod.txt

COPY . .