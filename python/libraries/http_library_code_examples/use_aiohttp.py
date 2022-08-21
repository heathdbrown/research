import aiohttp
import asyncio

async def test_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
                print(f"Testing using requests.get to {url}")
                print(f"Response: {await r.text()}")
                print(f"Status Code: {r.status}")
                print(f"Raise for Status: {r.raise_for_status()}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_get('https://httpbin.org/get'))
    loop.run_until_complete(test_get("https://httpbin.org/uuid"))
    loop.run_until_complete(test_get("https://httpbin.org/drip"))
    loop.run_until_complete(test_get("https://httpbin.org/json"))
    loop.run_until_complete(test_get("https://httpbin.org/status/429"))