Command

|Purpose|List All IPs, and do a mandatory DNS lookup|
|-------|-------------------------------------------|
|nmap -sL -R 192.168.1.0/24|List all IPs and resolve DNS|
|sudo nmap -PE <IP Subnet>| ICMP Echo scan a subnet ONLY; requires root for ICMP|
|nmap -n -vv -sn 192.168.1.1-255 -oG -|Ping sweep on a subnet in a grepable output|




