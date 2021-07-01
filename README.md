PYTHONPATH=app pytest -s && \
docker build --tag flask . && \
docker rm -f flask && \
docker run -tid -p 80:8080 --name flask flask && \
docker logs -f flask
