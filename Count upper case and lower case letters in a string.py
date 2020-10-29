'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.'''

def count_case(str1):
# Capital letter and small letter string as list
    upstr = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowstr = list('abcdefghijklmnopqrstuvwxyz')
# string2 captures the phrase given by user
    str2 = list(str1)
# list(str1.replace(" ", "")) can remove spaces
# counters to keep track of each case
    upper_case = 0
    lower_case = 0
    for element in str2:
        if element in upstr:
            upper_case = upper_case + 1
        if element in lowstr:
            lower_case = lower_case + 1

    str3 = ('No.of Lower case characters: '+ str(lower_case))
    str4 = ('No.of Upper case characters: '+ str(upper_case))
    return len(str2), str3, str4


# user enters input
str1 = str(input("Enter a phrase: "))
print(count_case(str1))
