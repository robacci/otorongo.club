FROM python:3.6-buster
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y curl
RUN curl -L https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y gcc postgresql-client-13 libpq-dev musl-dev bash postgresql-13 && rm -rf /var/lib/apt/lists/*

RUN apt-get autoremove -y
RUN mkdir /pip_requirements
COPY requirements/base.txt /pip_requirements/base.txt
COPY .env /code/.env
RUN pip install -r /pip_requirements/base.txt

RUN mkdir -p /code
WORKDIR /code

ADD docker/wait_for_it.sh /wait_for_it.sh
RUN chmod +x /wait_for_it.sh

ADD . /code/
RUN ls /code

EXPOSE 8000
