#List Less Than Ten
a = [1,99,23,55,2,10,11,76,8,9,3]
b = []
c = int(input("Enter a number: "))
for element in a:
    if element < c:
        b.append(element)
print(b)