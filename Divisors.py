# print the list of divisors for the given number
# Ask user to enter a number
a = int(input("Enter a number other than 0 or 1: "))
# List b is simply a range of numbers till the user entered
b = range(2,a)
# List c is to store the divisors
c = []
for element in b:
#divisors divide a number evenly
    if a % element is 0:
# add that number to list c
        c.append(element)
# print the final list
print(c)