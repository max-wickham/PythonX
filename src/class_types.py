from node import Node
from information import PythonXClassInformation
from expression import Expression

class Type(Node):

    def print_addition(left_expression : Expression, right_expression : Expression): ...


class Integer(Type):

    def print_addition(left_expression : Expression, right_expression : Expression):
        print('((')
        left_expression.print_cpp() 
        print(')+(')
        right_expression.print_cpp() 
        print('))')

class PythonClass(Type):

    def print_addition(left_expression : Expression, right_expression : Expression):
        ...

@dataclass
class PythonXClass(Type):

    information : PythonXClassInformation

    def print_addition(left_expression : Expression, right_expression : Expression):
        print('(')
        left_expression.print_cpp() 
        print('.__add__(')
        right_expression.print_cpp() 
        print('))')