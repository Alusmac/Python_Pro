import pytest


class FileProcessor:
    """class, which has the following methods:
    writes data to a file.
    reads data from a file.
    """
    @staticmethod
    def write_to_file(file_path, data: str) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(data)

    @staticmethod
    def read_from_file(file_path) -> str:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found")


def test_file_write_read(tmpdir) -> None:
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


def test_file_write_read_empty_string(tmpdir) -> None:
    file = tmpdir.join("empty.txt")
    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)
    assert content == ""


def test_file_write_read_large_data(tmpdir) -> None:
    file = tmpdir.join("large.txt")
    large_data = "A" * 10_000
    FileProcessor.write_to_file(file, large_data)
    content = FileProcessor.read_from_file(file)
    assert content == large_data


def test_file_not_found(tmpdir) -> None:
    non_existent_file = tmpdir.join("nofile.txt")
    with pytest.raises(FileNotFoundError):
        FileProcessor.read_from_file(non_existent_file)
