import json


class JSONConfig:
    """власний контекстний менеджер для роботи з файлом конфігурацій
     Менеджер має автоматично зчитувати конфігурацію при вході в контекст
     і записувати зміни в файл після завершення роботи
     """

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.config = {}

    def __enter__(self):

        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.config = {}
        return self.config

    def __exit__(self, exc_type, exc_value, traceback):

        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

        return False


with JSONConfig("test8.json") as cfg:
    cfg["username"] = "emma"
    cfg["theme"] = "white"
    cfg["password"] = "123456"
