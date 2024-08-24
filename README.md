# URL Shortener Microservices

## Project Overview

This is a microservices-based URL Shortener application built using Flask and Flask-RESTful in Python. The application consists of multiple microservices that handle different aspects of URL shortening and redirection. Each service is containerized using Docker and can be deployed on a Kubernetes cluster.

### Microservices Overview

- **API Gateway Service:** Routes incoming requests to the appropriate microservices.
- **URL Shortening Service:** Generates short URLs and stores them in MongoDB.
- **Redirection Service:** Handles redirection from shortened URLs to original URLs.
- **Caching Service:** Manages caching using Memcached for faster access to frequently used URLs.

## Prerequisites

- Docker
- Kubernetes (Minikube, Docker Desktop, or any Kubernetes cluster)
- Kubectl
- Python 3.x
- MongoDB
- Memcached

## Directory Structure

```plaintext
url_shortener_microservices/
│
├── api_gateway/
│   ├── app.py
│   ├── Dockerfile
│   └── deployment.yaml
│
├── url_shortener_service/
│   ├── app.py
│   ├── Dockerfile
│   └── deployment.yaml
│
├── url_redirection_service/
│   ├── app.py
│   ├── Dockerfile
│   └── deployment.yaml
│
├── caching_service/
│   ├── app.py
│   ├── Dockerfile
│   └── deployment.yaml
│
├── mongodb/
│   └── deployment.yaml
│
└── build_and_push.sh
```

## Building and Pushing Docker Images

### Step 1: Modify the Script

Update the `build_and_push.sh` script with your Docker registry URL or username.

```bash
DOCKER_REGISTRY="your-docker-registry"
```

### Step 2: Run the Build and Push Script

Make sure you are logged into your Docker registry, then run the script to build and push all the microservices' Docker images:

```bash
./build_and_push.sh
```

This script will build Docker images for each microservice and push them to your specified Docker registry.

## Deploying to Kubernetes

### Step 1: Deploy MongoDB and Memcached

First, deploy MongoDB and Memcached to your Kubernetes cluster:

```bash
kubectl apply -f mongodb/deployment.yaml
kubectl apply -f memcached/deployment.yaml
```

### Step 2: Deploy Microservices

Next, deploy each microservice:

```bash
kubectl apply -f api_gateway/deployment.yaml
kubectl apply -f url_shortener_service/deployment.yaml
kubectl apply -f url_redirection_service/deployment.yaml
kubectl apply -f caching_service/deployment.yaml
```

### Step 3: Verify Deployments

Check the status of the deployments to ensure everything is running correctly:

```bash
kubectl get pods
```

You should see all services up and running.

### Step 4: Accessing the Application

- **API Gateway:** The API Gateway will be exposed via a Kubernetes Service. You can access it by forwarding the port or exposing it via a LoadBalancer, depending on your Kubernetes setup.

Example to forward the port:

```bash
kubectl port-forward service/api-gateway 8080:80
```

Now you can access the API Gateway at `http://localhost:8080`.

## API Endpoints

### 1. Shorten URL

**Endpoint:** `/shorten`  
**Method:** `POST`  
**Description:** Shortens a given URL.

**Request Body:**

```json
{
  "url": "http://example.com"
}
```

**Response:**

```json
{
  "shortened_url": "http://localhost:8080/abc123"
}
```

### 2. Redirect to Original URL

**Endpoint:** `/<short_id>`  
**Method:** `GET`  
**Description:** Redirects to the original URL corresponding to the given short ID.

**Example:**

```bash
http://localhost:8080/abc123
```

This will redirect the user to the original URL stored in the database.

## Testing the Application

### Shorten a URL

To test the URL shortening functionality, use a tool like `curl` or Postman to send a POST request:

```bash
curl -X POST http://localhost:8080/shorten -H "Content-Type: application/json" -d '{"url": "http://example.com"}'
```

You should receive a response with a shortened URL.

### Redirect Using Shortened URL

After shortening a URL, you can test the redirection by navigating to the shortened URL in your browser:

```bash
http://localhost:8080/abc123
```

This should redirect you to the original URL.

### Error Handling

You can test error handling by:

- Disconnecting MongoDB or Memcached and observing how the services handle these situations.
- Sending invalid requests (e.g., missing URL field in the POST request).

The application should handle these gracefully and provide appropriate error messages.

## Cleanup

To remove the deployments from your Kubernetes cluster, you can use the following commands:

```bash
kubectl delete -f api_gateway/deployment.yaml
kubectl delete -f url_shortener_service/deployment.yaml
kubectl delete -f url_redirection_service/deployment.yaml
kubectl delete -f caching_service/deployment.yaml
kubectl delete -f mongodb/deployment.yaml
kubectl delete -f memcached/deployment.yaml
```

## Contributing

Feel free to fork this repository and submit pull requests if you would like to contribute to this project. All contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


