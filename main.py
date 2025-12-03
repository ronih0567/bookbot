import sys
from stats import book_word_count
from stats import character_stats
from stats import sort_character_stats

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
   
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    # Old hardcoded path:
    # book_text = get_book_text("books/frankenstein.txt")
    num_words = book_word_count(book_text)
    book_char_dict = {}
    book_char_dict = character_stats(book_text)
    # print(book_char_dict)
    sorted_char_stats = sort_character_stats(book_char_dict)
    # print(sorted_char_stats)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    for char, count in sorted_char_stats:
        if char.isalpha():
            print(f"{char}: {count}")
    
main()