def error_lines_generator(log_file_path: str) -> None:
    """генератор, який зчитує файл порціями (по рядку) і
     повертає тільки рядки з помилками (код статусу 4XX або 5XX)

    """
    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 9:
                continue
            status_code = parts[8]
            if status_code.startswith('4') or status_code.startswith('5'):
                yield line


def save_errors_to_file(log_file_path: str, output_file_path: str) -> None:
    """Зберігає всі рядки з помилками у новий файл.
    """
    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        for error_line in error_lines_generator(log_file_path):
            out_file.write(error_line)


log_file = 'test7.log'
error_file = 'errors7.log'

save_errors_to_file(log_file, error_file)
print(f"Помилки збережено у {error_file}")
