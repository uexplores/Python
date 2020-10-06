First = int(input("First: "))
Second = int(input("Second: "))
if Second < First:
    x=First
    First=Second
    Second=x
    print("A")
else:
    numbers = range(First, Second,2)
    for number in numbers:
        print(number)
