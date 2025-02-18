from string import ascii_lowercase
from os.path import dirname, abspath
from pathlib import Path

ROOT = Path(dirname(abspath(__file__)))


def number_of_word(book: Path):
    if isinstance(book, Path):
        book = book.read_text()

    return len(book.split())


def count_char(book: Path):
    if isinstance(book, Path):
        book = book.read_text()
    book = book.lower()
    return {s: book.count(s) for s in set(book)}


def main():
    books_dir = ROOT / 'books'
    frankenstein = books_dir / 'frankenstein.txt'

    print(f"--- Begin report of {frankenstein.parent.name}/{frankenstein.name} ---")
    print("{}  words found in the document".format(number_of_word(frankenstein)), end="\n\n")
    frankenstein_count = count_char(frankenstein)
    for letter in ascii_lowercase:
        if frankenstein_count[letter]:  # potential un-use letter ?
            print(f"The {repr(letter)} character was found {frankenstein_count[letter]} times")
    print("--- End report ---")


if __name__ == '__main__':
    main()
