# -*- encondig: utf-8 -*-

# --------------------------------------
# c minus lexer
# --------------------------------------

# NEW: 	comments in classic C
# 		comentario in C99 standard

import ply.lex as lex

# list of tokens
tokens = (

	# Reserverd words
	'ELSE',
	'IF',
	'INT',
	'RETURN',
	'VOID',
	'WHILE',
	
	# Symbols
	'MAS',
	'MENOS',
	'POR',
	'ENTRE',
	'MENOR_QUE',
	'MENORIGUAL',
	'MAYOR_QUE',
	'MAYORIGUAL',
	'IGUAL',
	'DESIGUAL',
	'DISTINTO',
	'PUNTO_Y_COMA',
	'COMA',
	'LPAREN',
	'RPAREN',
	'LLAVE_IZQ',
	'LLAVE_DER',
	'CORCH_IZQ',
	'CORCH_DER',

	# Others	
	'ID', 
	'NUMBER',
)

# Regular expressions rules for a simple tokens
t_MAS 	 = r'\+'
t_MENOS	 = r'-'
t_POR  = r'\*'
t_ENTRE = r'/'
t_IGUAL  = r'='
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_PUNTO_Y_COMA = ';'
t_COMA	 = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LLAVE_IZQ = r'\['
t_LLAVE_DER = r'\]'
t_CORCH_IZQ   = r'{'
t_CORCH_DER   = r'}'

def t_ELSE(t):
	r'else'
	return t

def t_IF(t):
	r'if'
	return t

def t_INT(t):
	r'int'
	return t
	
def t_RETURN(t):
	r'return'
	return t
	
def t_VOID(t):
	r'void'
	return t
	
def t_WHILE(t):
	r'while'
	return t
	
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_ID(t):
	r'\w+(_\d\w)*'
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'=='
	return t

def t_DISTINT(t):
	r'!='
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
	r'//(.)*?\n'
	t.lexer.lineno += 1

def t_error(t):
	print "Lexical error: " + str(t.value[0])
	t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print tok

lexer = lex.lex()

# Test 
if __name__ == '__main__':

	# Test
	data = '''
		/* comentario
   			de varias lineas
		*/
		void main (int argc) {
			int a;
			a = 10;
			// Esto es otro comentario
			return 0;
		}
	'''

	# Build lexer and try on
	lexer.input(data)
	test(data, lexer)
	
	raw_input("Pulse una tecla para continuar")

