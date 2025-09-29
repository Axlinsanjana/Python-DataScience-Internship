#Personal Info Organizer:
'''You are given personal information of a person. You need to store and display the following:

1)Person's name (string), age (int), hobbies (list), and address (dictionary with city and pincode).
2)From the hobbies list, join all hobbies into a single comma-separated string.
3)Create a tuple that combines the name, age, joined hobbies, and address.
4)Print a message using string formatting that displays all this information clearly.'''

name = "Axlin"
age = 21
hobbies = ["reading", "painting", "cycling"]
address = {"city": "Nagecoil", "pincode": 629201}

# Join hobbies
joined_hobbies = ", ".join(hobbies)

# Create tuple
info_tuple = (name, age, joined_hobbies, address)

# Print formatted info
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Hobbies: {joined_hobbies}")
print(f"Address: {address['city']} - {address['pincode']}")
print(f"Combined Info: {info_tuple}")

