import asyncio
from aiohttp import web


async def handle_root(request: web.Request) -> web.Response:
    """returns the simple text "Hello, World!
    """
    return web.Response(text="Hello, World!")


async def handle_slow(request: web.Request) -> web.Response:
    """simulates a long operation with a delay of 5 seconds and returns the text "Operation completed"
    """
    await asyncio.sleep(5)
    return web.Response(text="Operation completed")


async def init_app() -> web.Application:
    """Initializes the aiohttp web application and sets up routes.
    """
    app = web.Application()
    app.router.add_get("/", handle_root)
    app.router.add_get("/slow", handle_slow)
    return app


def main() -> None:
    """Entry point to run the aiohttp web server.
    """
    app = asyncio.run(init_app())
    web.run_app(app, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
