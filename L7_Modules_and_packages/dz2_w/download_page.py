import requests


def download_page(url: str, filename: str) -> None:
    """loads the page from the specified URL and saves its content to a text file.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Page successfully saved to file: {filename}")

    except requests.exceptions.Timeout:
        print("Error: Response timeout.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to establish a connection to the server.")

    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
