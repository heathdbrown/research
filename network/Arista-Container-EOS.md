# Overview

- Download the [cEOS-lab image](https://downloads.arista.com/cEOS-lab/EOS-4.31.1F/cEOS64-lab-4.31.1F.tar.xz) from Arista.com (you will need a valid account)
- Import the image into docker manually `docker import cEOS64-lab-4.31.1F.tar.xz ceosimage:4.31.1F`

# Arista Lab using Docker Compose file
```yaml
services:
  ansible:
    image: ansible:latest
    build:
      context: .
      tags:
        - ansible
      args:
        - ANSIBLE_CORE_VERSION=2.15.8
        - ANSIBLE_VERSION=8.7.0
        - ANSIBLE_LINT=6.22.2
    develop:
      watch:
        - action: sync
          path: ./playbooks
          target: /ansible
        - action: rebuild
          path: Dockerfile
  ceos1:
    hostname: CEOS-1
    privileged: true
    image: ceosimage:4.31.1F
    command: /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker
    ports: 
      - 6031:6030
      - 2001:22/tcp
    environment:
       - INTFTYPE=eth
       - ETBA=1
       - SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1
       - CEOS=1
       - EOS_PLATFORM=ceoslab
       - container=docker
    networks:
      default:
      p2p:
  ceos2:
    hostname: CEOS-2
    privileged: true
    image: ceosimage:4.31.1F
    command: /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker
    ports: 
      - 6032:6030
      - 2002:22/tcp
    environment:
       - INTFTYPE=eth
       - ETBA=1
       - SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1
       - CEOS=1
       - EOS_PLATFORM=ceoslab
       - container=docker
    networks:
      default:
      p2p:

networks:
  p2p:

```

# Attach to cli of containers using just Docker

```shell
docker exec -it ansible-networking-ceos1-1 Cli
docker exec -it ansible-networking-ceos2-1 Cli
```

# Attach to cli of containers using docker compose

```shell
docker compose exec -it ceos1 Cli
docker compose exec -it ceos2 Cli
```

# references
- https://github.com/arista-netdevops-community/ceos_lab_demo/tree/master
- https://arista.my.site.com/AristaCommunity/s/article/ceos-lab-topo
- https://containerlab.dev/manual/kinds/ceos/#__tabbed_1_1
- https://github.com/docker/compose/issues/123
- https://arista.my.site.com/AristaCommunity/s/article/arista-eos-hardening-guide