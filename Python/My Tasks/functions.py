#Addition:
'''def add():
    print('Addition:')
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = a+b
    print('Total:',c)
add()'''


#Subtraction:
'''def sub():
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))    
    print(a-b)
sub()'''

#Eg 1:
'''def age(b):
    print(b)

a = 10
age(a)'''

    #OR
'''def age(a):
    print('Age:',a)
age(10)'''

     #OR
'''def age(a):
    print('Age:',a)
a = 10
age(a)'''

#Eg 2:
'''def printrange():
    for i in range(1,11):
        print(i)
printrange()'''

    #OR
'''def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
        
a = 1
b =11
printrange(a,b)'''

        #OR
'''def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
        
a = int(input('Enter a:'))
b = int(input('Enter b:'))
printrange(a,b)'''


#Odd or Even:
'''def printrange(a):
    if a%2==0:
        print('Even')
    else:
        print('Odd')
        
a = int(input('Enter a number:'))
printrange(a)'''


#Find Factorial of a Number:
'''def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)

n = int(input('Enter a number:'))
factorial(n)'''

     #OR
'''def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

n = int(input('Enter a number:'))
x = factorial(n)
print(x)'''


#Find Maximum of Three Numbers:
'''def maximum(a,b,c):
    return max(a,b,c)
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
x = maximum(a,b,c)
print('Maximum number:',x)'''

         #OR
'''def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
x = maximum(a,b,c)
print('Maximum number:',x)'''


#Count Vowels in a String:
'''def vowels(n):
    count = 0
    for i in n:
        if i.lower() in 'aeiou':
            count = count +1
    return count
n = input('Enter a word:')
print(vowels(n))'''

      #OR
'''def vowels(n):
    count = 0
    for i in n:
        if i.lower() in 'aeiou':
            count = count +1
    print(count)
    
n = input('Enter a word:')
vowels(n)'''

       #OR
'''def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print("Vowel count:", count_vowels("Hello World"))'''



#Reverse a String:
'''def rev(n):
    x = ''
    for i in n:
        x = i + x
    print(x)  
n = input('Enter a string:')
rev(n)'''

       #OR
'''def rev(n):
    x = ''
    for i in n:
        x = i + x
    return x  
n = input('Enter a string:')
print(rev(n))'''


#Generate Fibonacci Series (n terms):
#Using for loop:
'''def fibo(n):
    a = 0
    b = 1
    for i in range(1,n+1):
        print(a, end =',')
        a,b = b,a+b
n = int(input('Enter a number:'))
fibo(n)'''

      #OR
'''def fibo(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter a number: "))
x = fibo(n)
print(x)'''

#Using while loop:
'''def fibo(n):
    a = 0
    b = 1
    count = 0
    while count<n:
        print(a,end =',')
        a,b = b,a+b
        count = count+1
n = int(input('Enter a number:'))    
fibo(n)'''

         #OR
'''def fibo(n):
    a, b = 0, 1
    series = []
    count = 0
    while count < n:
        series.append(a)
        a, b = b, a + b
        count += 1
    return series

n = int(input("Enter a number: "))
x = fibo(n)
print(x)'''


#Check Palindrome(int):
'''def fun(n):
    pali = n
    count = 0
    while n>0:
        count = count * 10 +(n%10)
        n = n//10
    if count == pali:
        print('palindrome')
    else:
        print('not')
n = int(input('Enter a number:'))
fun(n)'''


'''def fun(n):
    pali = n
    count = 0
    while n > 0:
        count = count * 10 + (n % 10)
        n = n // 10
    return count == pali  # returns True or False

n = int(input("Enter a number: "))
if fun(n):
    print("palindrome")
else:
    print("not palindrome")'''


#check plaindrome(string):
'''def pali(n):
    n = n.lower().replace(" ","")
    if n == n[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
n = input('Enter a string:')
pali(n)'''

         #OR
'''def pali(n):
    n = n.lower().replace(" ", "")
    if n == n[::-1]:
        return True   
    else:
        return False  
n = input("Enter a string: ")
if pali(n):
    print("It is a palindrome")
else:
    print("It is not a palindrome")'''




