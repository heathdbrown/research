# Issue DNS resolution not working
 ping apple.com
ping: cannot resolve apple.com: Unknown host
Copy
1. Restart mDNSResponder

Restarting the mDNSResponder service can often resolve DNS issues.

sudo killall -HUP mDNSResponder
Copy
This command flushes the DNS cache and restarts the mDNSResponder service.

2. Check DNS Configuration

Ensure that your DNS settings are correctly configured. You can check your current DNS configuration using the scutil command.

scutil --dns
Copy
This command displays the current DNS configuration.

3. Manually Set DNS Servers

Sometimes, manually setting DNS servers can help resolve issues. You can use Google's public DNS servers (8.8.8.8 and 8.8.4.4) or OpenDNS servers (208.67.222.222 and 208.67.220.220).

networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4
Copy
Replace "Wi-Fi" with the name of your network interface.

4. Flush DNS Cache

Flushing the DNS cache can help clear any stale entries that might be causing issues.

sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
Copy
This command sequence clears the cache and restarts the mDNSResponder service.

5. Verify Network Connectivity

Ensure that your network connection is working correctly by pinging a known IP address.

ping 8.8.8.8
