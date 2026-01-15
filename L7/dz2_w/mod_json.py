import requests
import json


def save_page_json(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = {
            "url": url,
            "content": response.text
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Сторінку збережено у JSON: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Помилка: {e}")
