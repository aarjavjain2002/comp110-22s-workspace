"""Wordle with functions"""

__author__ = "730506302"

SECRET: str = "codes"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def main() -> None:
    """The entrypoint of the program and main game loop"""

    count3 = 1
    loop = True
    while count3 <= 6 and loop == True:
        print(f"=== Turn {count3}/6 ===")

        guess = input(f"Enter a {len(SECRET)} character word: ")
    
        guess = input_guess(guess)

        print(emojified(guess, SECRET))
        
        if guess == SECRET:
            print(f"You won in {count3}/6 turns!")
            loop = False
            

        count3 += 1
    if loop == True:
        print("X/6 - Sorry, try again tomorrow")

    


def contains_char(string: str, char: str) -> bool:
    """Checks whether a character is present in a string"""
    assert len(char) == 1
    present = False
    count1 = 0
    while count1 < len(string):
        if char == string[count1]:
            present = True
        count1 += 1
    if present == True:
        return True
    else:
        return False
            
def emojified(guess: str, SECRET: str) -> str:
    """Returns a string of color emojis that show whether a character is present in the string or not"""
    assert len(guess) == len(SECRET)
    emoji = ""
    count2 = 0
    guess_index = 0
    while count2 < len(SECRET):
        present_emoji = contains_char(SECRET, guess[guess_index])
        if present_emoji == True:
            if guess[guess_index] == SECRET[guess_index]:
                emoji += GREEN_BOX
            else:
                emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        count2 += 1
        guess_index += 1
    return emoji

def input_guess(guess: str):
    """Asks the user to re-enter word if length does not match secret word length"""
    while len(guess) != len(SECRET):
        guess = input(f"That was not {len(SECRET)} letters! Try again: ")
    return guess
    
if __name__ == "__main__":
    main()