#utf-8


class Fuzzy:
	def __init__(self,initvalue):
		self.value = initvalue
		
	def max(self):
	'''Max value of fuzzy set'''
		pass
		
	def min(self):
	'''Min value of fuzzy set'''
		pass
		
	def middle(self):
	'''Middle value of fuzzy set'''
		pass
		
	def __add__(self,other):
	'''Fuzzyset1 + Fuzzyset2'''
		pass
	
	def __sub__(self,other):
	'''Fuzzyset1 - Fuzzyset2'''
		pass
		
	def __mult__(self,other):
	'''Fuzzyset1 * Fuzzyset2'''
		pass
		
	def __lt__(self,other):
	'''Fuzzyset1 > Fuzzyset2'''
		pass
	def __le__(self,other):
	'''Fuzzyset1 <= Fuzzyset2'''
		pass
	def __eq__(self,other):
	'''Fuzzyset1 == Fuzzyset2'''
		pass
	def __ne__(self,other):
	'''Fuzzyset1 != Fuzzyset2'''
		pass
	def __gt__(self,other):
	'''Fuzzyset1 > Fuzzyset2'''
		pass
	def __ge__(self,other):
	'''Fuzzyset1 >= Fuzzyset2'''
		pass
	
	def __repr__(self):
		return f"Fuzzy number {self.vatue.values()}"
	
