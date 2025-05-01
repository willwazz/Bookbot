from stats import get_num_words
from stats import get_num_letters
from stats import make_dict_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
   


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        book = get_book_text(path)
        num_words = get_num_words(book)
        num_letters = get_num_letters(book)
        new_dict = make_dict_list(num_letters)
        print("=============== BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in new_dict:
            for key, value in item.items():
                print(f"{key}: {value}")
        print("============= END ===============")
    else:
        print("Error: No File path provided")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
