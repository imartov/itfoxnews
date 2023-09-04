FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir /itfoxnewsproject

WORKDIR /itfoxnewsproject

ADD . /itfoxnewsproject/

RUN pip install -r requirements.txt