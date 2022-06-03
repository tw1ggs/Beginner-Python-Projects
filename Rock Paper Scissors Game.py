
import random


while True:
    choices = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(choices)
    player = input('Pick between Rock, Paper and Scissors  ')
    again = ['yes', 'no']

    while player == computer:
        player = input('Tie, Pick again ')
    while player not in choices:
        player = input('Input was wrong please, Pick between Rock, Paper and Scissors ')

    if player == 'Rock':
        if computer == 'Paper':
            print('You lost')
        if computer == 'Scissors':
            print('You Won')

    elif player == 'Paper':
        if computer == 'Rock':
            print('You Won')
        if computer == 'Scissors':
            print('You Lost')

    elif player == 'Scissors':
        if computer == 'Rock':
            print('You Lost')
        if computer == 'Paper':
            print('You Won')
    print(f'The computer chose {computer}')
    a = input('Play Again? Yes/No ')
    if a == 'Yes':
        continue
    else:
        break




