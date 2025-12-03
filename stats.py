def book_word_count(book_text):
    book_words = len(book_text.split())
    return book_words    

def character_stats(book_text):
    char_dict = {}
    book_chars = book_text.lower()
    for char in book_chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
    
def sort_character_stats(book_char_dict):
    # Convert dict items to a list so we can use the list.sort() method
    items = list(book_char_dict.items())
    # Sort in-place by the count (value) in descending order
    items.sort(key=lambda kv: kv[1], reverse=True)
    
    return items