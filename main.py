from lexer import Lexer

while True:
	text = input("calc > ")
	lexer = Lexer(text)
	print(list(lexer.generate_tokens()))
