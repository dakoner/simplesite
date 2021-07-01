FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV APT_LISTCHANGES_FRONTEND none

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip python3 && \
    pip3 install -r /tmp/requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY app /srv/app
RUN chown -R www-data /srv/app
USER www-data
WORKDIR /srv/app
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8080", "-t", "90", "--log-level", "DEBUG", "--access-logfile", "/dev/stdout", "--error-logfile", "/dev/stderr"]
