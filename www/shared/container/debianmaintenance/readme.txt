This is a maintenance linux that can be run on your docker host to test your setup.
build it with
docker network create etah-network
docker build -t debianmaintenance .
run it with
docker run -it --rm --network etah-network debianmaintenance

Test the predictor with : 
curl -X POST 172.20.0.2:5000/predict
