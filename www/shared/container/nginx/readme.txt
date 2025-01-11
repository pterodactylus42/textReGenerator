This nginx contains the site where the prediction is called and displayed.

Start the server with the following commands:
docker build -t etah-server .
docker run -d --network etah-network -p 8080:80 -v /var/www/shared/container/nginx/default.conf:/etc/nginx/conf.d/default.conf:ro --rm etah-server
