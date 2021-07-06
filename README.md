PYTHONPATH=src pytest -s && \
docker build --tag flask . && \
docker rm -f flask ; \
docker run -ti -p 80:8080 --name flask flask