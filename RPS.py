
import os
import random

POSSIBLE_HANDS = ['rock', 'paper', 'scissors','lizard','spock']
GAME_LOGIC = {  #dict of winning user hands
    'rock':     ['lizard', 'scissors'],
    'paper':    ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard':   ['spock', 'paper'],
    'spock':    ['scissors', 'rock']
}
POSSIBLE_TOURNAMENT_LENGTH = [1,3,5]

def prompt(message):        #identifies computer output
    print(f'==> {message}')

def invalid_tournament_length(user_input): #checks if tournament length is a valid input
    try:
        user_input = int(user_input)
        if user_input not in POSSIBLE_TOURNAMENT_LENGTH:
            return True
    except TypeError:
        return True

    return False

def invalid_hand_choice(user_input): #error handling if invalid hand
    try:
        if user_input not in POSSIBLE_HANDS:
            return True
    except TypeError:
        return True

    return False

def calculate_hand_winner(user_hand, computer_hand): #RPS game logic
    if user_hand in GAME_LOGIC[user_hand]:
        player_score['USER'] += 1
    elif user_hand == computer_hand:
        return 'tie'
    else:
        player_score['COMPUTER'] += 1

player_score = {                 #Create user and score dict
    'USER' : 0,
    'COMPUTER' : 0,
    }

os.system('clear')

while True:
    print('===============WELCOME TO RPS====================')
    prompt('How many Hands would you like to play in this tournament? ') # How long is this RPS tournament ?
    prompt('Choices are 1, 3, or 5 hands. ')
    tournament_length = input()

    while invalid_tournament_length(tournament_length): #check if tournament length is valid
        prompt('Sorry, you must chose either 1, 3, or 5 hands. ')
        tournament_length = input()


    current_hand = 1  #setting first hand number

    while current_hand <= int(tournament_length): #while loop to play tournament length
        print('=============================================================')
        prompt(f'This is HAND #{current_hand}')

        prompt(f'What hand would you like to play, {', '.join(POSSIBLE_HANDS)}')
        user_hand = input().casefold()
        while invalid_hand_choice(user_hand):
            prompt(f'Sorry, you must chose either {', '.join(POSSIBLE_HANDS)} ')
            user_hand = input().casefold()

        print('=============================================================')
        computer_hand = random.choice(POSSIBLE_HANDS)
        prompt(f'The COMPUTER has chosen {computer_hand}')
        print('=============================================================')

        result = calculate_hand_winner(user_hand, computer_hand)

        if result == 'tie':
            prompt(f'That was a TIE, we will have to replay HAND #{current_hand}')
            current_hand += 0
        else:
            current_hand += 1

        print('=============================================================')
        prompt(f'The Score is {player_score}')

    if player_score['USER'] > player_score['COMPUTER']:
        print('=============================================================')
        prompt('THE USER WINS!!!!!')
    else:
        print('=============================================================')
        prompt('THE COMPUTER WINS!!!!!')

    prompt('Would you like to play again? [y/n]' )
    play_again = input().casefold()

    while play_again not in ['y', 'n']:
        prompt("Sorry, you must choose 'y' or 'n'")
        play_again = input().casefold()

    if play_again == 'y':
        player_score['USER'] = 0
        player_score['COMPUTER'] = 0
        os.system('clear')
    else:
        break