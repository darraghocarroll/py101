import json

with open("calculator_messages.json", "r") as file:
    MESSAGES = json.load(file)

VALID_OPERATIONS = ['+','-','*','/']

def prompt(message):
    print(f"==> {message}")

def get_number(number_order):
    prompt(f'What is the {number_order} number? ')
    user_input = input()
    return user_input

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def get_operation():
    prompt('What operation would you like to perform? (+ , - , * , /) ')
    user_input = input()
    return user_input

def invalid_operation(operator):
    return True if operator not in VALID_OPERATIONS else False

def calculate_result(num1,num2,operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2

def get_cont_choice():
    prompt('Would you like to run another calculation? (y/n) ')
    choice = input().casefold()
    return choice


prompt(MESSAGES["welcome"])

calculate_again = 'not_asked_for_yet'

while calculate_again.casefold() != 'n':

    num1 = get_number('first')
    while invalid_number(num1):
        prompt('Hmmm... that doesnt look like a valid number. Try Again. ')
        num1 = input()

    num2 = get_number('second')
    while invalid_number(num2):
        prompt('Hmmm... that doesnt look like a valid number. Try Again. ')
        num2 = input()

    operation = get_operation()
    while invalid_operation(operation):
        prompt('Hmmm... that doesnt look like a valid operation. Try Again. ')
        operation = input()

    result = calculate_result(float(num1),float(num2),operation)

    prompt(f'The result of {num1} {operation} {num2} is {result}!')

    calculate_again = get_cont_choice()
    while calculate_again not in ['y', 'n']:
        prompt('Hmmm... that doesnt look like a valid choice. Try Again. ')
        calculate_again = input()

prompt('Thank you, have a great day!')




    