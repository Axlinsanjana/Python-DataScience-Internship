a = int(input('Enter a number:'))
b = str(a)
length = len(b)
sum = 0
for i in b:
    sum = sum + int(i)**length
if a==sum:
    print(a,'is an armstrong number')
else:
    print(a,'not an armstrong number')
