import random

while True:
    player = int(input('Guess the number (between 1-10) '))
    computer = random.randint(1, 10)
    guess_min = 0
    guess_max = 3

    while guess_min < guess_max:
        
        guess_min += 1
        if player == computer:
            print('Correct')
            break
        elif player < computer:
            player = int(input('A little higher '))
            guess_min += 1
        elif player > computer:
            player = int(input('A little lower '))
            guess_min += 1
    else:
        print("You've exhausted your tries")
    print('The computer chose ' + str(computer))
    re = input('Do you want to play again? YES/NO ').upper()
    if re == 'YES':
        continue
    else:
        break
