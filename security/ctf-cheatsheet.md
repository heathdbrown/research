# install tools
- git clone <sec-tools>
- cd sec-tools
- ./install.sh

# Enumerate target
- Start OWASP Zap proxy or mitmproxy
- Always go to /robots.txt
- Always go to /admin
- Port scan `nmap -A -p- -Pn $TARGET -v -oA nmap-initial.txt`
- Port scan `naabu -u $TARGET -o naabu-initial.txt`
- dirb `dirb $TARGET_URL -o dirb-initial.txt`
- grab urls from dirb files `gf urls dirb* | anew urls.txt`
- run `nuclei -u $TARGET`
- manually browse use extensions
  - wappalyzer to tell tech
  - owasp pentester to grab tech and vulns
  - verify proxy is on while browsing, CLICK EVERYTHING
  - first pass try simple ', or " in each form field
  - if we see 'text' coming back on the page from username and password, note the errors for later enumeration
- Research on book.hacktricks.xyz any tech or attack that might be interesting
# Online Tools
- https://github.com/zardus/ctf-tools
- https://gchq.github.io/CyberChef/
- https://gtfobins.github.io/
- https://github.com/swisskyrepo/PayloadsAllTheThings