def count_letters(words:list):
    letters = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for word in words:
        for letter in word:
            if letter.isalpha():
                letters[letter.lower()] += 1
    return letters

def create_report(total_words, letters_count):
    print("--- Begin report of book/frankenstein.txt --")
    print(f"{total_words} words found in the document\n")
    for letter in letters_count.keys():
        print(f"The '{letter}' was found {letters_count[letter]} times")
    print("--- End report ---")

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = len(words)
        letters_count = count_letters(words)
    create_report(total_words, letters_count)

if __name__ == "__main__":
    main()