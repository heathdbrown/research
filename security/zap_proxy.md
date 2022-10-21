# Zap Proxy
- https://www.zaproxy.org/download/
- https://www.zaproxy.org/getting-started/

# Prereqs
You need Java for this installed. Tested with Amazon Coretto on Windows and openjdk on Ubuntu.

# Install
- Install and and open

```bash
sudo apt install openjdk-17-jre -yq
wget https://github.com/zaproxy/zaproxy/releases/download/v2.11.1/ZAP_2_11_1_unix.sh | sh
chmod +x ZAP_2_11_1_unix.sh
./ZAP_2_11_1_unix.sh
zap.sh -daemon # put Zap proxy in daemon mode
```

Once 'started' you will need to set your proxy in your browser to <ip>:8080.

Then start browsing the site.

If you can and know a username and password 'login' to capture the request and response.

# Setup Context
- https://www.zaproxy.org/docs/desktop/ui/dialogs/session/context-auth/#form-based-authentication

if you have the request you can 'highlight' the text and right click 'add to context'

and assign it to login.