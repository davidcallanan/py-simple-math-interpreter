import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):

	def test_empty(self):
		tokens = []
		node = Parser(tokens).parse()
		self.assertEqual(node, None)

	def test_number_node(self):
		tokens = [Token(TokenType.NUMBER, 51.2)]
		node = Parser(tokens).parse()
		self.assertIsInstance(node, NumberNode)
		self.assertEqual(node.value, 51.2)

	def test_operator_nodes(self):
		tokens = [Token(TokenType.NUMBER, 27), Token(TokenType.PLUS), Token(TokenType.NUMBER, 14)]
		node = Parser(tokens).parse()
		self.assertIsInstance(node, AddNode)
		self.assertIsInstance(node.node_a, NumberNode)
		self.assertIsInstance(node.node_b, NumberNode)
		self.assertEqual(node.node_a.value, 27)
		self.assertEqual(node.node_b.value, 14)
		
		tokens = [Token(TokenType.NUMBER, 27), Token(TokenType.MINUS), Token(TokenType.NUMBER, 14)]
		node = Parser(tokens).parse()
		self.assertIsInstance(node, SubtractNode)
		self.assertIsInstance(node.node_a, NumberNode)
		self.assertIsInstance(node.node_b, NumberNode)
		self.assertEqual(node.node_a.value, 27)
		self.assertEqual(node.node_b.value, 14)
		
		tokens = [Token(TokenType.NUMBER, 27), Token(TokenType.MULTIPLY), Token(TokenType.NUMBER, 14)]
		node = Parser(tokens).parse()
		self.assertIsInstance(node, MultiplyNode)
		self.assertIsInstance(node.node_a, NumberNode)
		self.assertIsInstance(node.node_b, NumberNode)
		self.assertEqual(node.node_a.value, 27)
		self.assertEqual(node.node_b.value, 14)
		
		tokens = [Token(TokenType.NUMBER, 27), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 14)]
		node = Parser(tokens).parse()
		self.assertIsInstance(node, DivideNode)
		self.assertIsInstance(node.node_a, NumberNode)
		self.assertIsInstance(node.node_b, NumberNode)
		self.assertEqual(node.node_a.value, 27)
		self.assertEqual(node.node_b.value, 14)

	def test_full_expression(self):
		tokens = [
			Token(TokenType.NUMBER, 27),
			Token(TokenType.PLUS),
			Token(TokenType.LPAREN),
			Token(TokenType.NUMBER, 43),
			Token(TokenType.DIVIDE),
			Token(TokenType.NUMBER, 36),
			Token(TokenType.MINUS),
			Token(TokenType.NUMBER, 48),
			Token(TokenType.RPAREN),
			Token(TokenType.MULTIPLY),
			Token(TokenType.NUMBER, 51),
		]

		node = Parser(tokens).parse()
		self.assertIsInstance(node, AddNode)
		self.assertIsInstance(node.node_a, NumberNode)
		self.assertEqual(node.node_a.value, 27)
		self.assertIsInstance(node.node_b, MultiplyNode)
		self.assertIsInstance(node.node_b.node_a, SubtractNode)
		self.assertIsInstance(node.node_b.node_a.node_a, DivideNode)
		self.assertIsInstance(node.node_b.node_a.node_a.node_a, NumberNode)
		self.assertEqual(node.node_b.node_a.node_a.node_a.value, 43)
		self.assertIsInstance(node.node_b.node_a.node_a.node_b, NumberNode)
		self.assertEqual(node.node_b.node_a.node_a.node_b.value, 36)
		self.assertIsInstance(node.node_b.node_a.node_b, NumberNode)
		self.assertEqual(node.node_b.node_a.node_b.value, 48)
		self.assertIsInstance(node.node_b.node_b, NumberNode)
		self.assertEqual(node.node_b.node_b.value, 51)

		# TODO: check syntax errors
