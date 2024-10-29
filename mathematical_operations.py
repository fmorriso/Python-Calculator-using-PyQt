from enum import StrEnum

class MathOperation(StrEnum):
    addition= '+'
    subtraction= '-'
    multiplication= '*'
    division= '/'
    modulo= '%'

    @staticmethod
    def get_operations_list():
        lst: list[str] = []
        for operator in MathOperation:
            lst.append(f'{operator.value} {operator.name}')
        return lst


    def __str__(self):
        match self.name:
            case '+':
                return '+ Addition'
            case '-':
                return '- Subtraction'
            case '*':
                return '* Multiplication'
            case '/':
                return '/ Division'
            case '%':
                return '% Modulo'
            case _:
                return 'Operation not found'

    @staticmethod
    def to_string(val: str):
        match val[0]:
            case '+':
                return MathOperation.addition
            case '-':
                return MathOperation.subtraction
            case '*':
                return MathOperation.multiplication
            case '/':
                return MathOperation.division
            case '%':
                return MathOperation.modulo

