#Return values:
#Eg1:
'''def my_function(x):
    c = 5*x
    return c
print(my_function(3))
print(my_function(5))'''

#Eg2:
'''def add(a,b):
    return a+b
result = add(3,4)
print(result)'''

#Eg4:
'''def calculate(a,b):
    return a+b,a-b
add,sub = calculate(10,5)
print('Sum:', add)
print('Difference:',sub)'''

#Eg:
'''def add(a,b):
    return a+b
a = add(2,3)
print('Value of a',a)'''

#Eg:
'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
print('Add =',add(10,2))
print('Sub =',sub(5,2))
print('Mul =',mul(2,2))'''

#Eg(square):
'''def square(n):
    return(n*2)
print(square(4))'''


#RECURSION:
'''def recursion(k):
    if(k>0):
        result = k+recursion(k-1)
        print(result)
    else:
        result = 0
    return result
    print('\n\nRecursion example results')
recursion(6)'''

