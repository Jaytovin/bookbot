def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dictionary = get_character_dict(text)
    sorted_dict = get_dictionary_sorted(dictionary)
    
    print(dictionary)
    print(f"There are {num_words} words in this book")

    for item in sorted_dict:
        if not item["chars"].isalpha():
            continue
        print(f"The '{item["chars"]}' character was found '{item["num"]}' times")
    


def get_num_words(text):
    words= text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def get_dictionary_sorted(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"chars": ch, "num":dictionary[ch]})
    sorted_list.sort(reverse = True, key=sort_on)
    return sorted_list
    
def get_character_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()

