#JUMP STATEMENTS:
#1)Continue Statement:
#Eg(using while loop):
'''i = 0
while i<6:
    i = i+1
    if i == 3:
      continue
    print(i)'''

#Eg(using for loop):
'''for i in range(6):
    if i == 2:
        continue
    print(i)'''

#Eg2:
'''fruits = ['Apple','Banana','Cherry']
for a in fruits:    
    if a == 'Banana':
        continue
    print(a)'''

#2)Break Statement:
#Eg1:
'''fruits = ['Apple','Banana','Cherry','Papaya','Orange']
for x in fruits:
    print(x)
    if x == 'Banana':
        break'''

#Eg2:
'''fruits = ['Apple','Banana','Cherry']
for a in fruits:    
    if a == 'Banana':
        break
    print(a)'''
