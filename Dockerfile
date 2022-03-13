FROM python:3

ENV PYTHONBUFFERED 1
ENV C_FORCE_ROOT true
STOPSIGNAL SIGTERM

# RUN apk add --virtual build-deps postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libcurl curl-dev libmagic

# Needed for pycurl
ENV PYCURL_SSL_LIBRARY=openssl

WORKDIR /manatal/app

RUN pip install -U pip && \
    pip install pipenv

COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock

RUN pipenv install --system

ADD . /manatal

EXPOSE 8000

CMD gunicorn -w 3 app.wsgi -b :8000
# --worker-class eventlet