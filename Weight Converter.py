while True:
    weight = input('Enter your weight ')
    wint = float(weight)
    sint = float(weight)
    size = input('lbs or kgs ')

    k = sint * 1
    l = wint * 2

    if size == 'l':
        print(f'Your lbs is {l}')
    elif size == 'k':
        print(f'youre kg is {k}')
