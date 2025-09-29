#Nested if:
#Task 1: Age and Citizenship Eligibility
'''Check if a person is eligible to vote (age ≥ 18) and whether they are an Indian citizen.'''
#OUTPUT:
'''age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")
if age >= 18:
    if citizen.lower() == "yes":
        print("Eligible to vote.")
    else:
        print("Not eligible to vote (citizenship issue).")
else:
    print("Not eligible to vote (age issue).")'''


#Task 2: Number is Positive/Negative and Even/Odd
'''Determine if a number is positive or negative, and whether it's even or odd.'''
#OUTPUT:
'''num = int(input("Enter a number: "))
if num>=0:
    print("Positive number")
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")'''

         #OR

'''num = int(input("Enter a number: "))

if num >= 0:
    print("Positive number")
else:
    print("Negative number")
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")'''


#Task 3: Grade Category with Distinction
'''Input marks, categorize grade, and check for distinction (marks ≥ 85).'''
#OUTPUT:
'''marks = int(input("Enter your marks: "))
if marks >= 50:
    print("You passed.")
    if marks >= 85:
        print("Distinction!")
    elif marks >= 75:
        print("First class.")
    elif marks >= 60:
        print("Second class.")
    else:
        print("Third class.")
else:
    print("You failed.")'''


#Task 4: Login System with Role-Based Access
'''Check if the username and password match, then give access based on role.'''
#OUTPUT:
'''username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "admin123":
        print("Welcome Admin!")
    else:
        print("Incorrect password.")
elif username == "student":
    if password == "stud123":
        print("Welcome Student!")
    else:
        print("Incorrect password.")
else:
    print("Unknown user.")'''


#Task 5: Leap Year and Century Check
'''Check if a year is a leap year and if it’s a century year.'''
#OUTPUT:
'''year = int(input("Enter a year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year and century year")
        else:
            print("Century year but not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")'''









