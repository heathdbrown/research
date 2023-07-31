# wget
downloading websites

```bash
# for authenticated website using cookies
wget --keep-session-cookies --save-cookies cookies.txt --post-data 'username=<username>&password=<password>' http://<target>/path/to/login
```

```bash
wget --load-cookies cookies.txt -r -p http://<target>/path/
```

```bash
# if cookie does not work manual load of cookies
wget --no-cookies --header "Cookie: <cookieid>="<cookie value>" -r -p http://<target>/path/
```


## Use wget to enumerate all known file links, but don't download the file

Use a loop of a list of domain and enumerate all file links.

```bash

for domain in `cat domain-list.txt`; do wget -r --no-parent --spider -U "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183" https://$domain 2>&1 | tee $domain.log

```

To make this easier you can create a function and then call that function instead of the giant command

```bash
# vim ~/.bashrc

function wgetspider {
    wget -r --no-parent --spider -U "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183" https://$1 2>&1 | tee $1.log
}
```