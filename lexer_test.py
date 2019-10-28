import unittest
from tokens import Token, TokenType
from lexer import Lexer

class TestLexer(unittest.TestCase):

	def test_numbers(self):
		tokens = list(Lexer("123").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.NUMBER, 123.000), Token(TokenType.EOF)])

		tokens = list(Lexer("123.456").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.NUMBER, 123.456), Token(TokenType.EOF)])

		tokens = list(Lexer("123.").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.NUMBER, 123.000), Token(TokenType.EOF)])
		
		tokens = list(Lexer(".456").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.NUMBER, 000.456), Token(TokenType.EOF)])

	def test_operators(self):
		tokens = list(Lexer("+").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.PLUS), Token(TokenType.EOF)])

		tokens = list(Lexer("-").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.MINUS), Token(TokenType.EOF)])
	
		tokens = list(Lexer("*").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.MULTIPLY), Token(TokenType.EOF)])
	
		tokens = list(Lexer("/").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.DIVIDE), Token(TokenType.EOF)])

	def test_whitespace(self):
		tokens = list(Lexer(" \t\n  \t\t\n\n").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.EOF)])

	def test_illegal_characters(self):
		tokens = list(Lexer("!£$%^&*()").generate_tokens())
		self.assertEqual(tokens, [])

		tokens = list(Lexer("123, !£$%^&*()").generate_tokens())
		self.assertEqual(tokens, [Token(TokenType.NUMBER, 123)])

		tokens = list(Lexer("!£$%^&*() 123").generate_tokens())
		self.assertEqual(tokens, [])
	
	def test_all(self):
		tokens = list(Lexer("27 + 43 / 36 - 48 * 51 $").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.NUMBER, 27),
			Token(TokenType.PLUS),
			Token(TokenType.NUMBER, 43),
			Token(TokenType.DIVIDE),
			Token(TokenType.NUMBER, 36),
			Token(TokenType.MINUS),
			Token(TokenType.NUMBER, 48),
			Token(TokenType.MULTIPLY),
			Token(TokenType.NUMBER, 51)
		])
