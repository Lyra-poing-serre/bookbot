from pathlib import Path


def get_num_words(book: Path):
    if isinstance(book, Path):
        book = book.read_text()
    return len(book.split())