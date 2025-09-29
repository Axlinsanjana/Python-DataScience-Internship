#lambda function:
#Eg1(Simple addition):
'''x= lambda a:a+10
print(x(5))'''

#Eg2(Simple addition):
'''add = lambda a,b:a+b
print(add(5,3))'''

#Eg3(Square of a number)
'''square = lambda x:x**x
print(square(5))'''

#Eg(using return):
'''def add(a,b):
    return a+b
print(add(5,4))'''

#Eg(Addition):
'''add = lambda a,b:a+b
x = int(input('Enter the 1st number: '))
y = int(input('Enter the 2nd number: '))
print(add(x,y))'''

#Eg(Square):
'''def square(a):
    return a**2
print(square(3))'''

#Eg:
'''square = lambda x:x**2
x =(int(input('Enter a number: ')))
print(square(x))'''

#Eg4:(Using map())
#map():
'''a = [2,4,3,6,8,9,78,5]
b =list(map(lambda a:a%2==0,a))
print(b)'''

#Eg5(Using map() with lambda):
'''nums = [1,2,3,4,5]
squared = list(map(lambda x:x**2,nums))
print(squared)'''

#Eg6(Using map() with a normal function):
'''def square(x):
    return x * x

nums = [1, 2, 3, 4]
result = map(square, nums)
print(list(result)) '''

#Eg7(Adding two lists using map()):
'''a = [1,2,3]
b = [4,5,6]
result = map(lambda x,y:x+y,a,b)
print(list(result))'''

#Eg8(lambda with filter()):Filtering odd numbers
'''nums = [1,3,6,4,9,8,2,12]
even = list(filter(lambda x:x%2==0,nums))
print(even)'''

#Eg10( Using filter() with a normal function):
'''def even(x):
    return x%2==0
nums = [1,2,3,4,5,6]
result= filter(even,nums)
print(list(result))'''

#Eg11(Using filter() with lambda):
'''nums = [10, 15, 20, 25, 30]
result = filter(lambda x: x > 20, nums)
print(list(result))'''

#Eg12(Filtering odd numbers):
'''nums = [1, 2, 3, 4, 5]
odd = filter(lambda x: x % 2 != 0, nums)
print(list(odd)) '''





