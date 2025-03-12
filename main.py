from stats import get_num_words, get_chars_dict, sorting_dict
import sys



def main(book_path):

    #book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    # print(f"{num_words} words found in the document")
    chars_list = sorting_dict(chars_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in chars_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f'{char}: {count}')
    print("============= END ===============")        
    



def get_book_text(path):
    with open(path) as f:
        return f.read()


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

main(book_path)
