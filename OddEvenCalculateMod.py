20# Based on the input number, print Even or Odd
# if the number is a multiple of 4, print out a different message
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
# Determine whether the input numbers are Odd/Even, multiples of 4
if first_number > 0:
    if first_number % 2 == 0:
        if first_number % 4 == 0:
            print("{} is a multiple of 4".format(first_number))
        else:
            print("{} is an even number".format(first_number))
    else:
        print("{} is an odd number".format(first_number))
if second_number > 0:
    if second_number % 2 == 0:
        if second_number % 4 == 0:
            print("{} is a multiple of 4".format(second_number))
        else:
            print("{} is an even number".format(second_number))
    else:
        print("{} is an odd number".format(second_number))
# Determine whether 1st number can be divided 2nd number 
# Denominator is zero
if second_number == 0:
    if first_number ==0:
        print("{} is divided by {}, the answer is 0".format(first_number,second_number))
    else:
        print("{} cannot be divided by {}".format(first_number,second_number))
# Denominator is negative
elif second_number < 0:
    if first_number < 0:
        if first_number % second_number == 0:
            print("{} divides {} evenly".format(second_number,first_number))
        else:
            print("{} does not divide {} evenly".format(first_number,second_number))
    elif first_number ==0:
        print("{} is neither even nor odd, when you divide zero with any number, it always results in zero".format(first_number))
    else:
        print("{} is positive, {} is negative, cannot divide these".format(first_number,second_number))
else:
    if first_number ==0:
        print("Sorry the result is 0")
    elif first_number <0:
        print("{} is negative, {} is positive, cannot divide these".format(first_number,second_number))
    elif first_number % second_number == 0:
        print("{} divides {} evenly".format(second_number,first_number))
    else:
        print("{} does not divide {} evenly".format(second_number,first_number))