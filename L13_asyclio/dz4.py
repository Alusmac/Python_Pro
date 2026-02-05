import asyncio


async def slow_task() -> None:
    """function, which simulates the execution of a task for 10 seconds
    """
    try:
        print("|TASK| Started slow_task")
        await asyncio.sleep(10)
        print("|TASK| Finished slow_task")

    except asyncio.CancelledError:
        print("|TASK| slow_task was cancelled")
        raise


async def main() -> None:
    """Runs slow_task with a timeout of 5 seconds.
    """
    try:
        await asyncio.wait_for(slow_task(), timeout=5)

    except asyncio.TimeoutError:
        print("|TIMEOUT| Task execution exceeded 5 seconds")


if __name__ == "__main__":
    asyncio.run(main())
