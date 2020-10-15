# print only the numbers that are in common in both the lists
# used randrange from random
from random import randrange
firstrange = int(input("Enter the range for 1st list of random numbers: "))
size1 = int(input("Enter the desired size for 1st list of random numbers: "))
secondrange = int(input("Enter the range for 2nd list of random numbers: "))
size2 = int(input("Enter the desired size for 2nd list of random numbers: "))
# List a is random and always has numbers less than 60
a = list(randrange(firstrange) for i in range(size1))
print(a)
# List b is random and always has numbers less than 40
b = list(randrange(secondrange) for i in range(size2))
print(b)
c = [] 
if len(a) < len(b):
    for i in a:
        if i in b:
            if i not in c:
                c.append(i)
else:
    for i in b:
        if i in a:
            if i not in c:
                c.append(i)
print(c)