import random

number = random.randint(1,9)
guess = 0
count = 0
while guess != number and guess != "exit":
    guess = input("What's your guess?")
    if guess == "exit":
        break
    guess = int(guess)
    count += 1
    if guess < number-1:
        print("Too low!")
    elif guess > number+1:
        print("Too high!")
    elif (guess is (number+1)) or (guess is (number-1)):
        print("Almost there")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")
