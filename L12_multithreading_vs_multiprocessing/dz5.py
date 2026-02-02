import threading


def search_in_file(filename: str, keyword: str) -> None:
    """Searches for keyword in file and prints where found
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                if keyword in line:
                    print(f"Found '{keyword}' in {filename} on line {i}")
    except Exception as e:
        print(f"Error reading {filename}: {e}")


files = ["file1.txt", "file2.txt", "file3.txt"]
keyword = "Python"

threading.Thread(target=search_in_file, args=(files[0], keyword)).start()
threading.Thread(target=search_in_file, args=(files[1], keyword)).start()
threading.Thread(target=search_in_file, args=(files[2], keyword)).start()

print("Searching started.")
