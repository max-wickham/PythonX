from dataclasses import dataclass

class Node:

    def print_cpp(self) -> None:
        ...

    def seperated_print(self, items : list['Node'], seperator = ','):
        for index,item in enumerate(items):
            item.print_cpp()
            if index < (len(items) - 1):
                print(seperator)