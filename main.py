def main():
    book_path = "books/frankenstein.txt"
    book = get_book_contents(book_path)
    word_count = get_book_words_split(book)
    character_count = count_characters(book)
    sorted_dict = get_character_sort(character_count)
    
    for item in sorted_dict:
        if not item["chars"].isalpha():
            continue
        print(f"The '{item['chars']}' character was found '{item['num']}' times")

def get_book_contents(book_path):
    with open(book_path) as f:
        return f.read()

def get_book_words_split(book):
    book_words_split = book.split()
    return len(book_words_split)

def count_characters(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered in chars: 
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def get_character_sort(character_count):
    character_list = []
    for ch in character_count:
        character_list.append({"chars":ch, "num":character_count[ch]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list




main()