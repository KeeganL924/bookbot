def count_words(book_text):
   return len(book_text.split())

def count_char(book_text):
    lower_char = book_text.lower()

    char_count = {}

    for char in lower_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_list(char_count):
    sorted_char_list = []
    for char, num in char_count.items():
        sorted_char_list.append({"char": char, "num": num})
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list
