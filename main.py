from stats import get_word_count, get_char_count, get_report
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    book_word_count = get_word_count(book)
    char_count = get_char_count(book)
    sorted_data = get_report(char_count)
    print_report(book_path, book_word_count, sorted_data)

def print_report(book_path, book_word_count, sorted_data):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {book_word_count} total words')
    print("--------- Character Count -------")
    for letter in sorted_data:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

main()
