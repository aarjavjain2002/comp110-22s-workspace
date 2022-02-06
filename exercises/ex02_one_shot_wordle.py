"""One Shot Wordle program."""

__author__ = "730506302"

SECRET: str = "python"
sec_len = len(SECRET)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess = input(f"What is your {sec_len}-letter guess? ")

# Asking for input again when length does not match
while len(guess) != sec_len:
    guess = input(f"That was not {sec_len} letters! Try again: ")

# Correctly guessing the word
if guess == SECRET:
    print(f"{GREEN_BOX}" * sec_len)
    print("Woo! You got it!")

# Correct length but not the right word
i: int = 0
emoji: str = ""

if guess != SECRET:
    while i < sec_len:
        sec_index = SECRET[i]
        if guess[i] == sec_index:
            emoji += f"{GREEN_BOX}"
        else:
            present = False
            alternate = 0
            while present is not True and alternate < sec_len:
                if SECRET[alternate] == guess[i]:
                    present = True
                alternate += 1
            if present is True:
                emoji += f"{YELLOW_BOX}"
            else:
                emoji += f"{WHITE_BOX}"
        i += 1

    print(emoji)
    print("Not quite. Play again soon!")