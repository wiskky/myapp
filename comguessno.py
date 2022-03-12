import random

#This program allows computer to guess the user number correctly

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high
        feedback = input(f'is {guess} to high(H), too low(L) or correct(C)')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay, congrats. You have guessed the number, {guess} correctly')

computer_guess(20)
