import random

class MarkovChain:
	def __init__(self, lengths):
		self.lengths = []
		self.chains = {}
		for length in self.lengths:
			self.chains[length] = {}
	
	def add_to_chain(self, key, item):
		for length in self.lengths:
			node = self.chains[length].get(key[-length:], {})
			frequency = node.get(item, 0)
			
			node[item] = frequency+1
			self.chains[length][key[-length:] = node
	
	def generate(self, level, length):
		chain = self.chains[level]
		generated = random.choice(chain.items())
		while len(generated) < length:
			biggest = {'':0}
			for n in chain[generated[-level:]]:
				if n[1] > biggest[1]:
					biggest = n
					

def generateChain_fromText(text, chain_lengths):
	chain = MarkovChain(chain_lengths)
	buffer = ''
	for char in text:
		if len(buffer) < max(chain_lengths):
			buffer += char
			continue
		chain.add_to_chain(buffer, char)
	return chain
			

def generateText(chain, length):
	text = random.choice(chain.keys())
	while len(text) < length:
		