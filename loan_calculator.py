import json

with open('loan_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message} ')

def get_value(calc_value):
    prompt(MESSAGES['get_value'] + calc_value)
    value = input()
    return value

def invalid_input(user_input):
    try:
        user_input = float(user_input)
        if user_input <= 0:
            raise ValueError(f"Value must be > 0: {user_input}")

    except ValueError:
        return True
    return False

def calculation(loan_amount, monthly_interest, loan_duration_months):
    monthly_payment = loan_amount * (
        monthly_interest / (1 - (1 + monthly_interest) ** (-loan_duration_months)))
    return monthly_payment

def another_calc():
    prompt(MESSAGES['get_choice'])
    choice = input().casefold()
    return choice

prompt(MESSAGES['welcome'])

choice_to_calc_again = "not asked for yet "

while choice_to_calc_again != 'n':

    print('==============================================')
    loan_amount = get_value("LOAN AMOUNT")
    while invalid_input(loan_amount):
        prompt(MESSAGES['invalid_input'])
        loan_amount = input()

    loan_amount = float(loan_amount)

    APR = get_value("APR")
    while invalid_input(APR):
        prompt(MESSAGES['invalid_input'])
        APR = input()

    APR = float(APR)
    APR = APR / 100

    loan_duration_years = get_value("LOAN DURATION IN YEARS")
    while invalid_input(loan_duration_years):
        prompt(MESSAGES['invalid_input'])
        loan_duration_years = input()

    loan_duration_years = float(loan_duration_years)

    loan_duration_months = loan_duration_years * 12
    monthly_interest = APR / 12

    monthly_payment = calculation(loan_amount, monthly_interest, loan_duration_months)

    prompt(f'Your monthly payment is ${monthly_payment:.2f}')
    choice_to_calc_again = another_calc()
    while choice_to_calc_again not in ['y', 'n']:
        prompt(MESSAGES['invalid_input'])
        choice_to_calc_again = input()

prompt(MESSAGES['goodbye'])