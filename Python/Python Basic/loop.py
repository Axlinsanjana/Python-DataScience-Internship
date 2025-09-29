#LOOPS:
#1)For loop:
#Eg1(greatest amoung 4):
'''a = [7,5,9,4]
total = 0
for i in a:
    total += i
    if i>8:
        print(i,'greatest')
print(total)'''

#Eg2:
'''a = int(input('Enter a number: '))
for i in range(a):
    print(i,end='')'''

#Eg3:
'''fruits = ['Apple','Banana','Cherry']
for x in fruits:
    print(x)'''

#Eg4:
'''for x in 'BANANA':
    print(x)'''

#Eg5:
'''fruits = ['Apple','Banana','Cherry']
for x in range(10):
    print(fruits)'''

#Eg6(to find odd numbers):
'''for i in range(1,20):
    if i%2!=0:
        print(i)'''

#Eg7(sum of elements):
'''a = [7,5,9,4]
sum = 0
for i in a:
    sum +=i
print('Sum of the elements: ',sum)'''

#Eg8:(Dictionary using for loop)
'''details = {'Name':'Axlin','Age':21}
for key,value in details.items():
    print(value)'''

#2)while loop:
#Eg1:
'''i =1
while i<6:
    print(i)
    i = i+1'''

#Eg2:
'''i =1
while i<6:
    print('Hello World')
    i = i+1'''


#else in loops:
#for loop with else:
'''fruits = ['Apple','Banana','Cherry']
for x in fruits:
    print(x)
else:
    print('All the fruits are printed!')'''


#else with break(for loop with break – else does not run):
'''fruits = ['Apple','Banana','Cherry']
for x in fruits:
    if x == 'Banana':
        break    
    print(x)
else:
    print('All the fruits are printed!')'''

#else with continue (Using continue – else still runs):
'''for i in range(6):
    if i == 1:
        continue
    print(i)
else:
    print("Loop finished without break")'''


#While loop with else:
'''x = 0
while x<3:
    print(x)
    x +=1
else:
    print('Counting compled!')'''

#while loop with break - else does not run:
'''i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("While loop completed without break")'''











     
