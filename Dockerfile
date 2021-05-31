FROM python:3.8-buster
LABEL maintainer="IndraP24 - Indrashis Paul"

RUN apt-get update

RUN mkdir -p /usr/app
WORKDIR /usr/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /usr/app/

EXPOSE 5000

CMD uvicorn app:app --reload