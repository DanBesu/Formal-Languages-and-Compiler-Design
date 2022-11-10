import re
from SymbolTable import SymbolTable

P1_FILE = '/Users/dbesu/Desktop/lfcd/p1.txt'

ST_OUT_FILE = '/Users/dbesu/Desktop/lfcd/ST.out'
PIF_OUT_FILE = '/Users/dbesu/Desktop/lfcd/PIF.out'

RESERVED_WORDS = ['ridicaNumar', 'cuvant', 'parere', 'baga', 'arata', 'saZicemCa', 'dacaNu', 'arFi', 'nuArFi', 'seImparteLa', 'pleaca', 'deLa', 'panaLa', 'gata', 'adevarat', 'fals']
OPERATORS = ['+', '-', '*', '/', '<', '>', '=', '>=', '=<']
SEPARATORS = ['{', '}', '[', ']', '(', ')', ',', ' ', '\n']

NUMERIC_VALUE = "^0|[+|-][1-9]([0-9])*|[1-9]([0-9])*|[+|-][1-9]([0-9])*"
BOOLEAN_VALUE = "^(adevarat)|(fals)$"
STRING_VALUE = "^\"[a-zA-Z0-9_?!#*./%+=<>;)(}{ ]+\""
IDENTIFIER_VALUE = "^[a-zA-Z]([a-z|A-Z|0-9])*$"

IDENTIFIER = "ID"
CONSTANT = "CONST"

class Scanner: 
    def __init__(self):
        self.__symbol_table = SymbolTable()
        self.__pif = []

    def pif_insert(self, token, index):
        self.__pif.append((token, index))

    def check_reserved_word(token):
        return RESERVED_WORDS.__contains__(token)
    
    def check_separator(token):
        return SEPARATORS.__contains__(token)

    def check_operator(token):
        return OPERATORS.__contains__(token)

    def check_identifier(token):
        return bool(re.match(IDENTIFIER_VALUE, token))

    def check_constant(token):
        return bool(re.match(NUMERIC_VALUE, token)) or bool(re.match(STRING_VALUE, token)) or bool(re.match(BOOLEAN_VALUE, token))

    def __print_lexical_error(line, token):
        print('Lexical error at' + str(line) + ", token: ", token)

    def __get_operator(self, line, index):
        operator = line[index] + line[index + 1]
        if self.check_operator(operator):
            return operator
        return line[index]

    

    