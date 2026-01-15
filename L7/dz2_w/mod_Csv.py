import requests
import csv


def save_page_csv(url, filename: str) -> None:
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["content"])
            writer.writerow([response.text])

        print(f"Сторінку збережено у CSV: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Помилка: {e}")
