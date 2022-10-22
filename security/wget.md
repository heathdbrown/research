# wget
downloading websites

```bash
# for authenticated website using cookies
wget --keep-session-cookies --save-cookies cookies.txt --post-data 'username=<username>&password=<password>' http://<target>/path/to/login

wget --load-cookies cookies.txt -r -p http://<target>/path/
'''

'''bash
# if cookie does not work manual load of cookies
wget --no-cookies --header "Cookie: <cookieid>="<cookie value>" -r -p http://<target>/path/
'''