def perform_mathematical_operation(operator):
    number1 = input("Please enter an integer and press enter: ")
    number2 = input("Please type another integer and press enter: ")
    number1 = int(number1)
    number2 = int(number2)
    result = None
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        result = number1 / number2
    elif operator == '%':
        result = number1 % number2
    elif operator == '//':
        result = number1 // number2
    elif operator == '**':
        result = number1 ** number2

    print(f"{number1} {operator} {number2} = {result}")

perform_mathematical_operation('+')
perform_mathematical_operation('-')
perform_mathematical_operation('*')
perform_mathematical_operation('/')
perform_mathematical_operation('%')
perform_mathematical_operation('//')
perform_mathematical_operation('**')

