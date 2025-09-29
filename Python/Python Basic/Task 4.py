#1. Print the pattern 
'''1 3 5 7 9
1 3 5 7
1 3 5
1 3
1'''
#OUTPUT:
'''n = 5
for i in range(n,0,-1):
    for j in range(1,2*i,2):
        print(j,end = ' ')
    print()'''


#2. Find the vowel count In a string using python function.
'''def vowel(n):
    count = 0
    for i in n:
        if i.lower()in 'aeiou':
            count = count+1
    return count
n = input('Enter a string:')
x = vowel(n)
print(x)'''


#3. Find the last digit of a number is a multiple of 5.
'''n = int(input("Enter a number: "))
x = n%10 
if x%5 == 0:
    print("Last digit is a multiple of 5.")
else:
    print("Last digit is NOT a multiple of 5.")'''

    
#4.Find the middle value in a list without using built-in function:



