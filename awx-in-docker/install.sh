#!/bin/bash

function install_ansible() {
	# AWX requires ansible to install itself via containers
	pip install ansible --user
}

function install_awx() {
	AWX_VERSION=$(curl --silent https://github.com/ansible/awx/releases/latest | grep ansible/awx/releases/tag | grep -v rc | head -n 1 | sed 's/^.*tag\///' | sed 's/".*//')
	wget https://github.com/ansible/awx/archive/refs/tags/${AWX_VERSION}.tar.gz -q -O- - | tar xzv 
	cd awx-${AWX_VERSION}/
	# podman instead of docker
	#sed -i 's/docker /podman /g' Makefile
	# Same adjustment here for podman-compose
	#sed -i 's/docker-compose -f/podman-compose -f/g' Makefile
	# Remove docker-auth to fix issues
	sed -i 's/docker-auth //g' Makefile
	sed -i 's/docker-compose-sources: .git\/hooks\/pre-commit/docker-compose-sources:/g' Makefile
	sed -i "s/docker info | grep 'Operating System'/\"docker info | grep '    distribution:' | cut -d ':' -f 2 \"/g" tools/docker-compose/ansible/roles/sources/tasks/main.yml
	#sed -i "s/docker info | grep 'Operating System'/\"docker info | grep '    distribution:' | awk '{print \$2}'\"/g" tools/docker-compose/ansible/roles/sources/tasks/main.yml
        make docker-compose-build
        make docker-compose
}

function main() {
	install_ansible
	install_awx
}

main
