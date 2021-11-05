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
	sed -i 's/docker /podman /g' Makefile
	# Same adjustment here for podman-compose
	se -i 's/docker-compose -f/podman-compose -f/g' Makefile
    make docker-compose-build
    make docker-compose
}

function main() {
	install_ansible
	install_awx
}

main
