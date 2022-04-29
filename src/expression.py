from dataclasses import dataclass
from node import Node

class Expression(Node):
    ...

@dataclass
class Variable(Expression):
    name : str

    def print_cpp(self):
        print(" ", self.name, " ")

    
class BinaryExpression(Expression):
    ...

@dataclass
class Addition(Expression):
    '''
    Use type to find the code needed for addition
    '''
    left_expression : Expression
    right_expression : Expression
    expression_type : 'Type'

    def print_cpp(self):
        expression_type.print_addition(left_expression, right_expression)

@dataclass
class FunctionCall(Expression):

    expression_list : list[Expression]

    def print_cpp(self):
        ...

@dataclass
class PrintCall(FunctionCall):

    expression_list : list[Expression]

    def print_cpp(self):
        print('print.attr("__call__")(')
        self.seperated_print(self.expression_list)
        print(')')

@dataclass
class NumberConstant(Expression):

    value : float

    def print_cpp(self):
        print(self.value)
        
@dataclass 
class Return(Expression):

    expression : Expression

    def print_cpp(self):
        print('return')
        self.expression.print_cpp()