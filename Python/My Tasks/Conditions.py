#Python Conditions:
#TASK 1-Positive, Negative, or Zero:
'''Take a number and check whether it is positive, negative, or zero using conditions.'''
#OUTPUT:
'''num = int(input('Enter a number: '))
if num>0:
    print(num,'is positive')
elif num<0:
    print(num,'is negative')
else:
    print(num,'is zero')'''


#TASK 2-Even or Odd:
'''Take a number and check whether it is even or odd using `if`.'''
#OUTPUT:
'''num = int(input('Enter a number: '))
if num%2==0:
    print(num,'is even')
else:
    print(num,'is odd')'''


#TASK 3-Largest of Three Numbers:
'''Compare three numbers and find the largest one using `if-elif-else`.'''
#OUTPUT:
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>=b and a>=c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)'''

    
#TASK 4-Check Vowel or Consonant:
'''Take a letter input and check if it is a vowel or consonant.'''
#OUTPUT:
'''x = input('Enter a single letter:').lower()
if x in 'aeiou':
    print(x,'is vowel')
elif x.isalpha():
    print(x,'is consonent')
else:
    print(x,'is not an alphabet')'''


#TASK 5-Grade Checker:
'''*Take marks (0–100) and print the grade:
*`90+`: A, `80–89`: B, `70–79`: C, `60–69`: D, below `60`: Fail.'''
#OUTPUT:
'''x = int(input("Enter marks (0-100): "))
if x>=90:
    print('Grade A')
elif x>=80:
    print('Grade  B')
elif x>=70:
    print('Grade C')
elif x>=60:
    print('Grade D')
else:
    print('Fail')'''


#TASK 6-Leap Year Checker:
'''*Take a year as input and check if it's a leap year:
*Divisible by 4, not divisible by 100 unless divisible by 400.'''
#OUTPUT:
'''year = int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year")'''

    
#TASK 7-Check Divisibility:
'''Take a number and check if it is divisible by 3 and 5 both, only 3, only 5, or neither.'''
#OUTPUT:
'''num = int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print("Divisible by both 3 and 5")
elif num%3==0:
    print("Divisible by 3")
elif num%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")'''


#TASK 8-Triangle Validity:
'''Given three sides, use conditions to check if a triangle is possible (`a + b > c`, etc.).'''
#OUTPUT:
'''a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
if a+b>c and b+c>a and c+a>b:
    print("Valid triangle")
else:
    print("Invalid triangle")'''

    
#TASK 9-Check Alphabet Case:
'''Take a character input and check if it is uppercase, lowercase, or not a letter.'''
#OUTPUT:
'''ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif not ch.isalpha():
    print("Not an alphabet")'''

    
#TASK 10-Check if Number is in Range:
'''Take a number and check whether it's in the range 1–100.'''
#OUTPUT:
'''num = int(input("Enter a number: "))
if num>=1 and num<=100:
    print("Number is in the range 1 to 100")
else:
    print("Out of range")'''


#TASK 11:
#string palindrome:
'''s = input("Enter a string: ")
s = s.lower().replace(" ", "")
if s == s[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")'''





















