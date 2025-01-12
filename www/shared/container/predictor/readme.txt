This is a flask server that has the model loaded and can be called for a prediction.

Run it with the following commands:
docker network create etah-network
docker build -t etah-predictor .
docker run -d --network etah-network etah-predictor

The flask app listens on port 5000. 
