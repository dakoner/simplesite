docker rm -f flask ; \
docker run -tid -p 80:8080 --name flask flask && \
docker logs -f flask