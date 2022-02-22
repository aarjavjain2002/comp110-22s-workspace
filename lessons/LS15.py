"""Examples of using lists in a simple 'game'."""

from random import randint

rolls: list[int] = list()
rolls.append(randint(1,6))
rolls.append(randint(1,6))
print(rolls)

# Access an individual item
print(rolls[0])
print(rolls[1])

# Access the length of a list (number of times)
print(len(rolls))

# Access the last item in a list
print(rolls[len(rolls) - 1])

# Running a loop until we get a certain number (3)
while len(rolls) == 0 and rolls[len(rolls) -1 ] != 3:
    rolls.append(randint(1,6))

# Removing an item using "pop"
rolls.pop(len(rolls) - 1)

# Reassigning items in a list
rolls[0] = 2

