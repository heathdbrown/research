# Kubernetes 

# common commands

|Command|Purpose|
|-------|-------|
|kubeadm init --pod-network-cidr=192.168.0.0/16| Initilializes cluster with specific pod network|
|kubadm reset --v=5| Resets the cluster installation and clean-ups everything BUT iptables, ipvs|
|kubectl get nodes -o wide| Displays nodes|
|kubeadm join <master ip address>:6443 --token <token> --discovery-token-unsafe-skip-ca-verification|  Joins new member to cluster and skips CA verificiation check; not recommended|


# commands
|Command|Purpose|
|-------|-------|
|kubectl taint nodes --all <node>| Removes 'taint' for master node to take on  additional duties in cluster|

# References
- https://github.com/nigelpoulton/getting-started-k8s
