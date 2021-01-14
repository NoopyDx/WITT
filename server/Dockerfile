from python:3.9.0-alpine

WORKDIR /app

ADD requirements.txt /app/backend/

RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r backend/requirements.txt

ADD . /app/backend
RUN chmod +x /app/backend/entrypoint.sh