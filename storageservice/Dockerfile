# syntax=docker/dockerfile:1
FROM python:3.9.7-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

#CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "main_system:wsgi"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]