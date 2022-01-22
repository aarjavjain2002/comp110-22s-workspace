"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730506302"

word: str = input("Enter a 5-character word: ")

if len(word) == 5:

    char: str = input("Enter a single character: ")

    if len(char) == 1:

        print("Searching for", char, "in", word)

        char_count = 0

        if char == word[0]:
            print(char, "found at index", 0)
            char_count = char_count + 1

        if char == word[1]:
            print(char, "found at index", 1)
            char_count = char_count + 1

        if char == word[2]:
            print(char, "found at index", 2)
            char_count = char_count + 1

        if char == word[3]:
            print(char, "found at index", 3)
            char_count = char_count + 1

        if char == word[4]:
            print(char, "found at index", 4)
            char_count = char_count + 1

        if char_count == 0:
            print("No instances of", char, "found in", word)
        else:
            if char_count == 1:
                print("1 instance of", char, "found in", word)
            else:
                print(char_count, "instances of", char, "found in", word)
    else:
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()