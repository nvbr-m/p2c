FROM python:3.8.11-slim-buster

RUN apt-get update && apt-get install -y \
curl
RUN curl -fsSL https://get.docker.com/ | sh

WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .