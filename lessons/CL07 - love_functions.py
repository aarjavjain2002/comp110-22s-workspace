"""Some examples of tender, loving function definitions"""

def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string"""
    return f"I love you {name}"

# print(love(input("What is your name? ")))

to = input("What is your name? ")
n = int(input("Number of times: "))

def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times"""
    love_note = ""
    i = 0
    while i<n:
        love_note += (love(to) + "\n")
        i += 1
    
    return love_note

print(spread_love(to,n))