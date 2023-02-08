from random import randint

name = input('Hi! What is your name? ')


for guess_number in range(1,6):
    month_number = randint(1, 12)
    year_number = randint (1960, 2010)

    print('Guess', guess_number, ' were you born in', month_number, '/', year_number, '?')

    response = input('yes or no?')

    if response == 'yes':
        print('I knew it!')
        exit()
    elif guess_number == 5:
        print('I have other things to do. Good bye.')
    else:
        print('Draft! lemme try again!')
