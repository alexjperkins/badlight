FROM python:3.8-slim-buster
MAINTAINER Alex Perkins

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
	&& apt-get install -y build-essential \
	&& apt-get install -y libpq-dev \
	&& apt-get install -y gettext \
	&& apt-get purge -y --auto-remove -o API::AutoRemove::RecommendsImportant=false \
	&& rm -rf /var/lib/apt/lists/*

COPY ./requirements /requirements
RUN pip install -r ./requirements/development.txt

COPY ./compose/production/flask/entrypoint ./entrypoint
RUN sed -i 's/\r$//g' ./entrypoint
RUN chmod +x ./entrypoint

COPY ./compose/local/flask/start ./start
RUN sed -i 's/\r$//g' ./start
RUN chmod +x ./start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
