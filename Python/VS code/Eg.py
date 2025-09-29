'''def sum1(a,b):
    add=a+b
    print(add)

def difference(a,b):
    sub=a-b
    print(sub)

def product(a,b):
    pro=a*b
    print(pro)'''

#details = {'name':'vivek', 'age':23}

import modules as m

import datetime
import math
m.sum1(5,4)
m.difference(5,4)


print(datetime.datetime.now())

a=[8,76,6,6]
print(math.sqrt(49))




try:
    a=int(input('Enter the 1st number :'))
    b=int(input('Enter the 2nd number :'))

    c=a/b
    
except ZeroDivisionError:
    print('cant divide bt zero')
except ValueError:
    print('enter valid input')
else:
    print(c)
    print('hii')
finally:
    print('tnks')


import modules as m

import datetime
import math
m.sum1(5,4)
m.difference(5,4)


print(datetime.datetime.now())

a=[8,76,6,6]
print(math.sqrt(49))