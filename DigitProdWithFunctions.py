# function to calculate product of digits in a number
def digit_prod(num):
# read user input into a temporary variable
  temp = num
# declare b, it will be used to store the output of this program  
  b = 1
# check if temp > 1 before adding it
  while (temp>1): 
# take the right most digit and store it in a
    a = temp % 10
# Now remove the last digit and ensure no fraction
    temp = int(temp/10)
# if user inputs a number with 0, handle it
    if (a==0):
# assigning 1, it it were a sum then change a to 0
      a = 1
# multiply with the current value in b
    b *= a
  return b

# take a number as input from user
num = int(input("Enter a number: "))
# print the result
print (digit_prod(num))
