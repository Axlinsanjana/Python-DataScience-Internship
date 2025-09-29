#While Loop:
#Task 1:
#Keep asking for input until the user types 'exit':
'''while True:
    word = input("Type something (or 'exit' to stop): ")
    if word.lower() == 'exit':
        break'''


#Task 2:
#Print the digits of a number in reverse:               
'''n = int(input("Enter a number: "))
while n > 0: 
    digit = n % 10
    print(digit, end=' ')
    n = n // 10'''


#Task 3:
#Check if a number is a palindrome:
'''n = int(input("Enter a number: "))
original = n
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10
if rev == original:
    print("Palindrome")
else:
    print("Not a palindrome")'''


#Task 4:
#Print Fibonacci series up to n terms:
'''n = int(input("Enter number of terms: "))
a = 0
b =1
count = 0
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1'''


#Task 5:
#Sum of digits of a number:
'''n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    sum_digits = sum_digits + n % 10
    n = n // 10
print("Sum of digits:", sum_digits)'''

           #OR
'''num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print("Sum of digits:", total)'''


#Print numbers from 1 to 10:
'''n=0
while 10>n:
    n = n+1
    print(n)'''
    
    #OR
'''i = 1
while i <= 10:
    print(i)
    i += 1'''

#Sum of first n natural numbers:
'''n = int(input("Enter a number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum:", total)'''


#Print multiplication table of a number:
'''num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1'''


#Factorial of a number:
'''n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)'''


#Print even numbers from 2 to 20
'''i = 2
while i <= 20:
    print(i)
    i += 2'''

#Count digits in a number:
'''num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Total digits:", count)'''







































