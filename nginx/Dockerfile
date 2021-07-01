FROM ubuntu:20.04

ENV APT_LISTCHANGES_FRONTEND none
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y -qq && \
    apt-get upgrade -y -qq && \
    apt-get install -y --no-install-recommends apt-utils nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN service nginx stop && \
    mkdir -p /var/run/nginx/cache

COPY nginx.conf /etc/nginx
CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]
