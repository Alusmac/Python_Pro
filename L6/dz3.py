import os
import csv
from PIL import Image


def collect_image_stats_simple(folder_path: str, output_csv: str) -> None:
    """ітератор, який по черзі відкриває кожне зображення,
     витягує з нього метадані (розмір, формат тощо) і зберігає ці дані у файл CSV.
     """
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Заголовки
        writer.writerow(['filename', 'format', 'width', 'height', 'mode'])

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    writer.writerow([filename, img.format, img.width, img.height, img.mode])
            except Exception as e:
                print(f"Не вдалося обробити {filename}: {e}")

# collect_image_stats_simple("path_to_images", "output.csv")
