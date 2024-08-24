#!/bin/bash

# Set Docker registry and image names
DOCKER_REGISTRY="your-docker-registry"
API_GATEWAY_IMAGE="api-gateway"
URL_SHORTENER_IMAGE="url-shortener-service"
URL_REDIRECTION_IMAGE="url-redirection-service"
CACHING_SERVICE_IMAGE="caching-service"

# Build Docker images
echo "Building Docker images..."

docker build -t $DOCKER_REGISTRY/$API_GATEWAY_IMAGE:latest ./api_gateway
docker build -t $DOCKER_REGISTRY/$URL_SHORTENER_IMAGE:latest ./url_shortener_service
docker build -t $DOCKER_REGISTRY/$URL_REDIRECTION_IMAGE:latest ./url_redirection_service
docker build -t $DOCKER_REGISTRY/$CACHING_SERVICE_IMAGE:latest ./caching_service

echo "Docker images built successfully."

# Push Docker images to the registry
echo "Pushing Docker images to the registry..."

docker push $DOCKER_REGISTRY/$API_GATEWAY_IMAGE:latest
docker push $DOCKER_REGISTRY/$URL_SHORTENER_IMAGE:latest
docker push $DOCKER_REGISTRY/$URL_REDIRECTION_IMAGE:latest
docker push $DOCKER_REGISTRY/$CACHING_SERVICE_IMAGE:latest

echo "Docker images pushed to the registry successfully."
