FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=itfoxnews.settings

WORKDIR /itfoxnewsdocker

COPY requirements.txt /itfoxnewsdocker/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /itfoxnewsdocker/

RUN apt-get update && apt-get install -y postgresql-client