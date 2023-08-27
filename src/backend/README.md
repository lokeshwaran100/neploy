# Setting up the Kubernetes Cluster Backend
## Prerequisites
Before you proceed with setting up the backend for Neploy, please ensure that you have the following prerequisites in place:
1. **Kubernetes Cluster:** You should have a Kubernetes cluster deployed and accessible. If you don't have a Kubernetes cluster, you can deploy one using tools like [Minikube](https://minikube.sigs.k8s.io/), [k3s](https://k3s.io/), or on cloud providers like [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine), [Amazon EKS](https://aws.amazon.com/eks/), or [Microsoft Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/services/kubernetes-service/).
2. **kubectl:** Ensure that you have the `kubectl` command-line tool installed and configured to interact with your Kubernetes cluster.
3. **Docker:** You should have Docker installed on your local machine to build and push Docker images. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).
4. **Container Registry:** You'll need access to a container registry to push your Docker images. Popular options include [Docker Hub](https://hub.docker.com/), [Google Container Registry](https://cloud.google.com/container-registry), and [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/).

To deploy the backend for Neploy on a Kubernetes cluster, follow these steps:

1. Navigate to the backend src files directory:
```bash
cd neploy-build-python
```
2. Build the Docker image using the provided Dockerfile:
```bash
docker build --tag neploy-build-python:latest .
```
3. Push the Docker image to a container registry of your choice (e.g., Docker Hub, Google Container Registry):
```bash
docker tag neploy-backend <registry-name>/neploy-build-python:latest
docker push <registry-name>/neploy-build-python:latest
```
This Dockerfile uses an Ubuntu base image to create a containerized environment for the backend.

4. Open a terminal and make sure you have kubectl configured to access your Kubernetes cluster.

5. Deploy the Kubernetes pod containing the backend using the following command:
```bash
kubectl apply -f neploy-build-python/deployment.yaml
```
This deployment.yaml file specifies a pod running the Python Flask scripts for the backend. The /build endpoint is exposed to compile code, and the /optimise endpoint is exposed for AI/ML code review.

6. Deploy the service endpoint for the backend:
```bash
kubectl apply -f neploy-build-python/service.yaml
```
This service.yaml file creates a Kubernetes service to expose the pod's endpoints within the cluster.

Once the service is deployed, you can access the backend endpoints from your frontend application using the Kubernetes service's ClusterIP and port.

Ensure that the frontend makes POST REST API calls to the /build and /optimise endpoints of the backend pod to submit code for compilation and AI/ML code review respectively.

Your Kubernetes cluster backend for Neploy is now set up and ready to handle code compilation and AI/ML code review requests from the frontend.

Please note that these steps are general guidelines and might need adjustments based on your Kubernetes cluster setup and networking configurations.

