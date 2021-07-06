docker rm -f flask
docker run -tid -p 80:8080 --name flask  -e OAUTHLIB_INSECURE_TRANSPORT=1 -e OAUTHLIB_RELAX_TOKEN_SCOPE=1 flask
docker logs -f flask