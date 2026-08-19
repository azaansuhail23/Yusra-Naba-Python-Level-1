name="Naba"
age=8
country_city="UK : London"
hobbies="Playing Roblox"

""" 
Naba is my sister whose age is 8 her hobbies are Playing Roblox and she lives in UK: London  
"""

# Way 1 : Worst way (using normal print statement)
print(
    name,
    "is my sister whose age is",
    age,
    "her hobbies are ",
    hobbies,
    "and she lives in ",
    country_city
)

# Way 2 : Solution --> String Formatting (f-string)
print(
    f"{name} is my sister whose age is {age} her hobbies are {hobbies} and she lives in {country_city}"
)
