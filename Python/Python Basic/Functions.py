#Functions:
#Eg:
'''def hi(name, age): #parameters
    print('My name is',name)
    print('My age is',age)

hi('Axlin',21) #Arguments'''

#Eg:
'''def add(a,b):
    c = a+b
    print(c)
add(1,3)
add(1,4)'''
  
#Eg1:
'''def my_function():
    print("Hello")
my_function()'''

#Eg2:
'''a = [2,4,3]
def num(a):
    b = []
    for i in a:
        b.append(i*i)
    print(b)
num(a)'''


#Arguments:
#Eg1:
'''def my_function(name):
    print('My Name is',name)
my_function('Emil')
my_function('Tobias')'''

#Eg2:
'''def my_function(fname, sname):
    print('My Name is',fname,sname)
my_function('Emil','Tobias')'''

#Example:
'''def hi(name,age):#Parameters
    print('My Name is',name)
    print('My age is',age)
hi('Axlin',21)''' #Arguments

#Eg3(Positional arguments):
'''def add(a,b):
    c = a+b
    print(c)
add(1,3)

def sub(x,y):
    z = x-y
    print(z)
sub(13,3)'''

#Eg4(Keyword arguments):
'''def greet(name,msg):
    print(f'Hello {name},{msg}')
greet(name = 'Sanjana',msg='Gud mrng' )'''

#Eg:
'''def hi(name,age):
    print(f'My name is {name} and my age is {age}')
hi('Axlin',21)'''

#Eg6(Keyword arguments):
'''def my_function(child3,child2,child1):
    print('The youngest child is ' + child3)
my_function(child1 = 'Emil', child2 = 'Tobias', child3 = 'Linus')'''


#Eg5(Keyword arguments):
'''def hi(name,age):
    print('My name is',name,'My age is',age)    
hi('sanjana',21)'''

#Eg(Keyword arguments):
'''def my_function(child3,child2,child1):
    print('The youngest child is '+child3)
my_function(child1='Emil',child2='Tobias',child3='Linus')'''

            #(or)

'''def hi(name,age):    
    print(f'My name is {name} My age is {age}')
hi('sanjana',21)'''

#Eg6(Default parameters):
'''def greet(name='User'):
    print('Hello',name)
greet()
greet('Sanjana')'''


#Arbitrary Arguments:(*args)
#Eg1:
'''def my_function(*kids):
    print('The youngest kid is', kids[0])
    print('The youngest kid is', kids[2])
    print('The youngest kid is', kids[1])
my_function('Emil','Tobias','Linus')'''

#Eg2:
'''def ax(*name):
    print('The youngest child is',name[1])
ax('emil','tobias')'''

#Eg3:
'''def fun(*kids):
    print('The youngest child is',kids[2])
fun('Emil','axl','san')'''

#Eg4:
'''def add_numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_numbers(1, 2, 3))       
print(add_numbers(5, 10, 15, 20))'''


#Arbitrary keyword arguments(**kwargs):
#Eg1:
'''def profile(**info):
    print(info)
profile(name="Sanjana", age=21)'''

#Eg2:
'''def create_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
create_profile(name="Sanjana", age=21, city="Chennai")'''

#Eg3:
'''def print_info(**info):
    for key,value in info.items():
        print(f'{key}:{value}')
print_info(name = 'Sanjana', age=21, Course='Python')'''

#Eg:
'''def my_function(**kids):
    print('The youngest child1 is', kids['kid1'])
    print('The youngest child2 is', kids['kid2'])
    print('The youngest child3 is',)
my_function(kid3 = 'Emil', kid2 ='Tobias', kid1 ='linus')'''

#Eg:
'''def my_details(**details):
    print('My name is',details['name'])
    print('My age is', details['age'])
    print('My place is', details['place'])
my_details(name='Axlin', age = 21, place = 'Nagercoil')'''

#Eg:
'''def details(**childs):
    print('The youngest child is', childs['child2'])
details(child1 = 'Emil',child2 = 'Tobias', child3 = 'Linus')'''

#Example(*args, **kwargs):
'''def Show_Data(*args,**kwargs):
    print('Args:',args)
    print('Kwargs:',kwargs)
Show_Data(1,2,3, name = 'Sanjana', age = 21)'''

















    
          
    
    
    
















