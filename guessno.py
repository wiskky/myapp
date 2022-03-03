#Program to allow user to enter the guess number from 1 to 10
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if (guess < random_number):
            print('Sorry, guess again. Too low.')
        elif (guess > random_number):
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed the {random_number}')

guess(40)
