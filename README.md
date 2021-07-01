docker build --tag flask flask && docker rm -f flask; docker run -tid -p 80:8080 -v $(pwd)/flask/app:/app --name flask flask 
