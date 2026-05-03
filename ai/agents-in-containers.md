# Overview
I like opencode for a coding agent. I wanted to attempt to run opencode in a container, these are the notes.

# Finding someone else's work

I found several articles and github repos from reddit and uesrs online. I tried several.

https://www.reddit.com/r/opencodeCLI/comments/1qbtyql/docker_container_for_opencode/

- https://github.com/asfaload/agents_container
- https://github.com/glennvdv/opencode-dockerized/tree/main#-troubleshooting

The container would execute, however, opencode would never initialize and I would have a blank cli terminal for a period of time with the CPU spinning.

I settled on agent-conters (see references).

side note: I run rootless docker and there are some quirks that need to be addressed with that setup I had to modify the 'command' script I was running 'open-code' and the open-code/Dockerfile for the correct persimissions set to write back to the host.

# References
- https://github.com/faileon/agent-containers/blob/main/open-code/README.md
