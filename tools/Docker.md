# Docker Commands

# Docker Compose Commands
- docker compose up
- docker compose down
- docker compose run


# Docker Third Party tools
- [Docker run to Docker Compose](https://www.composerize.com/)

# Issues with Docker Desktop on Windows

## Error response from daemon: no command specified
- this error happens on both the docker run command and the docker compose file when turning up the netscaler cpx image.
- similar issues found
  - https://forums.docker.com/t/how-to-fix-error-response-from-daemon-no-command-specified/128302/14

```bash
 docker compose up
[+] Running 1/2
 ✔ Network netscaler_default  Created                                                                              0.1s
 - Container cpx-hello-world  Creating                                                                             0.0s
Error response from daemon: no command specified
```

```docker
name: netscaler
services:
    netscaler-cpx:
        tty: true
        privileged: true
        environment:
            - EULA=yes
        ulimits:
            core: -1
        container_name: cpx-hello-world
        image: cpx:14.1-34.42
```

Attempted
- upgrading Docker desktop
  - upgraded version
  - running the commands from the k8s documentation run 'works'
  - https://github.com/netscaler/netscaler-k8s-ingress-controller/blob/master/deployment/aws/quick-deploy-cpx/README.md

```
 docker version
Client:
 Version:           27.3.1
 API version:       1.47
 Go version:        go1.22.7
 Git commit:        ce12230
 Built:             Fri Sep 20 11:42:27 2024
 OS/Arch:           windows/amd64
 Context:           desktop-linux

Server: Docker Desktop 4.35.1 (173168)
 Engine:
  Version:          27.3.1
  API version:      1.47 (minimum version 1.24)
  Go version:       go1.22.7
  Git commit:       41ca978
  Built:            Fri Sep 20 11:41:11 2024
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.7.21
  GitCommit:        472731909fa34bd7bc9c087e4c27943f9835f111
 runc:
  Version:          1.1.13
  GitCommit:        v1.1.13-0-g58aa920
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```



```bash
docker run -dt -P --privileged=true -e EULA=yes --ulimit core=-1 --name cpx-hello-world quay.io/netscaler/netscaler-cpx:14.1-25.111
```

```bash
docker exec -it cpx-hello-world bash
```

```bash
docker exec -it cpx-hello-world cli_script.sh "show ns ip"
exec: show ns ip
        Ipaddress        Traffic Domain  Type             Mode     Arp      Icmp     Vserver  State
        ---------        --------------  ----             ----     ---      ----     -------  ------
1)      172.17.0.2       0               NetScaler IP     Active   Enabled  Enabled  NA       Enabled
2)      192.0.0.1        0               SNIP             Active   Enabled  Enabled  NA       Enabled
Done
```

### WSL Docker no systemd

```
sudo service docker start
```

### WSL Docker systemd
* Enable Systemd
```
# vim /etc/wsl.conf
[boot]
systemd=true
reboot

sudo systemctl enable docker.service
sudo systemctl start docker.service
```

# References
- https://docs.docker.com/storage/volumes/