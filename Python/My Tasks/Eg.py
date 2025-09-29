#Task 1:
#Print numbers from 1 to 10 (Using for loop):
'''for i in range(1,11):
    print(i)'''


#Task 2:
#Print numbers from 1 to 10 using while loop:
'''i = 1
while i<11:
    print(i)
    i = i+1'''


#Task 3:
#Stop the loop when number is 5 (Using break)
'''n = 0
while n<11:
    n = n+1
    if n==5:        
        break    
    print(n)'''

     #OR
'''for i in range(1,11):
    if i==5:
        break
    print(i)'''


#Task 4:
#Skip even numbers (Using continue):
'''for i in range(1,11):
    if i%2==0:
        continue
    print(i)'''

     #OR
'''n = 0
while n<10:
    n = n+1
    if n%2==0:
        continue
    print(n)'''


#Task 5:
#Count digits in a number (Using while):
'''n = int(input('Enter a number: '))
i = 0
while n>0:
    n = n//10
    i = i+1
print(i)'''

    #OR
'''num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Total digits:", count)'''


#Task 6:
#Print the first 5 multiples of a number, stop if multiple is greater than 20:
'''n = int(input('Enter a number: '))
for i in range(1,6):
    if i*n>20:
        break
    print(f'{i} x {n} = {i*n}')'''

      #OR
'''n = int(input("Enter a number: "))
for i in range(1, 6):
    result = n * i
    if result > 20:
        break
    print(result)'''

    

#Task 7:
#Continue only if number is not divisible by 3:
'''n = int(input('Enter a number: '))
for i in range(0,n+1):
    if i%3==0:
        continue
    print(i)'''

      #OR
'''for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)'''


#Task 8:
#Find sum of digits, skip 0 digits (using continue):
'''num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    if digit == 0:
        num //= 10
        continue
    total += digit
    num //= 10
print("Sum of non-zero digits:", total)'''


#Task 9:
#Infinite loop with break to stop on user input:
'''while True:
    word = input("Enter a word (or 'stop' to quit): ")
    if word == "stop":
        break
    print("You entered:", word)'''










 
