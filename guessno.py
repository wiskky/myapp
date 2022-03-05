#Program to allow user to enter the guess number from 1 to 10
import random

def guess(guessnumber):
    random_number = random.randint(1, guessnumber)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {guessnumber}: '))
        if (guess < random_number):
            print('Sorry, guess again. Too low.')
        elif (guess > random_number):
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed the {random_number}')

guess(30)