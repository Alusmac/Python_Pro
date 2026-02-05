import asyncio
import aiohttp


async def download_image(session: aiohttp.ClientSession, url: str, filename: str) -> None:
    """ accepts the image URL and file name for saving
    """
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.read()

            with open(filename, "wb") as f:
                f.write(content)

        print(f"Downloaded {url} -> {filename}")

    except aiohttp.ClientResponseError as e:
        print(f"Error {url}: status {e.status}")

    except aiohttp.ClientConnectionError:
        print(f"Error {url}: cannot connect")

    except asyncio.TimeoutError:
        print(f"Error {url}: request timed out")

    except Exception as e:
        print(f"Error {url}: {e}")


async def main() -> None:
    """downloads multiple images concurrently using asyncio.gather
    """
    image_urls = [
        ("https://www.python.org/static/community_logos/python-logo.png", "python.png"),
        ("https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png", "js.png"),
        ("https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg", "r.png"),
    ]

    timeout = aiohttp.ClientTimeout(total=15)

    async with aiohttp.ClientSession(timeout=timeout, trust_env=True) as session:
        tasks = [
            download_image(session, url, filename)
            for url, filename in image_urls
        ]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
