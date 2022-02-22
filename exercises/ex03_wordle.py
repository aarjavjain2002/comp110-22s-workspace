"""Wordle with functions."""

__author__ = "730506302"

SECRET: str = "codes"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(string: str, char: str) -> bool:
    """Checks whether a character is present in a string."""
    assert len(char) == 1
    present = False
    count1 = 0
    while count1 < len(string):
        if char == string[count1]:
            present = True
        count1 += 1
    if present is True:
        return True
    else:
        return False


def emojified(guess: str, SECRET: str) -> str:
    """Returns a string of color emojis that show whether a character is present in the string or not."""
    assert len(guess) == len(SECRET)
    emoji = ""
    count2 = 0
    guess_index = 0
    while count2 < len(SECRET):
        present_emoji = contains_char(SECRET, guess[guess_index])
        if present_emoji is True:
            if guess[guess_index] == SECRET[guess_index]:
                emoji += GREEN_BOX
            else:
                emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        count2 += 1
        guess_index += 1
    return emoji


def input_guess(length: int) -> str:
    """Asks the user to re-enter word if length does not match secret word length."""
    guess: str = input(f"Enter a {length} character word: ")

    while True:
        if len(guess) == length:
            return guess
        else:
            guess = input(f"That wasn't {length} chars! Try again: ")


def main() -> None:
    """The entrypoint of the program and main game loop."""
    count3 = 1
    loop = True
    while count3 <= 6 and loop is True:
        print(f"=== Turn {count3}/6 ===")
    
        guess = input_guess(len(SECRET))

        print(emojified(guess, SECRET))
        
        if guess == SECRET:
            print(f"You won in {count3}/6 turns!")
            loop = False
            
        count3 += 1

    if loop is True:
        print("X/6 - Sorry, try again tomorrow")


if __name__ == "__main__":
    main()