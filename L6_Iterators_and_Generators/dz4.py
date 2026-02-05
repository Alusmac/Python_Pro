def filter_lines_case_insensitive(file_path, keyword:str) -> None:
    """генератор, який читає великий текстовий файл рядок за рядком (наприклад, лог-файл)
    і повертає лише ті рядки, що містять певне ключове слово
    """
    keyword_lower = keyword.lower()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if keyword_lower in line.lower():
                yield line


input_file = 'test4.txt'
output_file = 'test4_new.txt'
keyword = 'beautiful'

with open(output_file, 'w', encoding='utf-8') as out_f:
    for line in filter_lines_case_insensitive(input_file, keyword):
        out_f.write(line)

print(f"Фільтрація завершена. Результати збережено у {output_file}")
