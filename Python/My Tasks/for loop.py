#Loop Tasks:
#for loop: 
#Task 1:
#Print numbers from 1 to 10:
'''for i in range(1,11):
    print(i)'''


#Task 2:
#Print even numbers between 1 and 50:
'''for i in range(2,51,2):
    print(i)'''

       #OR
'''for i in range(1,51):
    if i%2==0:
        print(i)'''


#Task 3:
#Calculate the sum of numbers from 1 to n (user input):
'''n = int(input("Enter a number: "))
total = 0
for i in range(1,n+1):
    total =total+i
print("Sum:", total)'''

          #OR
'''n = int(input("Enter a number: "))  
total = n * (n + 1) // 2
print("Sum:", total)'''

          #OR
'''n = int(input("Enter a number: "))
total = sum(range(1, n + 1))
print("Sum:", total)'''


#Task 4:
#Print the multiplication table of a number (user input):
'''n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")'''


#Task 5:
#Find the factorial of a number:
'''n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print("Factorial:", fact)'''


#Task 6:
#Count how many vowels are in a given string:
'''text = input("Enter a string: ")
count = 0
for char in text:
    if char.lower() in 'aeiou':
        count = count + 1
print("Number of vowels:", count)'''

        #OR
'''text = "Hello World"
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Number of vowels:", count)'''


#Task 7:
#Print all elements of a list using a loop:
'''items = [10, 20, 30, 40]
for i in items:
    print(i)'''


#Task 8:
#Reverse a string using a loop:
'''text = input("Enter a string: ")           
reversed_str = ''                              
for char in text:                               
    reversed_str = char + reversed_str          
print("Reversed:", reversed_str)'''


#Task 9:
#Find the largest number in a list using a loop:
'''numbers = [5, 3, 9, 2, 8]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Largest number:", max_num)'''


#Task 10:
#Calculate the average of numbers in a list:
'''num = [10, 20, 30, 40, 50]
total = sum(num)
average = total / len(num)
print("Average:", average)'''

       #OR
'''numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total = total + num
average = total / len(numbers)
print("Average:", average)'''


#Task 11:
#Print the square of each number from 1 to 10:
'''for i in range(1,11):
    print(i**2)'''


#Task 12:
#Print each character in a string:
'''name = input('Enter a name:')
for i in name:
    print(i)'''


#Task 13:
#Print elements of a list with their index
'''fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")'''

       #OR
'''fruits = ['apple', 'banana', 'cherry']
for i in enumerate(fruits):
    print(i)'''

       #OR
'''fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)'''


#Task 14:
#Find the sum of digits of a number:
'''num = int(input("Enter a number: "))
sum_digits = 0
for digit in str(num):
    sum_digits += int(digit)
print("Sum of digits:", sum_digits)'''


#Task 15:
#Print a right-angle triangle pattern of stars:
'''n= int(input("Enter a number: "))
for i in range(1,n+1):
    print('*'*i)'''


#Task 16:
#Print pattern:
'''n = 4
for i in range(1, n + 1):
    print("*" * i)'''


#Task 17:
#Find duplicate elements in a list:
'''items = [1, 2, 2, 3, 4, 4, 5]
duplicates = []
for i in items:
    if items.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print("Duplicates:", duplicates)'''


#Task 18:
#Print only unique characters from a string:
'''text = input("Enter a string: ")
for char in text:
    if text.count(char) == 1:
        print(char, end=' ')'''


#Task 19:
#Count how many times each letter appears in a word
''''word = input("Enter a word: ")
for char in set(word):  # Using set to avoid repeats
    count = word.count(char)
    print(f"{char}: {count}")'''







