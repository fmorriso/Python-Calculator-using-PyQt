import sys

from input_utilities import InputUtils
from output_utilities import OutputUtils


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_operation() -> str:
    choices: list[str] = ['+', '-', '*', '/']
    opr = InputUtils.get_single_choice('Operation', 'Select an operation', choices)
    return opr


def performOperation(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2


def performOneCalculation():
    num1 = InputUtils.get_decimal_number('First', 'Enter the first number:')
    num2 = InputUtils.get_decimal_number('Second', 'Enter the second number:')
    operation = get_operation()
    result = performOperation(num1, num2, operation)
    msg = f'{num1} {operation} {num2} = {result}'
    print(msg)
    OutputUtils.display_message(msg, 'Result')


def main():
    msg = f'Python version: {get_python_version()}'
    print(msg)
    # OutputUtils.display_message(msg, 'Python Version')

    keepCalculating = True
    while keepCalculating:
        performOneCalculation()
        keepCalculating = InputUtils.get_yesno_response("Perform another calculation?", 'Keep Calculating?')

    msg = 'Thank you for using my calculator'
    print(msg)
    OutputUtils.display_message(msg, 'Calculator')


if __name__ == '__main__':
    main()
