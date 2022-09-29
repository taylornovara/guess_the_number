# from art import logo
import random
import art

EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5


def random_number():
    """Generates a random number between 1 and 100"""
    return random.randint(1, 100)


def compare(rand_number, user_guess, tries):
    """Compares the generated number to the user guess, Returns the number of tries remaining"""
    if rand_number > user_guess:
        print('Too Low')
        return tries - 1
    elif rand_number < user_guess:
        print('Too High')
        return tries - 1
    else:
        print('You won! You guessed the correct number!')


def set_difficulty():
    """Sets the difficulty level based on user input"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TRIES
    else:
        return HARD_LEVEL_TRIES


def guess_the_number():
    random_num = random_number()

    print(art.logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    print(f'Test code: Pssst, the correct answer is {random_num}.')
    tries = set_difficulty()

    user_guess = 0
    while user_guess != random_num:
        print(f'You have {tries} attempts remaining to guess the number.')
        user_guess = int(input('Make a guess: '))
        tries = compare(random_num, user_guess, tries)
        if tries == 0:
            print(f'You ran out of tries. The correct answer is {random_num}.')
            return


guess_the_number()
