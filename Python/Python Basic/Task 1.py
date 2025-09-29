#1)Create a list with 5 elements and print it
'''a = [1,2,3,4,5]
print(a)'''

#2)Print the 4 element in the list
'''b = [1,2,3,4,5]
print(b[0:4])'''

#3)Print the last element in the list (negative index)
'''c = ['Apple','Banana','Cherry']
print(c[-1])'''

#4)Print the 3rd, 4th and 5th element in a single code.
'''d = [1,2,3,4,5]
print(d[2:4])'''

#5)Change the 2nd element by replaced by new one.
'''e = ['Apple','Banana','Cherry']
e[1]='Blackcurrent'
print(e)'''

#6)Add an element in the 3rd index position
'''f = ['Apple','Banana','Cherry','Papaya']
f.insert(3,'Orange')
print(f)'''

#7)Add an element in the last position
'''g = ['Apple','Banana','Cherry']
g.append('Orange')
print(g)'''

#8)Create 2 different list and join them with out creating a new list
'''list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1.extend(list2)
print(list1)'''

#9)Eliminate a specific element in the list
'''a = ['Apple','Banana','Cherry']
a.remove('Banana')
print(a)'''

#10)Eliminate the 3rd element in the list
'''a = ['Apple','Banana','Cherry','Papaya']
a.pop(2)
print(a)'''

#11)Clear the list elements
'''a = ['Apple','Banana','Cherry','Papaya']
a.clear()
print(a)'''

#12)Add two lists
'''a = [1,2,3,4]
b = [5,6,7,8]
c =a+b
print(c)'''

#13)Print the elements in a list by reverse order
'''a = [1,2,3,4]
a.reverse()
print(a)'''

#14)Count the elements in the list
'''a = ['Apple','Banana','Cherry','Papaya']
print(len(a))'''

#15)Create a tuple and add an element and remove the 3rd element in the tuple
'''a = ('Apple','Banana','Cherry','Papaya')
b = list(a)
b.append('Orange')
print(b)
b.pop(2)
print(b)
a = tuple(b)
print(a)
print(type(a))
print(type(b))'''








