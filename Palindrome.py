str1 = str(input("Enter the word: "))
str2 = str1[::-1]
if str1 == str2:
    print("Palindrome")
else:
    print("Not a palindrome")