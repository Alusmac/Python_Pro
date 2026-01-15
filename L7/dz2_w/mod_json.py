import json


def save_json(filename: str, data: dict | list) -> None:
    """saving file in JSON format.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"[OK] JSON saved: {filename}")
    except Exception as e:
        print(f"[Error] Cann not save in JSON: {e}")


def load_json(filename: str):
    """Reading file  JSON format.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"[Error] Не вдалося прочитати JSON: {e}")
        return None
