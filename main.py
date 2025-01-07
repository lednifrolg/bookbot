def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_character_count(text)
    print(f"{num_words} words found in the document")
    for char in char_count:
        print(f"The '{char['char']}' character was found {char['count']} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["count"]

def get_character_count(text):
    count_dictionary = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in count_dictionary:
            count_dictionary[char] += 1
        else:
            count_dictionary[char] = 1
    count_array = []
    for name in count_dictionary:
        if name >= 'a' and name <= 'z':
            count_array.append({"char": name, "count": count_dictionary[name]})
    count_array.sort(reverse=True, key=sort_on)
    return count_array

main()
