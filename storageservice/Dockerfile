# syntax=docker/dockerfile:1
FROM python:3.9.7-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install --upgrade pip 
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code
RUN cd /code
EXPOSE 8000
CMD ["gunicorn", "wsgi:application"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]