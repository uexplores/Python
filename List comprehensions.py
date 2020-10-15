# List a is the list of squares in the range 20
x = int(input("Enter a range, a number until which you like the squares: "))
a = [x**2 for x in range(x)]
print(a)
# List b will only have even numbers from List a
b = [i for i in a if i%2 == 0 ]
print(b)
# List c will only have odd numbers from List a
c = [i for i in a if i%2 == 1 ]
print(c)