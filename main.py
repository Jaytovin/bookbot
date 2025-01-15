def main():
    characters = {}
    with open("books/frankenstein.txt") as f:
	    file_contents = f.read()
    print(file_contents)
    word_count = len(file_contents.split())
    print(f"There are {word_count} words in this book")
    lowered_characters = file_contents.lower()
    letter_count = 0
    for i in lowered_characters:
         characters[i]=characters.get(i,0)+1
    print(f"the {characters} character was found ")
        
main()

