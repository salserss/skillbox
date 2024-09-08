FROM python:latest

RUN apt update && apt install -y postgresql-client

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .


RUN pip install -r requirement.txt

COPY . .