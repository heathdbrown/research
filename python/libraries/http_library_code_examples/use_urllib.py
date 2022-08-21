import urllib.request

def test_get(url):
    r = urllib.request.Request(url=url)
    with urllib.request.urlopen(r) as f:
        print(f"Testing using requests.get to {url}")
        print(f"Response: {f.data}")
        print(f"Status Code: {f.status}")
        print(f"Raise for Status: {f.raise_for_status()}")

if __name__ == "__main__":
    test_get("https://httpbin.org/get")
    test_get("https://httpbin.org/uuid")
    test_get("https://httpbin.org/drip")
    test_get("https://httpbin.org/json")
    test_get("https://httpbin.org/status/429")