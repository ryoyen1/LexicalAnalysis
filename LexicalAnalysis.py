from sly import Lexer

class simpleLexer(Lexer):
    tokens = { STRING, NAME, CLASS , NUMBER , PLUS , MINUS, DIVIDE, MULTI, EQUAL, LPAREN, RPAREN}
    ignore = '\t'

    #Operators
    symbol = { '=', '+', '-', '/', '*', '(', ')', '{' ,'}', ',', ';'}

    #Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    CLASS = r'CLASS'
    STRING = r'\".*?\"'


column = 0
line = 1

data = '''<?php
          class MyClass {
            function abc(){ $i=5;
            $z=$i*2;
            echo "One '$=".$z;}
          }
          ?>'''

space = " "
lexeme = ''

@_('r\d+')
def NUMBER(self, t):
    t.value = int(t.value)
    return t


# for i, char in enumerate(data):
#     if char != space:
#         lexeme += char
#     if (i+1 < len(data)):
#         if(data[i+1] == space):
#             if lexeme != '':
#                 print(lexeme.replace('\n','<newline>'))
#                 lexeme = ""

print(lexeme)
