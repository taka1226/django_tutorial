FROM python:3.10-bullseye
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_tutorial
WORKDIR /django_tutorial
COPY requirements.txt /django_tutorial/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /django_tutorial/

EXPOSE 8000
