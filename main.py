def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    letters = []
    for char in char_count:
        if char.isalpha() == True:
            letter = {
                "letter": char,
                "num": char_count[char]
            }
            letters.append(letter)

    letters.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    for letter in letters:
        print(f"The '{letter['letter']}' character was found {letter['num']} times")
    
    
def count_words(string):
    words = string.split()
    return len(words)
    #print(len(words))

def count_chars(text):

    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]


main()