import threading
import random

lock = threading.Lock()


def evolve_organism(organism):
    """Simulates one day in the life of an organism
    """

    organism["energy"] += random.randint(1, 5)

    if organism["energy"] > 10:
        organism["energy"] //= 2
        organism["offspring"] += 1

    organism["alive"] = organism["energy"] > 0

    with lock:
        print(f"Organism {organism['id']} updated: {organism}\n")


if __name__ == "__main__":
    population = [
        {"id": i, "energy": random.randint(5, 10), "offspring": 0, "alive": True}
        for i in range(10)
    ]

    print("Initial population:")
    for org in population:
        print(org)
    print("\n--- Evolving population ---\n")

    threads = []
    for org in population:
        t = threading.Thread(target=evolve_organism, args=(org,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nPopulation after one day:")
    for org in population:
        print(org)
