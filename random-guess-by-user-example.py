import random

def guess(x):
    random_num = random.randint(1,x)
    guess =0
    while guess != random_num:
        guess = int(input(f'guess a number between 1 and {x}:'))
        if guess <random_num :
            print('sorry, guess again ,too low')
        elif guess >random_num :
            print('sorry guess aain, too high')

    print(f'you win, you guessed the num correct which is {random_num}')



guess(10)
