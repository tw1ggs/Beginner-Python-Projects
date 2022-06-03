while True:
    start = 'The car has started'
    stop = 'The car has stopped'
    s = 'Start - to start the car'
    op = 'Stop - to stop the car'
    q = 'quit - to exit'
    options = [s, op, q,]
    user = input('> ')

    if user == 'help':
        for driv in options:
            print(driv)   
    elif user == 'start':
        print(start)
    elif user == 'stop':
        print(stop)
    elif user == 'quit':
        print('the game has ended')
        break
    else:
        while user not in options:
            print('Not a valid input')
            break