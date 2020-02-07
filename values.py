from dataclasses import dataclass

@dataclass
class Number:
	value: any
	
	def __repr__(self):
		return f"{self.value}"
