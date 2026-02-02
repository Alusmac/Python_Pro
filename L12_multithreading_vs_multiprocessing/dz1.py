import threading
import requests

lock = threading.Lock()


def download_file(url: str, filename: str) -> None:
    """Function that downloads multiple files from the network
    """
    with lock:
        print(f"Starting download: {filename}")

    response = requests.get(url)

    with open(filename, "wb") as f:
        f.write(response.content)

    with lock:
        print(f"Done: {filename}")


url1 = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
url2 = "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"
url3 = "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"

t1 = threading.Thread(target=download_file, args=(url1, "file1"))
t2 = threading.Thread(target=download_file, args=(url2, "file2"))
t3 = threading.Thread(target=download_file, args=(url3, "file3"))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All files downloaded")
