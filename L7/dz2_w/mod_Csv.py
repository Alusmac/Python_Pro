import csv


def save_csv(filename: str, data: list) -> None:
    """Saving file in CSV
    """
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"[OK] CSV saved: {filename}")
    except Exception as e:
        print(f"[Error] Filed to record CSV: {e}")


def load_csv(filename: str) -> list:
    """Reading file  CSV .
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            return list(reader)
    except Exception as e:
        print(f"[Error] Impossible to read CSV: {e}")
        return []
