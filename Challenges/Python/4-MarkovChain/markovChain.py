
def generateChain(text, chain_length=2):
	chain = {}
	buffer = ''
	for char in text:
		if len(buffer) < chain_length:
			buffer += char
			continue
			
		node = chain.get(buffer, {})
		cell = node.get(char, 0)
		
		node[char] = cell+1
		chain[buffer] = node
		
		buffer = buffer[1:] + char
	return chain