def with_backup(filepath: str, callback) -> None:
    """менеджер контексту, який буде створювати резервну копію важливого файлу перед
     його обробкою. Якщо обробка пройде успішно, оригінальний файл замінюється новим.
     У разі помилки резервна копія автоматично відновлюється.
     """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            backup = f.read()
    except FileNotFoundError:
        backup = None

    try:
        callback(filepath)
    except Exception:
        if backup is not None:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(backup)
        raise


def append_line(path):
    with open(path, 'a', encoding='utf-8') as f:
        f.write("\nToday the weather is not like yesterday)")


with_backup("test9.txt", append_line)
