from node import Node
from dataclasses import dataclass
from class_types import Type
from expression import Expression, NumberConstant, PrintCall, Return, Variable

class Statement(Node):
    ...

@dataclass
class ExpressionStatement(Statement):
    
    expression : Expression

    def print_cpp(self):
        self.expression.print_cpp()
        print(';')

@dataclass
class Assignment(Statement):

    name : str
    expression : Expression = None

    def print_cpp(self):
        print(self.name)
        if self.expression is not None:
            print('=')
            self.expression.print_cpp()
        print(';')

@dataclass
class Deceleration(Statement):
    
    type_name : str
    assignment : Assignment

    def print_cpp(self):
        print(self.type_name)
        self.assignment.print_cpp()

@dataclass
class FunctionDefinition(Statement):

    name : str
    return_type : str
    parameter_list : list[Deceleration]
    statement_list : list[Statement]

    def _print_cpp_body(self):
        print('(')
        self.seperated_print(self.parameter_list)
        print(')')
        print('{')
        for statement in self.statement_list:
            statement.print_cpp()
        print('}')
    
    def print_cpp(self):
        print(self.return_type)
        print(self.name)
        self._print_cpp_body()

    def print_cpp_constructor(self, class_name : str):
        print(class_name)
        self._print_cpp_body()
        print()
        self.print_cpp()
    
@dataclass
class ClassDefinition(Statement):
    
    name : str
    method_list : list[FunctionDefinition]
    property_list : list[Deceleration]
    constructor : FunctionDefinition = None

    def print_cpp(self):
        print('class')
        print(self.name)
        print('{')
        print()
        print('public:')
        print()
        for prop in self.property_list:
            prop.print_cpp()
        print()
        if self.constructor is not None:
            self.constructor.print_cpp_constructor(self.name)
        print()
        for method in self.method_list:
            method.print_cpp()
            print()
        print('};')

        # TODO print converter to python object

        # TODO print boost python module 


assignment = Assignment('x', NumberConstant(784))
deceleration = Deceleration('int', assignment)
re_exp = Return(Variable('x'))
re_state = ExpressionStatement(re_exp)
function = FunctionDefinition('getX', 'int', [], [deceleration,re_state])
classdefinition = ClassDefinition('Test', [function], [])

classdefinition.print_cpp()