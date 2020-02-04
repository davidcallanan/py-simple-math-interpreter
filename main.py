from lexer import Lexer
from parser_ import Parser

while True:
	try:
		text = input("calc > ")
		lexer = Lexer(text)
		tokens = lexer.generate_tokens()
		parser = Parser(tokens)
		tree = parser.parse()
		print(tree)
	except Exception as e:
		print(e)
