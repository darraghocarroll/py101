
import os
import random

POSSIBLE_HANDS = ['rock', 'paper', 'scissors','lizard','spock']
GAME_LOGIC = {  #dict of winning user hands
    'rock':     {'lizard': 'ROCK CRUSHES LIZARD!',
                 'scissors': 'ROCK CRUSHES SCISSORS!'},
    'paper':    {'rock': 'PAPER SUFFOCATES ROCK!', 
                  'spock': 'PAPER DISPROVES SPOCK!'},
    'scissors': {'paper': 'SCISSORS CUTS PAPER!',
                  'lizard': 'SCISSORS DECAPITATES LIZARD!'},
    'lizard':   {'spock': 'LIZARD POISONS SPOCK!',
                 'paper': 'LIZARD EATS PAPER!'},
    'spock':    {'scissors': 'SPOCK CRUSHES SCISSORS',
                 'rock': 'SPOCK VAPORIZES ROCK!'}
}
POSSIBLE_TOURNAMENT_LENGTH = [1,3,5]

def prompt(message):        
    print(f'==> {message}')
    
def display_welcome_message():   
    print('===============WELCOME TO RPS====================')

def display_separater():         
    print('=============================================================')
    
def get_tournament_length(): #How many rounds is this RPS tournament?
    prompt('How many Hands would you like to play in this tournament? ')
    prompt('Choices are 1, 3, or 5 hands. ')
    return input()

def display_hand_choices(user_hand, computer_hand):
    prompt(f'The COMPUTER chose -- {computer_hand.upper()} --')
    prompt(f'The USER chose -- {user_hand.upper()} --')
    
def display_current_round(current_round):  
    prompt(f'This is ROUND #{current_round}')
    
def display_score():#display score
    prompt(f'The Score is USER:{player_score['USER']} COMPUTER:{player_score['COMPUTER']}')
    
def get_user_hand(): #get user hand choice
    prompt(f'What hand would you like to play? [{', '.join(POSSIBLE_HANDS)}]')
    return input().casefold()

def when_a_hand_is_tied(current_round):#handling of a tied round
    prompt(f'That was a TIE, we will have to replay HAND #{current_round}')
    current_round += 0 #replay of the round, noting to programmer

def invalid_tournament_length(user_input): 
    try:
        user_input = int(user_input)
        if user_input not in POSSIBLE_TOURNAMENT_LENGTH:
            return True
    except (TypeError, ValueError):
        return True

    return False

def invalid_hand_choice(user_input): #error handling
    try:
        if user_input not in POSSIBLE_HANDS:
            return True
    except TypeError:
        return True

    return False

#Calculates hand winner and updates score
def calculate_hand_winner(user_hand, computer_hand): 
    if computer_hand in GAME_LOGIC[user_hand]:
        player_score['USER'] += 1
        prompt(GAME_LOGIC[user_hand][computer_hand])
        prompt('The USER has WON THIS HAND!')
    elif user_hand == computer_hand:
        return 'tie'
    else:
        player_score['COMPUTER'] += 1
        prompt(GAME_LOGIC[computer_hand][user_hand])
        prompt('The COMPUTER has WON THIS HAND!')
        
def display_tournament_winner(): #Displays Tournament Winner 
    if player_score['USER'] > player_score['COMPUTER']:
        display_separater()
        prompt('THE USER WINS!!!!!')
    else:
        display_separater()
        prompt('THE COMPUTER WINS!!!!!')
        
def play_one_round(): #one round of RPS-LS
    global current_round
    
    display_current_round(current_round)
        
    user_hand = get_user_hand()
    
    while invalid_hand_choice(user_hand):
        prompt(f'Sorry, you must chose either {', '.join(POSSIBLE_HANDS)} ')
        user_hand = input().casefold()

    os.system('clear')
        
    display_separater()
    computer_hand = random.choice(POSSIBLE_HANDS)
        
    display_hand_choices(user_hand, computer_hand)
        
    result = calculate_hand_winner(user_hand, computer_hand)

    if result == 'tie':
        when_a_hand_is_tied(current_round)
    else:
        current_round += 1

    display_separater()

    display_score()
    
def would_you_like_to_play_again(): 
    prompt('Would you like to play again? [y/n]' )
    play_again = input().casefold()

    while play_again not in ['y', 'n']:
        prompt("Sorry, you must choose 'y' or 'n'")
        play_again = input().casefold()
    
    return play_again


os.system('clear')

while True:  #MAIN LOOP
    display_welcome_message()
    
    player_score = { #Create or reset both scores to 0 
    'USER' : 0,
    'COMPUTER' : 0,
    }
    
    tournament_length = get_tournament_length()  

    while invalid_tournament_length(tournament_length):
        prompt('Sorry, you must chose either 1, 3, or 5 hands. ')
        tournament_length = input()

    tournament_length = int(tournament_length)  
    
    current_round = 1  #setting first round number

    while current_round <= tournament_length:# user-selected # of rounds

       play_one_round()
    
    display_tournament_winner()#
    
    play_again = would_you_like_to_play_again()

    if play_again == 'y':
        os.system('clear')
    else:
        prompt('GOODBYE!')
        break