#
# [lexer.py]
#
# The lexer for Ergonomica.
#

import ply.lex as lex

tokens = (
    'ARGARRAY',
    'LITERAL',
    'PIPE',
    'INT',
    'STRING',
    'COMMENT',
    'NEWLINE',
    'DEFINITION',
    'END',
    'SUBSTITUTION',
)

t_NEWLINE  = r'\n+'
t_PIPE = r'->'
t_ignore = ' \t'

def t_LITERAL(t):
    r'[a-z_]+'
    if t.value == "def":
        t.type = 'DEFINITION'
    elif t.value == "end":
        t.type = 'END'
    elif "_" in t.value:
        t.type = 'SUBSTITUTION'
    return t
        

def t_ARGARRAY(t):
    r'\[.*?\]'
    t.value = t.value[1:-1].split()
    return t
    
def t_STRING(t):
    r'".*"'
    t.value = t.value[1:-1]
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):

    print(t.value)
    t.lexer.skip(1)

lexer = lex.lex(optimize=1)

def tokenize(string):

    tokens = []
    lexer.input(string)
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens
    
