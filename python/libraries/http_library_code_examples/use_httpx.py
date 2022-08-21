import httpx
import asyncio

def test_get(url):
    r = httpx.get(url)
    print(f"Testing using requests.get to {url}")
    print(f"Response: {r.text}")
    print(f"Status Code: {r.status_code}")
    print(f"Raise for Status: {r.raise_for_status()}")

if __name__ == "__main__":
    test_get("https://httpbin.org/get")
    test_get("https://httpbin.org/uuid")
    test_get("https://httpbin.org/drip")
    test_get("https://httpbin.org/json")
    test_get("https://httpbin.org/status/429")