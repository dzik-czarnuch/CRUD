# pull official base image
FROM python:3.10.2-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app.py

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt gunicorn.conf.py run.py ./
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /app/

EXPOSE 5000
CMD ["gunicorn", "--config", "gunicorn.conf.py", "run:app"]