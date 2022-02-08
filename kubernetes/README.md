# Kubernetes 

# common commands

|Command|Purpose|
|-------|-------|
|kubeadm init --pod-network-cidr=192.168.0.0/16| Initilializes cluster with specific pod network|
|kubadm reset --v=5| Resets the cluster installation and clean-ups everything BUT iptables, ipvs|
|kubectl get nodes -o wide| Displays nodes|
|kubeadm join $KUBE_MASTER_IP:6443 --token $KUBE_TOKEN --discovery-token-unsafe-skip-ca-verification|  Joins new member to cluster and skips CA verificiation check; not recommended|
|kubectl create  deployment $deployment-name --image=$image| Creates a new deployment for a pod|
|kubectl get deployments| View deployment|
|kubectl get pods| View pods|
|kubectl get events| View cluster events|
|kubectl config view| View the kubectl configuration|
|kubectl expose deployment $deployment-name -type=LoadBalancer --port=$port| Create services and Expose the Pod to the public network|
|kubectl get services|Displays  services|


# commands
|Command|Purpose|
|-------|-------|
|kubectl taint nodes --all <node>| Removes 'taint' for master node to take on  additional duties in cluster|

# Jargon
- monolith: large old/legacy application; does all kinds of things
- microservices: small apps,  loosely coupled, deployed indepently.
- Deployment: description of service to deploy to k8s api
- Pod: Compute Execution Layer in kubernetes for keeping coupled containers together that typically share resources.
- Container: lowest layer and where the app runs
  
# References
- https://kubernetes.io/docs/tutorials/kubernetes-basics/
- https://github.com/nigelpoulton/getting-started-k8s
