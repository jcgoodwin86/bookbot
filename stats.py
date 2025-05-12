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

def sort_on(dict):
    return dict["num"]

def get_report(data):
    report_dict = []

    for letter in data:
        if letter.isalpha():
            report_dict.append({"char": letter, "num": data[letter]})

    report_dict.sort(reverse=True, key=sort_on)

    return report_dict
