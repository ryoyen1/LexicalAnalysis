from sly import Lexer

class simpleLexer(Lexer):
    tokens = { PHP, ECHO, FUNCTION, IF, STRING,
               NAME, CLASS , NUMBER , PLUS , MINUS,
               DIVIDE, MULTI, EQUAL, LPAREN, RPAREN}
    ignore = ' \t'

    #Operators
    symbol = {'(', ')', '{' ,'}', ',', ';'}

    #Tokens
    # NUMBER = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    MULTI = r'\*'
    DIVIDE = r'/'
    EQUAL = r'='

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NAME['class'] = CLASS
    NAME['if'] = IF
    NAME['function'] = FUNCTION
    NAME['echo'] = ECHO
    # NAME['<?php'] = PHP

    STRING = r'\".*?\"'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')


# data = '''<?php
#           class MyClass {
#             function abc(){ $i=5;
#             $z=$i*2;
#             echo "One '$=".$z;}
#           }
#           ?>'''

data = '''
ryo
is
while
test
if
echo'''

lexer = simpleLexer()
for tok in lexer.tokenize(data):
    print(tok)





# for i, char in enumerate(data):
#     if char != space:
#         lexeme += char
#     if (i+1 < len(data)):
#         if(data[i+1] == space):
#             if lexeme != '':
#                 print(lexeme.replace('\n','<newline>'))
#                 lexeme = ""


