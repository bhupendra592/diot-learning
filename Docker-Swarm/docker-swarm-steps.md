# SET UP Docker Swarm

To deploy your Flask app using Docker Swarm with one manager node worker node.

# Follow the steps

# Initialize the Swarm on the Manager Node:

docker swarm init --advertise-addr <MANAGER-IP>

# Join Worker Nodes to the Swarm:

docker swarm join --token <TOKEN> <MANAGER-IP>:2377

# Build and Push Docker Hub Image

sudo docker build -t your-dockerhub-username/cdac-enrollment-app .

sudo docker push your-dockerhub-username/cdac-enrollment-app

# Deploy the stack

sudo docker service create --name <servicename> --replicas <replicanumber> -p 5000:5000 <dockerhubimage>

# Example

sudo docker service create --name cdac-enrollment-service --replicas 50 -p 5000:5000 diot224/cdac-enrollment-app

# Check the service

sudo docker service ls

# Remove the service

sudo docker service rm <serviceid>

# Scale the service <50 is the number of services>

sudo docker service update --replicas 50 <servicename>
or 

docker service update --replicas 50 <servicename>

# How to get NodeID # on Manager Node only

sudo docker node ls

# Check the service running on all the nodes

 sudo docker service ps cdac-enrollment-service

# Service Logs

sudo docker service logs cdac-enrollment-service

# Check Tasks for specific Node

sudo docker ps <nodeid>   # nodeid from sudo docker node ls

# Promote Worker to Manager

sudo docker node promote <nodeid>

# Leave the node

sudo docker swarm leave