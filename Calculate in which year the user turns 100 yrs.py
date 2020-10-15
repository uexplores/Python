# capture name
name = str(input('Enter your name: '))
# capture age
age = int(input('{}, please enter your age: '.format(name)))
# calculate the year when user will be 100 years old
x = 100 - age
y = 2020 + x
z=int(input('{}.now enter a number between 1 to 10: '.format(name)))
msg = str('Hey {}, do you know that you will be 100 yrs old in the year {}' .format(name, y))
print(z*(msg+"\n"))