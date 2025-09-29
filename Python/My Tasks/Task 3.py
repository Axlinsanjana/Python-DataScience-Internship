#TASK 1: String and List Formatting
''''You are given:
name = "Alice"
hobbies = ["Reading", "Cycling", "Gaming"]
Your task:
Combine all hobbies into a single string using .join()
Create a final sentence: "Alice likes Reading, Cycling, Gaming."'''
#OUTPUT:
'''name = "Alice"
hobbies = ["Reading", "Cycling", "Gaming"]
joined = ', '.join(hobbies)
print('Alice likes',joined)
print(f"{name} likes {joined}")
print(name, "likes", joined)'''


#TASK 2: Tuple and Arithmetic Operators
'''You are given:
marks = (78, 85, 90)
Your task:
Calculate the total and average marks using arithmetic operators.'''
#OUTPUT 1:
'''marks = (78, 85, 90)
total = sum(marks)
average = total/len(marks)
print('Average:',average)
print('Total:',total)'''

#OUTPUT 2:
'''marks = (78, 85, 90)
total = marks[0] + marks[1] + marks[2]
average = total / 3
print("Total Marks:", total)
print("Average Marks:", average)'''



#TASK 3: Set Operations
'''You are given:
subjects_A = {"Math", "English", "Biology"}
subjects_B = {"English", "Physics", "Biology"}
Your task:
Find common subjects
Find subjects only in A
Find all unique subjects'''
#OUTPUT:
'''subjects_A = {"Math", "English", "Biology"}
subjects_B = {"English", "Physics", "Biology"}
common = subjects_A & subjects_B
only_in_A = subjects_A - subjects_B
all_unique = subjects_A | subjects_B
print("Common Subjects:", common)
print("Subjects only in A:", only_in_A)
print("All Unique Subjects:", all_unique)'''


#TASK 4: Dictionary Value Manipulation
'''You are given:
prices = {"apple": 30, "banana": 10, "mango": 50}
quantities = {"apple": 2, "banana": 5, "mango": 3}
Your task:
Multiply each item's price with quantity
Create a new dictionary total_cost like: {"apple": 60, "banana": 50, "mango": 150}'''
#OUTPUT:
'''prices = {"apple": 30, "banana": 10, "mango": 50}
quantities = {"apple": 2, "banana": 5, "mango": 3}
total_cost = {
    "apple": prices["apple"] * quantities["apple"],
    "banana": prices["banana"] * quantities["banana"],
    "mango": prices["mango"] * quantities["mango"]
}
print("Total Cost:", total_cost)'''



#TASK 5: Mixed Data Types Display
'''You are given:
person = {
    "name": "David",
    "age": 28,
    "hobbies": ["Guitar", "Chess"],
    "address": ("New York", 10001)
}
Your task:
Print a formatted message like:
"David, aged 28, lives in New York - 10001 and likes Guitar and Chess."'''
#OUTPUT:
'''person = {
    "name": "David",
    "age": 28,
    "hobbies": ["Guitar", "Chess"],
    "address": ("New York", 10001)
}

info = f"{person['name']}, aged {person['age']}, lives in {person['address'][0]} - {person['address'][1]}and likes {person['hobbies'][0]} and {person['hobbies'][1]}."
print(info)'''


#TASK 6: List Arithmetic
'''You are given:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
Your task:
Create a combined list using + operator
Multiply list1 by 2 using * operator'''
#OUTPUT:
'''list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
repeated = list1 * 2
print("Combined List:", combined)
print("Repeated List:", repeated)'''



#TASK 7: Dictionary Key Access
'''You are given:
student = {"name": "Sita", "score": 88, "grade": "A"}
Your task:
Extract values and print as:
"Sita got 88 marks and secured grade A."'''
#OUTPUT:
'''student = {"name": "Sita", "score": 88, "grade": "A"}
message = f"{student['name']} got {student['score']} marks and secured grade {student['grade']}."
print(message)'''

'''name = "Sanjana"
age = 21
print(f"Next year, I will be {age + 1} years old.")'''




















