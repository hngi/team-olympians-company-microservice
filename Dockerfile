FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

RUN sed -i "s|{% load staticfiles %}|{% load static %}|g" /usr/local/lib/python3.8/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html
