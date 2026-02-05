import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def sync_task(n: int) -> int:
    """Synchronous task with 10ms
    """
    time.sleep(0.01)
    return n


async def async_task(n: int) -> int:
    """asynchronous task with 10ms
    """
    await asyncio.sleep(0.01)
    return n


def run_sync() -> float:
    """Synchronous processing
    """
    start = time.time()
    results = [sync_task(i) for i in range(500)]
    total = sum(results)
    elapsed = time.time() - start
    print(f"|SYNC| Elapsed: {elapsed:.2f}s, sum={total}")
    return elapsed


def run_threads() -> float:
    """Multithreaded processing
    """
    start = time.time()
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(sync_task, range(500)))
    total = sum(results)
    elapsed = time.time() - start
    print(f"|THREAD| Elapsed: {elapsed:.2f}s, sum={total}")
    return elapsed


def run_processes() -> float:
    """Multiprocessing
    """
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(sync_task, range(500)))
    total = sum(results)
    elapsed = time.time() - start
    print(f"|PROCESS| Elapsed: {elapsed:.2f}s, sum={total}")
    return elapsed


async def run_async() -> float:
    """Asynchronous processing
    """
    start = time.time()
    tasks = [async_task(i) for i in range(500)]
    results = await asyncio.gather(*tasks)
    total = sum(results)
    elapsed = time.time() - start
    print(f"|ASYNC| Elapsed: {elapsed:.2f}s, sum={total}")
    return elapsed


def main() -> None:
    """function to run all tests
    """
    print("Starting processing 500 requests...\n")

    sync_time = run_sync()
    thread_time = run_threads()
    process_time = run_processes()

    async_time = asyncio.run(run_async())

    print("\nSummary:")
    print(f"SYNC:     {sync_time:.2f}s")
    print(f"THREAD:   {thread_time:.2f}s")
    print(f"PROCESS:  {process_time:.2f}s")
    print(f"ASYNC:    {async_time:.2f}s")


if __name__ == "__main__":
    main()
