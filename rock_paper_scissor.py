# rock_paper_scissor
import random


def choice():
    i = 0
    w = 0
    l = 0
    while i < 6:
        user_choice = input('enter your choice: ')
        a_list = ['r', 'p', 's']
        computer_choice = random.choice(a_list)

        if computer_choice == user_choice:
            print(f'computer said {computer_choice}')
            print('it was a draw')
            print(f'Your score is {w} & Computer is {l} ')

        elif win(user_choice,computer_choice):
            print(f'computer said {computer_choice}')
            print('you won')
            w += 1
            print(f'Your score is {w} & Computer is {l} ')

        else:
            print(f'computer said {computer_choice}')
            print('you loose')
            l +=1
            print(f'Your score is {w} & Computer is {l} ')

        i +=1
        print(f' Attempt {i}/5')

def win(user_choice,computer_choice):
    if (user_choice == 'r' and computer_choice == 's') or \
            (user_choice == 'p' and computer_choice == 'r') or \
            (user_choice == 's' and computer_choice == 'p'):
        return True

choice()