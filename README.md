docker build --tag flask flask && docker rm -f flask; docker run -tid -p 8080:8080 -v $(pwd)/flask/app:/app --name flask flask 
docker build --tag nginx nginx && docker rm -f nginx; docker run -tid -p 80:80 -v $(pwd)/nginx/html:/var/www/html --name nginx nginx
