FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=itfoxnews.settings

RUN pip install --upgrade pip

RUN mkdir /itfoxnewsproject

WORKDIR /itfoxnewsproject

ADD . /itfoxnewsproject/

RUN pip install -r requirements.txt

EXPOSE 8000