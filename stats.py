def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    char_dict = {}

    for char in book:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1

    return char_dict
