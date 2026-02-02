from multiprocessing import Pool
import math


def partial_factorial(range_tuple: tuple) -> int:
    """Calculates the product of numbers from start to end included
    """
    start, end = range_tuple
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


if __name__ == "__main__":
    N = 30
    num_processes = 4

    part_size = N // num_processes
    ranges = []
    for i in range(num_processes):
        start = i * part_size + 1
        end = (i + 1) * part_size if i < num_processes - 1 else N
        ranges.append((start, end))

    with Pool(processes=num_processes) as pool:
        partial_results = pool.map(partial_factorial, ranges)

    factorial_result = 1
    for pr in partial_results:
        factorial_result *= pr

    print(f"{N}! = {factorial_result}")
    print("Check with math.factorial:", math.factorial(N))
