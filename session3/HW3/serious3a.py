print('Welcome to Word Jumble game')
from random import *
words = ['food', 'sleep', 'assignment', 'champion']
choice = choice(words)
word = list(choice)
shuffle(word)
print(*word)
print('You have 5 times to guess')
count = 0
while count < 5 :
    answer = input('Your answer is: ')
    if answer == choice:
        print('You are right!')
        break
    else:
        print("Sorry:( that's wrong")
        print("You can guess", 4 - count, 'more')
        count += 1
        if count == 5:
            print('GAME OVER!!')
