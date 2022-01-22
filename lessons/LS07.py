"""Example of memory diagram"""

age = int(input("How old are you? "))
year = int(input("What year is it? "))
age_in_2041 = 2041 - year + age
print("In 2041, you will be ", str(age_in_2041), " year old")

age = age + 1
year = year + 1
print("In ", str(year), " you will be ", str(age))