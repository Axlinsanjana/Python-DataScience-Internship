#TASK 1:
'''Write a while loop that continuously prompts the user to enter numbers until they enter 0.
Store each entered number in a set and print the final set after the loop ends.'''
#OUTPUT:
'''numbers = set()
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    numbers.add(num)
print("Final set of numbers:", numbers)'''


#TASK 2:
'''Create a list where each element is a tuple containing a name and age.
Use a for loop to print names of people who are older than 30.'''
#OUTPUT:
'''people = [("Alice", 25), ("Bob", 35), ("Charlie", 40), ("Diana", 28), ("Ethan", 32)]
for name,age in people:
    if age>30:
        print(name)'''


#TASK 3:
'''Given a list of lists (e.g., [[1, 2], [3, 4], [5, 6]]),
use nested for loops to print each element in the inner lists.'''
#OUTPUT:
# List of lists
'''matrix = [[1, 2], [3, 4], [5, 6]]
# Nested loop to print each element
for inner_list in matrix:
    for element in inner_list:
        print(element)'''

