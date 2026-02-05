import asyncio
import time
import random


async def download_page(url: str) -> None:
    """function accept a URL and “load” the page at random intervals of 1 to 5 seconds.
    After loading is complete, the function should display a message with the URL and load time
    """
    start_time = time.perf_counter()

    delay = random.randint(1, 5)
    await asyncio.sleep(delay)

    ended = time.perf_counter() - start_time
    print(f"Downloaded {url} for {ended:.2f} seconds.")


async def main(urls: list) -> None:
    """Loads multiple pages asynchronously at the same time
    """
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = [
        "https://phython.org",
        "https://www.ukrlib.com.ua/world/printit.php?tid=590&page=6",
        "https://github.com",
    ]

    asyncio.run(main(urls))
