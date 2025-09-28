from stats import count_words, count_char, sort_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    relative_path = sys.argv[1]
    book_text = get_book_text(relative_path)
    num_words = count_words(book_text)
    book_chars = count_char(book_text)
    sorted_list = sort_list(book_chars)
    print ("============ BOOKBOT ============")
    print ("Analyzing book")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        if item ['char'].isalpha():
            print(f"{item['char']}: {item['num']}")



main()
