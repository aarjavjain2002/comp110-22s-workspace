"""Demonstrations of dictionary capabilities"""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools['Duke'] = 6717
schools["NCSU"] = 26150

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Removing a key-value pair from a dictionary
schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] = schools["NCSU"] + 200

# Print a dictionary literal repersentation
print(schools)


# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()
print(schools)
# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19_400,
    "Dukie": 6717,
    "NCSU": 26150}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")