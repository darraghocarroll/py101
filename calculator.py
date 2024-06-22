VALID_NUMBERS = ['1','2','3','4','5','6','7','8','9','10']
VALID_OPERATIONS = ['+','-','*','/']


prompt("Welcome to Calculator!\n")

calculate_again = 'not_asked_for_yet'

while calculate_again.casefold() != 'n':

    first = get_number('first')
    second = get_number('second')

    operation = get_operation()

    result = calculate_result(first,second,operation)

    print(f'your first number is {first}')
    print(f'your second number is {second}')

    prompt(f'The result of {first} {operation} {second} is {result}!')

    calculate_again = cont_choice()

prompt('Thank you, have a great day!')




    