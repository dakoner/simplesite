PYTHONPATH=app pytest -s && \
docker build --tag flask . && \
docker rm -f flask && \
docker run -tid -p 80:8080 -v $(pwd)/flask/app:/app --name flask flask && \
docker logs -f flask
