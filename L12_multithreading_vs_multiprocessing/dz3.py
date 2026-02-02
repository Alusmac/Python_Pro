from multiprocessing import Process, Queue
import random


def partial_sum(numbers, queue):
    """counting the sum of numbers in a large array
    """
    result = sum(numbers)
    queue.put(result)


if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(10_000_000)]

    part_size = len(numbers) // 4
    parts = [
        numbers[0:part_size],
        numbers[part_size:2 * part_size],
        numbers[2 * part_size:3 * part_size],
        numbers[3 * part_size:]
    ]

    queue = Queue()
    processes = []

    for par in parts:
        p = Process(target=partial_sum, args=(par, queue))
        processes.append(p)
        p.start()

    total_sum = 0
    for _ in processes:
        total_sum += queue.get()

    for p in processes:
        p.join()

    print("Total amount:", total_sum)
