from art import logo, vs
from random import randint
from game_data import data
from replit import clear

DATA_LENGTH = len(data)


def display_game_logo():
    print(logo)


def play_game():
    display_game_logo()
    compare_user_choice()


def compare_user_choice():
    user_choice, correct_choice = '', ''
    game_has_ended = False
    current_stage, current_score = 0, 0

    random_a = randint(0, len(data) - 1)
    random_b = random_a

    while not game_has_ended:
        while random_a == random_b:
            random_b = randint(0, len(data) - 1)
        
        correct_choice = 'A' if get_details(random_a)[1] > get_details(random_b)[1] else 'B'

        show_comparison(random_a, random_b)

        user_choice = input('Who has more followers? Type \'A\' or \'B\': ').upper()

        if user_choice != correct_choice:
            game_has_ended = True
        else:
            current_stage, current_score = give_user_feedback(current_stage, current_score, game_has_ended)

            random_a = random_b
    else:
        give_user_feedback(current_stage, current_score, game_has_ended)

        
def show_comparison(random_a, random_b):
    print(f'Compare A: {get_details(random_a)[0]}, a {get_details(random_a)[2]}, from {get_details(random_a)[3]}.')
    print(vs)
    print(f'Against B: {get_details(random_b)[0]}, a {get_details(random_b)[2]}, from {get_details(random_b)[3]}.')


def give_user_feedback(current_stage, current_score, has_game_ended):
    clear()
    display_game_logo()

    if has_game_ended:
        print('Sorry, that\'s wrong. Final score: {final_score}.'.format(final_score=current_score))
    else:
        current_stage += 1
        current_score += 1
        print('You\'re right! Current score: {}.'.format(current_score))
        return current_stage, current_score


def get_details(index):
    return data[index]['name'], data[index]['follower_count'], data[index]['description'], data[index]['country']


play_game()
