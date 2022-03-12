<<<<<<< HEAD
#Program to allow user to enter the guess number from 1 to 40
import random

#This program allows user to guess the correct number from 1 to 40

#system will ask user to enter the guess number and if is correct the user wins
# if not the user will continue to enter the number until it guess it right.

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

guess(40)
