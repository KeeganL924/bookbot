from stats import count_words, count_char, sort_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    relative_path = "books/frankenstein.txt"
    book_text = get_book_text(relative_path)
    num_words = count_words(book_text)
    book_chars = count_char(book_text)
    sorted_list = sort_list(book_chars)
    print (f"Found {num_words} total words")

    for item in sorted_list:
        if item ["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")



main()
