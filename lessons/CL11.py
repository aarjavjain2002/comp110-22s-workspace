"""List diagram example."""

a: list[str] = ["one"]
b: list[str] = a
a.append("two")

print(b[1]) 

def dup(xs: list[int]) -> None:
    """Duplicate a list's values."""
    start_len: int = len(xs)
    i: int = 0
    while i < start_len:
        xs.append(xs[i])
        i += 1


nums: list[int] = [10,20]
dup(nums)
print(nums)


def odds(min: int, max: int) -> list[int]:
    """Constructs list of odds, inclusive."""
    xs: list[int] = list()
    i: int = (min // 2) * 2 + 1
    while i <= max:
        xs.append(i)
        i += 2
    return xs


ys: list[int] = odds(3,6)
print(ys)

"""Example of writing a function to search a list."""


def contains(needle: str, haystack: list[str]) -> bool:
    """Test if needle is found in the haystack."""
    for item in haystack:
        if item == needle:
            return True
    return False


print(contains("aarjav", ["aarjav", "andy", "ridhi"]))

def main() -> None:
    guess: str = input("What is the code word?")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you in the secret club")
    else:
        print("Go back to Davis")