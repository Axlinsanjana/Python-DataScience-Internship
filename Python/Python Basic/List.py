#Python Collections(Arrays)
#1)List:
'''a = ['Apple', 'Orange', 'Grapes', 'Grapes']
print(a)'''

#Print the Second Item of the list:
'''a = ['Apple', 'Orange', 'Grapes']
print(a[1])'''

#Negative Indexing:
'''a = ['Apple', 'Orange', 'Grapes']
print(a[-1])'''

#Range of Indexes:
'''a = ['Apple', 'Orange', 'Grapes', 'Banana', 'Papaya']
print(a[2:6])'''

#Change Item Value:
'''a = ['Apple', 'Orange', 'Grapes', 'Banana', 'Papaya']
a[1]= 'Pineapple'
print(a)'''

#Insert Items:
'''a = ['Apple', 'Orange', 'Grapes']
a.insert(2,'Papaya')
print(a)'''

#Append Items:
'''a = ['Apple', 'Orange', 'Grapes']
a.append('Papaya')
print(a)'''

#Extend List:
'''a = ['Apple', 'Orange', 'Grapes']
b = ['Papaya',  'Pineapple', 'Cherry']
a.extend(b)
print(a)'''

#Remove List Items: (using items)
'''a = ['Apple', 'Orange', 'Grapes']
a.remove('Orange')
print(a)'''

#Remove Specified Index: (using index)
'''a = ['Apple', 'Orange', 'Grapes']
a.pop(1)
print(a)'''

#Clear the list:
'''a = ['Apple', 'Orange', 'Grapes']
a.clear()
print(a)'''

#Join two List:
'''a = ['Apple', 'Orange', 'Grapes']
b = ['Papaya',  'Pineapple', 'Cherry']
c = a+b
print(c)'''

#Returns copy of the list:
'''a = ['Apple', 'Orange', 'Grapes']
b = a.copy()
b.append('Papaya')
print(b)'''

#Returns a number of same elements:
'''a = ['Apple', 'Orange', 'Grapes','Apple']
print(a.count('Apple'))'''

#Returns index of the element:
'''a = ['Apple', 'Orange', 'Grapes','Apple']
print(a.index('Apple'))'''

#Reverse:
'''a = ['Apple', 'Orange', 'Grapes']
a.reverse()
print(a)'''

#Total count of the elements:
'''a = ['Apple', 'Orange', 'Grapes']
print(len(a))'''

#Eg:
'''a = 'hlo'
length = len(a)
print(length)'''











