'''class hi:
    x = 5
    y = 8
obj = hi()
print(obj.x)
print(obj.y)'''



'''class hi:
    def my_name(self,name):
        print('My name is',name)
    def my_age(self,age):
        print('My age is',age)
obj = hi()
obj.my_name('sanjana')
obj.my_age(21)'''



'''class Details:
    def  __init__(self,name,age):
        self.name = name
        self.age = age

    def my_name(self):
        print('My name is', self.name)

    def my_age(self):
        print('My age is', self.age)

my_details = Details('axlin',21)
my_friend = Details('sanjana',21)

my_details.my_name()
my_details.my_age()

my_friend.my_name()
my_friend.my_age()'''


#Rectangle:
'''class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        x = self.length*self.width
        print('Area of rectangle',x)

    def perimeter(self):
        y = 2*(self.length+self.width)
        print('Parameter of rectangle',y)

first_rect = Rectangle(2,3)

first_rect.area()
first_rect.perimeter()

print("---------------")

second_rect = Rectangle(6,8)
second_rect.area()
second_rect.perimeter()'''
    

#Car:
'''class Car:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def display_info(self):
        print('Model:',self.model)
        print('Year:',self.year)
my_car = Car('Figo',2020)
my_car.display_info()'''
    

#Student details:
'''class Student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def Details(self):
        print('Name:',self.name)
        print('Roll_Number:',self.roll_number)
    def TotalMark(self):
        print('Marks:',self.marks)

info = Student('Axlin',2345)
info.Details()

calculate_grade = Student(2345)
calculate_grade.TotalMark()'''



'''class Student:
    def __init__(self,name,roll_number,mark):
        self.name = name
        self.roll_number = roll_number
        self.mark = mark
    def Details(self):
        print('Name:',self.name)
        print('Roll_Number:',self.roll_number)
    def Calculate_grade(self):
        if self.mark >= 80:
            print('Grade "A"')
        elif self.mark >= 60:
            print('Grade "B"')
        elif self.mark >= 50:
            print('Grade "C"')
        else:
            print('Failed')
       
info = Student('Axlin',2345,55)
info.Details()
info.Calculate_grade()'''


#Bank Statement:
'''class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder =  account_holder
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
    def withdraw(self,wd):
        self._balance -=wd
    def get_balance(self):
        print('Current balance:',self._balance)
sbi  = BankAccount('Sanjana',5000)
sbi.deposit(1000)
sbi.withdraw(500)
sbi.get_balance()'''

class example:
    pass


def hi():
    pass







        



