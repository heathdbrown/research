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

# Agent-containers errors

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

>Dockerfile
```Dockerfile
# Build stage
FROM agent-base AS builder

# 1. Install global modules
RUN npm install -g opencode-ai && \
  npm install -g @anthropic-ai/claude-code && \
  echo "Installed Open Code version: $(opencode --version)"

# Runtime stage
FROM agent-base

# Copy the installed global modules from builder
COPY --from=builder --chown=node:node /home/node/.npm-global /home/node/.npm-global


# Display version information
RUN echo "" && \
  echo "\e[34m=================================================================\e[0m" && \
  echo "\e[34m                   OPEN CODE VERSION                           \e[0m" && \
  echo "\e[34m=================================================================\e[0m" && \
  echo "\e[34m" && opencode --version && \
  echo "\e[0m" && \
  echo ""

USER 0

CMD ["opencode"]
```

>~/.local/bin/open-code
```bash
#!/usr/bin/env bash
PROJ="$(basename "$(pwd)")"
NAME="open-code-${PROJ}"
# Create a clean config dir with just the config file
CONFIG_DIR="$HOME/.config/opencode-config"
mkdir -p "$CONFIG_DIR"
# Ensure opencode.json exists with at least empty config
[ -f "$CONFIG_DIR/opencode.json" ] || echo '{}' >"$CONFIG_DIR/opencode.json"
exec docker run --rm --tty --interactive \
  --name "$NAME" \
  --add-host=host.docker.internal:host-gateway \
  -v "$CONFIG_DIR:/home/node/.config/opencode" \
  -v "$HOME/.local/share/opencode:/home/node/.local/share/opencode" \
  -v "$HOME/.local/state/opencode:/home/node/.local/state/opencode" \
  -v "$(pwd):/app:rw" \
  -e OPENCODE_API_KEY="${OPENCODE_API_KEY:-}" \
  open-code "$@"
```

# References
- https://github.com/faileon/agent-containers/blob/main/open-code/README.md
