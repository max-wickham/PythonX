from dataclasses import dataclass
from node import Node
from class_types import Type

class Expression(Node):
    ...

@dataclass
class Variable(Expression):
    name : str
    object_type : str

    def print_cpp(self):
        print(" ", name, " ")

    
class BinaryExpression(Expression):
    ...

@dataclass
class Addition(Expression):
    '''
    Use type to find the code needed for addition
    '''
    left_expression : Expression
    right_expression : Expression
    expression_type : Type

    def print_cpp(self):
        expression_type.print_addition(left_expression, right_expression)