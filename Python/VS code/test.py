import datetime
print(datetime.datetime.now())


import math
print(math.sqrt(49))


from pack import module1 as c, module2 as b   #importing package
b.product(5,6)
c.Sum(1,5)


from pack.module1 import difference    #importing package(specific function/ object from a module)
difference(5,4)