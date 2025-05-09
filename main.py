from stats import get_word_count, get_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    book_word_count = get_word_count(book)
    char_count = get_char_count(book)

    print(f'{book_word_count} words found in the document')
    print(char_count)

main()
