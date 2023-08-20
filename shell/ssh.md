# Generating the ssh keys

```bash
ssh-keygen -t rsa
```

# Configuring the ssh client

Control the ssh client with ~/.ssh/config

Example below is to use older algorithms for older devices

```bash

Host 192.168.1.102
        user super
        KexAlgorithms +diffie-hellman-group14-sha1
        HostKeyAlgorithms +ssh-rsa

```

# Copying ssh authorized key

- By default the ssh-copy-id command will choose the `~/.ssh/.id_rsa.pub` if it exists.

```bash
ssh-copy-id <user>@<host>
```

# Running a ssh-agent

```bash
eval `ssh-agent`

echo $SSH_AGENT_SOCK
```

# Add keys to agent

By default it will add the ~/.ssh/id_rsa and other id* keys to the agent.

```bash
ssh-add

ssh-add -l
```

# Resources
- https://www.ssh.com/academy/ssh/agent