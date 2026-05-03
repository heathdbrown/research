# Overview
I like opencode for a coding agent. I wanted to attempt to run opencode in a container, these are the notes.

# Finding someone else's work

I found several articles and github repos from reddit and uesrs online. I tried several.

https://www.reddit.com/r/opencodeCLI/comments/1qbtyql/docker_container_for_opencode/

- https://github.com/asfaload/agents_container
- https://github.com/glennvdv/opencode-dockerized/tree/main#-troubleshooting

The container would execute, however, opencode would never initialize and I would have a blank cli terminal for a period of time with the CPU spinning.

I settled on agent-conters (see references).

side note: I run rootless docker and there are some quirks that need to be addressed with that setup I had to modify the the open-code/Dockerfile to run as ROOT so that the rootless docker would user mapping would work properly.

# AGent-containers errors

## Error 
```bash
EACCES: permission denied, mkdir '/home/node/.local/share/opencode/log'
    path: "/home/node/.local/share/opencode/log",
 syscall: "mkdir",
   errno: -13,
    code: "EACCES"


Bun v1.3.13 (Linux x64 baseline)
```

## Solution
- modify open-code/Dockerfile to run as root and use the auto mapping feature of rootless docker
- Remove the --user from the docker run command

# References
- https://github.com/faileon/agent-containers/blob/main/open-code/README.md
