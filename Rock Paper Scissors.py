import random
'''Rules:
Rock beats scissors
Scissors beats paper
Paper beats rock'''
name =str(input("Enter your name: "))
b = ['R','P','S']
c = random.choice(b)
a = str(input("Enter R for Rock, P for Paper, S for Scissors: "))
print('{} picked {}'.format(name,a))
print('I picked {}'.format(c))
if (a == 'R' and c == 'S') or (a == 'S' and c == 'P') or (a == 'P' and c == 'R') or (a == b):
    print("{} win".format(name))
else: 
    print("I win")