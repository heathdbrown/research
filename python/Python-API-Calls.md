Probably need a better title
> https://www.youtube.com/watch?v=E39a7kQfjSg

## Use a session

```python
import requests

def create_session():
    s = requests.Session():
    return s

def main():
    sess = create_session()
    resp = sess.get(creds.url + "/api/blah")

if __name__ == '__main__':
   main()
```

## Event Hooks
- https://requests.readthedocs.io/en/latest/user/advanced/#event-hooks

# Credentials
- https://swharden.com/blog/2021-05-15-python-credentials/
- https://janakiev.com/blog/python-credentials-and-configuration/#python-configuration-files