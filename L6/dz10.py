import zipfile


class ArhivZip:
    """менеджер контексту для архівування файлів (за допомогою модуля zipfile). Менеджер автоматично
    створює архів, додає файли, а після виходу з блоку with – завершує архівування та закриває архів.
    """

    def __init__(self, archive_name: str, mode='w') -> None:
        self.archive_name = archive_name
        self.mode = mode
        self.archive = None

    def __enter__(self):
        self.archive = zipfile.ZipFile(self.archive_name, self.mode, compression=zipfile.ZIP_DEFLATED)
        return self

    def add(self, file_path, arcname=None):
        self.archive.write(file_path, arcname=arcname or None)

    def __exit__(self, exc_type, exc_value, traceback):
        self.archive.close()
        return False


with ArhivZip("test10.zip") as z:
    z.add("test10.txt")
