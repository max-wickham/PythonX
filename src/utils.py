from node import Npode

def seperated_print(items : list[Node], seperator = ','):
    for index,item in enumerate(items):
        item.print_cpp()
        if index < (len(items) - 1):
            print(seperator)