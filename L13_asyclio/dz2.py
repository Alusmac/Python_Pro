import asyncio
import aiohttp


async def fetch_content(session: aiohttp.ClientSession, url: str) -> str:
    """makes an HTTP request and returns the page content
    """
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()

    except aiohttp.ClientResponseError as e:
        return f"Error {url}: status {e.status}"

    except aiohttp.ClientConnectionError:
        return f"Error {url}: cannot connect"

    except asyncio.TimeoutError:
        return f"Error {url}: request timed out"

    except Exception as e:
        return f"Error {url}: {e}"


async def fetch_all(urls: list[str]) -> list[str]:
    """Asynchronously loads all pages in parallel
    """
    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(
            timeout=timeout,
            trust_env=True
    ) as session:
        tasks = [fetch_content(session, url) for url in urls]
        return await asyncio.gather(*tasks)


async def main():
    """function defines a list of URLs, fetches their content asynchronously
    using `fetch_all`, and prints a preview of each response
    """
    urls = [
        "https://python.org",
        "https://www.ukrlib.com.ua/world/printit.php?tid=590&page=6",
        "https://docs.python.org/3/library/math.html",
    ]

    results = await fetch_all(urls)

    for url, content in zip(urls, results):
        print(f"\nURL: {url}")
        print(content[:200])


if __name__ == "__main__":
    asyncio.run(main())
