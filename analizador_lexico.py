import ply.lex as lex

# Palabras reservadas
reserved = {
    'using':'USING',
    'namespace': 'NAMESPACE',
    'class': 'CLASS',
    'static':'STATIC',
    'void':'VOID',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'print': 'PRINT',
    'println': 'PRINTLN',
    'object': 'OBJECT',
    'def': 'DEF',
    'Array': 'ARRAY',
    'string': 'STRING_TYPE', 
    'Unit': 'UNIT',
    'Main':'MAIN',
    'args':'ARGS',
    'System':'SYSTEM',
    'Console':'CONSOLE',
    'WriteLine':'WRITELINE'
}

tokens = [
    'PLUS', 
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN', 
    'RPAREN', 
    'LBRACE', 
    'RBRACE',
    'SEMICOLON', 
    'COLON',
    'ID', 
    'NUMBER', 
    'STRING_LITERAL',
    'EQUALS', 
    'COMMA', 
    'DOT', 
    'LEFT_BRACKET',
     'RIGHT_BRACKET'
   

] + list(reserved.values())

# Definición de tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'
t_EQUALS = r'='
t_COMMA = r','
t_DOT = r'\.'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'




def reset_lexer():
    global line_counter
    line_counter = 1


t_ignore  = ' \t'
    
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()