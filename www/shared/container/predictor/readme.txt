This is a flask server that has the model loaded and can be called for a prediction.

Run it with the following commands:
docker network create etah-network
docker build -t etah-predictor .
docker run -d --network etah-network etah-predictor

The flask app listens on port 5000. 

Test the predictor with json as payload:
curl -X POST -H 'Content-Type: application/json' -d '{"sequence": [1, 2, 3, 4, 5]}'  172.18.0.2:5000/sum
when testing the prediction, the sequence length must be 40:
curl -X POST -H 'Content-Type: application/json' -d '{"sequence": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]}'  172.18.0.2:5000/next
