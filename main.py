import sys
from string import ascii_lowercase
from os.path import dirname, abspath
from pathlib import Path

from stats import get_num_words

ROOT = Path(dirname(abspath(__file__)))
args = sys.argv
if not args:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def sort_on(dict):
    return dict[-1]

def count_char(book: Path):
    if isinstance(book, Path):
        book = book.read_text()
    book = book.lower()
    return dict(sorted({s: book.count(s) for s in set(book)}.items(), key=sort_on))


def main():
    book = (ROOT / sys.argv[-1]).absolute()

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book.parent.name}/{book.name} ---")
    print("----------- Word Count ----------\nFound {} total words\n--------- Character Count -------".format(get_num_words(book)))
    book_count = count_char(book)
    for letter, v in book_count.items():
        print(f"{letter}: {v}")
    print("============= END ===============")


if __name__ == '__main__':
    main()
