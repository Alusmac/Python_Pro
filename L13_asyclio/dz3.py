import asyncio


async def producer(queue: asyncio.Queue) -> None:
    """ function that adds 5 tasks to the queue with a delay of 1 second
    """
    for i in range(1, 6):
        await asyncio.sleep(1)
        task = f"task-{i}"
        await queue.put(task)
        print(f"PRODUCER Added {task}")

    for _ in range(2):
        await queue.put(None)


async def consumer(queue: asyncio.Queue, consumer_id: int) -> None:
    """function that takes a task from the queue, executes it (for example, displays a message),
     simulating work with each task with a delay of 2 seconds.
    """
    while True:
        task = await queue.get()

        if task is None:
            queue.task_done()
            print(f"CONSUMER {consumer_id} Stopping")
            break

        print(f"CONSUMER {consumer_id} Processing {task}")
        await asyncio.sleep(2)
        print(f"CONSUMER {consumer_id} Finished {task}")

        queue.task_done()


async def main() -> None:
    """Entry point that starts producer and multiple consumers concurrently.
    """
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))

    consumers = [
        asyncio.create_task(consumer(queue, consumer_id=1)),
        asyncio.create_task(consumer(queue, consumer_id=2)),
    ]

    await asyncio.gather(producer_task)
    await queue.join()
    await asyncio.gather(*consumers)


if __name__ == "__main__":
    asyncio.run(main())
