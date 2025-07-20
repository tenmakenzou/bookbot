import sys
from stats import *


def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]  

    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: File not found -> {filepath}")
        sys.exit(1)


    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")


    char_freq = count_characters(book_text)


    if ' ' in char_freq:
        del char_freq[' ']


    sorted_chars = sort_character_counts(char_freq)

  
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()

