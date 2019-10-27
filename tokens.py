from enum import Enum

class Token:
	def __init__(self, type, value=None):
		self.type = type
		self.value = value
	
	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")

class TokenType(Enum):
	NUMBER = 0
	PLUS = 1
	MINUS = 2
	MULTIPLY = 3
	DIVIDE = 4
