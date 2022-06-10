FROM python:3.10.0a1-alpine3.12

COPY requirements.txt /app/requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ADD . .

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "churchclicks.wsgi:application"]

CMD gunicorn churchclicks.wsgi:application --bind 0.0.0.0:8000