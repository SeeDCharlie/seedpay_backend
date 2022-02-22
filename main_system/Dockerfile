# syntax=docker/dockerfile:1
FROM python:3.9.7-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

#CMD ["gunicorn" , "-b", "0.0.0.0:8000", "main_system.wsgi"]

#/home/ec2-user/seedpay_backend/main_system/main_system/staticfiles
#server {
#  location / {
#    proxy_pass          http://localhost:8000;
#    proxy_set_header    Host $host;
#    proxy_set_header    X-Forwarded-Proto $scheme;
#  }
#
#  location /static {
#    autoindex on;
#    alias /var/www/supersecure.codes/static/;
#  }
#}
#sudo amazon-linux-extras install nginx1.12
