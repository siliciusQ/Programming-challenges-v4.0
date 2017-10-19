import random

class MarkovChain:
	def __init__(self, level):
		self.level = level
		self.chain = {}
	
	def add_to(self, key, succ):
		if len(key) < self.level:
			raise ValueError("To short key for chain! [ {} ]".format(key))
		
		node = self.chain.get(key, {})
		cell = node.get(succ, 0)
		node[succ] = cell+1
		self.chain[key] = node
	
	def get_seed(self):
		return random.choice(list(self.chain))
	
	def get_random_from(self, key):
		pairs = list(self.chain[key].items())
		probs = [x[1] for x in pairs]
		return random.choices(pairs, probs, k=1)[0][0]

		
def generateChainFromText(text, level):
	chain = MarkovChain(level)
	for offset in range(len(text)-level-1):
		key = text[offset:offset+level]
		succ = text[offset+level+1]
		chain.add_to(key, succ)
	return chain

def generateTextFromChain(chain, length, seed=None):
	text = seed or chain.get_seed()
	while len(text) < length:
		text += chain.get_random_from(text[-chain.level:])
	return text

		
if __name__ == '__main__':
	with open('test.txt', 'r') as file:
		chain = generateChainFromText(file.read(), 6)
	print(generateTextFromChain(chain, 50))
	