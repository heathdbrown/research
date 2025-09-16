# Bash resources and commands to help build snippets
- [shellexplained](https://explainshell.com/)
- [Talk Python to Me - Ep 392 - Data Science from CLI](https://talkpython.fm/episodes/show/392/data-science-from-the-command-line)

# curl

```bash
curl -Iks https://www.google.com
```

* `-I` - show response headers only
* `-k` - insecure connection when using ssl
* `-s` - silent mode (not display body)

# Generic Snippets
- Using ping with `&&` and `||` for an action afterwards based on positive or negative.

```bash
ping 1.1.1.1 -c 3 && echo "It's UP" || echo "It's Down"
```

- replace first char with " and rewrite file
```bash
sed -i 's/^/"/g' file
```

- replace last char of line with ", and rewrite file
```bash
sed -i 's/$/",/g' file
```

- add line to bottom
```bash
sed -i "\$a]" file
```
- add line to top of file
```bash
sed -i "1 i[" file
```
- seq of numbers 
```bash
seq 1 58
```

- for loop with seq
```bash
for i in $(1 58); do echo $i; done
```

- take list of devices with device number and create seperate batches with just devices
```bash
for i in $(seq 81 158); do cat all-batches | grep $i$ | awk '{print $1}' | tr [:upper:] [:lower:] > batch$i; done
```

- run a sequence cp files on success add " to each line then add ", to end of lines then remove the last ',' on the last line then add ] to the last line then add [ to the first line

```bash
for i in $(seq 81 158); do cp batch$i batch$i-upload && sed -i 's/^/"/g' batch$i-upload && sed -i 's/$/",/g' batch$i-upload && sed -i '$ s/.$//' batch$i-upload && sed -i "\$a]" batch$i-upload && sed -i "1 i[" batch$i-upload; done
```

- Remove the first character of a file and replace in place
```bash
sed -i "1s/^.//" file
```
- Remove last character of a file and replace in place
```bash
sed -i "$ s/.$//" file
```

- Print the last awk'd field
```bash
awk '{print $NF}'
```

- Print the first awk'd field
```bash
awk '{print $1}'
```

- ssh agent functions
```bash
SSH_ENV="$HOME/.ssh/environment"

function start_agent {
    echo "Initialising new SSH agent..."
    /usr/bin/ssh-agent | sed 's/^echo/#echo/' > "${SSH_ENV}"
    echo succeeded
    chmod 600 "${SSH_ENV}"
    . "${SSH_ENV}" > /dev/null
    /usr/bin/ssh-add;
}

# Source SSH settings, if applicable

if [ -f "${SSH_ENV}" ]; then
    . "${SSH_ENV}" > /dev/null
    #ps ${SSH_AGENT_PID} doesn't work under cywgin
    ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
        start_agent;
    }
else
    start_agent;
fi
```

- Create a SSL certificate from a single line in bash for the correct format

```bash
(
  echo "-----BEGIN CERTIFICATE-----"; 
  echo $CERTIFICATE | sed -e "s/.\{67\}/&\n/g"; 
  echo "-----END CERTIFICATE-----";
) > certificate.pem
```

- Flush Single Entry in ARP table
```bash
arp -d <IP>
```

- Flush Whole ARP Table 
```bash
ip -s -s neigh flush all
```

- Compare two files with sorting without creating a new file and make two column output
```bash
diff <(foo) <(bar) -y 
```

- nmap ping scan only
```bash
nmap -sn -PE <target>
```

- Test Port without nmap or telnet
```bash
nc -v -z -w1 <target> <port>
```

- Print 1st column data
```bash
cat <file> | awk '{print $1}'
```

- Network Tools
  - nethogs
  - bmon
  - iftop -i eth0
  - netstat
  - ss

- tcpdump for top talkers based on source
```bash
tcpdump -tnnr 2016-02-02.pcap | awk -F "." '{print $1"."$2"."$3"."$4}' | sort | uniq -c | sort -nr | head
```

- Grep, awk, sed, uniq for returning unique parameters
```bash
cat <file> | grep <text> | awk '{print $1}'| sed s/[[0-9]*]//g | uniq
```

# Grep Snippets
Consider using the application [gf](https://github.com/tomnomnom/gf) which takes standard grep patterns and makes it easier to apply and remember them with simple syntax.

- Grep for RFC1918 IP addresses
```bash
grep -P "(10.|192.168|172.1[6-9].|172.2[0-9].|172.3[01].).* "
```

- Grep for IP addresses (invalid|valid)
```bash
 grep -oE "([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
```

# Wget Snippets
- Wget timestamping as per [Lars Appel - wget](http://www.editcorp.com/Personal/Lars_Appel/wget/wget_5.html)
```bash
# downloads files from site with 'last modified' timestamps
wget -S http://www.gnu.ai.mit.edu/

# Reattempt to download later and it checks the last-modified headers against the local last modified dates
wget -N http://www.gnu.ai.mit.edu/
```

### Wget process for login and use cookies for download
- Wget process for grabbing cookies for authentication and saving cookies

```bash
# for authenticated website using cookies
wget --keep-session-cookies --save-cookies cookies.txt --post-data 'username=<username>&password=<password>' http://<target>/path/to/login
```

- Load saved cookies and use recursive to download

```bash
wget --load-cookies cookies.txt -r -p http://<target>/path/
```

- If manual load of cookie does not work manual method to set cookies in wget

```bash
# if cookie does not work manual load of cookies
wget --no-cookies --header "Cookie: <cookieid>="<cookie value>" -r -p http://<target>/path/
```


### Use wget to enumerate all known file links, but don't download the file

- Use a loop of a list of domain and enumerate all file links.

```bash

for domain in `cat domain-list.txt`; do wget -r --no-parent --spider -U "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183" https://$domain 2>&1 | tee $domain.log

```

- To make this easier you can create a function and then call that function instead of the giant command

```bash
# vim ~/.bashrc

function wgetspider {
    wget -r --no-parent --spider -U "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183" https://$1 2>&1 | tee $1.log
}
```

- Gathering all urls from the $1.log

```bash
cat '^---' $1.log | awk '{print $NF}' | sort | uniq > urls.txt
```

# Reference
- https://github.com/trimstray/the-book-of-secret-knowledge?tab=readme-ov-file#shell-one-liners-toc