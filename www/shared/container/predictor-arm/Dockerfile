# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# docker build -t etah-predictor-arm -f predictor-arm/Dockerfile . 
# needs to be called from the parent dir (shared/container) for this to work
# Copy the requirements file into the container
COPY predictor-arm/requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY predictor/ .

# Command to run the application
CMD ["python","predict.py"]
