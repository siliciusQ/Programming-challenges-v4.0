class Challenge: 
	def __init__(self):
		self._main_description = ''
		self._bonus_text = ''
		self._difficulity = ''
		self._category = ''


	def description(self):
		return self._main_description


	def set_description(self, description):
		self._main_description = description

	def set_bonus_text(self, bonus_text):
		self._bonus_text = bonus_text

	def set_difficulity(self, difficulity):
		self._difficulity = difficulity

	def set_category(self, category):
		self._category = category





class ChallengeList:
	def __init__(self):
		self._challenges = {}

	def add_challenge(self, pos: int, chg: Challenge):
		if not self._challenges.get(pos, False):
			self._challenges[pos] = chg

	def get_challenge(self, pos: int) -> Challenge:
		return self._challenges[pos]


	def load_from_chl(self, file_path: str):
		"""Load *.chl to object.
		"""

		# First, read lines from file
		with open(file_path, 'r') as file:
			lines = file.readlines()

		#
		current_difficulity = None
		category_declarations = []
		last_challenge = None
		created_chalenges = {}

		# Then loop trough and iterpret them
		for line in lines:
			if not line.strip():	# Line is empty  
				continue

			elif line.startswith('$'):
				# Save category declaration for later (without '$')  
				category_declarations.append(line[1:])
				continue

			elif line.startswith('@'):
				# New difficulity was declared, so change (without '@')  
				current_difficulity = line[1:]
				continue
			
			elif line.startswith('#'):
				# Add bonus text to last challenge (without '#\t')  
				last_challenge.set_bonus_text(line.strip('#\t'))
				continue

			# So it's must be a line wchich starting with number (challenge)  
			
			# get number and rest of the challenge  
			line_tokens = line.split(None, 1)
			number = int(line_tokens[0])	# assumption that it's number  
			text = line_tokens[1]

			#create challenge and feed with data  
			challenge = Challenge()
			challenge.set_description(text)
			challenge.set_difficulity(current_difficulity)
			#set last challenge  
			last_challenge = challenge
			#add to list
			self.add_challenge(number, challenge)

		# Now do something usefull with category declarations.  
		# Loop trough all, ad apply them to challenges created before  
		for category_declaration in category_declarations:
			# tokenize declaration
			tokens = category_declaration.split(':')
			category_name = tokens[0].strip()
			category_ranges = [x.strip() for x in tokens[1].split(',')]
			# apply category in given ranges
			for range_ in category_ranges:
				start, end = map(int, range_.split('-'))
				for x in range(start, end+1):
					chg = self.get_challenge(x)
					chg.set_category(category_name)




if __name__ == '__main__':
	c = ChallengeList()
	c.load_from_chl('challenges_list.txt')