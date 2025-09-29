#Inheritance:
#Single
'''class Parent:
    def father(self):
        print('I am father')
class Child(Parent):
    def child(self):
        print('I am child')

ch = Child()
ch.child()
ch.father()'''


#Multi level:
'''class Parent:
    def father(self):
        print('I am father')
class Child1(Parent):
    def child_1(self):
        print('I am first child')
class Child2(Child1):
    def child_2(self):
        print('I am second child')

ch= Child1()
ch.child_1()
ch.father()
ch2 = Child2()
ch2.child_2()'''


#Multiple:
'''class Parent:
    def father(self):
        print('I am a father')
class child1:
    def child_1(self):
        print('I am first Child')
class child2(Parent,child1):
    def child_2(self):
        print('I am second child')

ch = child2()
ch.child_2()
ch.child_1()
ch.father()'''

#Hierarchical:
'''class parent:
    def father(self):
        print('I am a father')
class child1(parent):
    def child_1(self):
        print('I am first child')
class child2(parent):
    def child_2(self):
        print('I am second child')

ch = child2()
ch.child_2()
ch.father()
ch2 = child1()
ch2.child_1()
ch2.father()'''

#Hybrid:
'''class Father:
    def father(self):
        print('Iam father')
class Mother(Father):
    def mother(self):
        print('I am mother')
class Parent:
    def parent(self):
        print('I am parent')
class Child(Mother,Parent):
    def child(self):
        print('I am child')

x = Child()
x.child()
x.parent()
x.mother()
x.father()'''


class Bird:
    def fly(self):
        print('Birds fly')

class plane:
    def fly(self):
        print('plane fly')
        
def flying(obj):
   obj.fly()
   
b = Bird()
p = plane()
b.fly()
p.fly()

    

















