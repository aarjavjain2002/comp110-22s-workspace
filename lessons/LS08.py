"""An example of if else conditional statements"""

SECRET: int = 3 # SECRET in all caps is recognized by Python.
# This all caps represents that we don't intend to change this value later in this program

print("I'm thinking of a number between 1 and 5.")
guess: int = int(input("What is your guess? "))
# Here we need to specify int() outside the input since it is a STRING by default

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day!")

else:
    print("Sorry, you guessed incorrectly")
    print("Try running the program again")
    
    if guess > SECRET:
        print("Your guess was too high")
    else:
        print("Your guess was too low")

print("Game Over")