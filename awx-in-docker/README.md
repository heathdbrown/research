# AWX in docker
> NOtes on running AWX in docker / podman on WSL

I attempted to adjust the Makefile to utilize podman so I did not have to have docker + Podman installed.

However, there are several different commands that utilize different parts of the docker cli.

docker-auth in issue https://github.com/heathdbrown/research/issues/23#issuecomment-961612639

Changing gears to a suggested guide to just do docker ce instead of podman on WSL
