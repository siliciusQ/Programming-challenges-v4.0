import random

class NGram:
	def __init__(self, order):
		self.order = order
		self.ngram = {}
	
	def feed(self, sequence):
		for offset in range(len(sequence)-offset):
			key = sequence[offset:offset+self.order]
			item = sequence[offset+self.order]
			self.add(key, item)
	
	def add(self, key, item):
		node = self.ngram.get(key, {})
		counter = node.get(item, 0)
		
		node[item] = counter + 1
		self.ngram[key] = node
	
	def walk(self, steps):
		list_= self.get_seed()
		
	
	def get_seed(self):
		list_ = self.ngram.keys()
		return list(list_)
		
with open('test.txt', 'r') as file:
	text = file.read()

chain = NGram(2)
chain.feed(text)
print(chain.walk(10))
	