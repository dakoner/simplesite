pushd flask  && PYTHONPATH=app pytest -s && popd && docker build --tag flask flask && docker rm -f flask && docker run -tid -p 80:8080 -v $(pwd)/flask/app:/app --name flask flask && docker logs -f flask
