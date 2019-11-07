#
# Player Profile
# a class that has file reading and writing capabilities and handles what state in the game the user is in currently
#

#
#   IMPORT STATEMENTS
#

# imports
import json

# froms

# class imports

# 
#   CLASS
# 

# constants

# definition

class Profile():
	
	"""docstring for Profile"""
	
	def __init__(self, *args, **kwargs):
		# 1st arg should be name
		# 2nd arg should be inventory
		
		if 'information' in kwargs.keys(): 	# information is passed as the newly read json file 
			
			self.information = kwargs['information']

		else:								# else means that the initialization has 

			# self dictionary for easy data storage and collection
			self.information = {
				'case': 1,
				'problems': [False],
				'minigame': 'helicase'
			}

# init

# setters/getters

# methods

	def get_serializable_information(self):

		return {
			'case' : self.information['case'],
			'problems' : self.information['problems'],
			'minigame': self.information['minigame']
		}

	def save(self, saveDir):

		with open(saveDir, 'w') as fp:
			json.dump(self.get_serializable_information(), fp)

	def print_self(self):
		print(self.__dict__)

	def set_inventory(self, inventory_contents):
		self.information['inventory'] = inventory_contents

	def get_inventory(self):
		return self.information['inventory']

	def get_cutscenes_watched(self):
		return self.information['cutscenes_watched']

	def set_skippable(self, number):
		self.information['cutscenes_watched'][number-1] = True

	def finished(self, phasename):
		self.information['finished_levels'][phasename] = True

	def is_finished(self, phasename):
		return self.information['finished_levels'][phasename]

	@classmethod
	def read_save(cls, saveDir):

		# binary_file = open(saveDir, mode='wb')
		# serialized = pickle.dump(self, binary_file)
		# binary_file.close()
		# pass

		with open(saveDir) as json_file:
			data = json.load(json_file)
			
			# print(data['inventory'])
			# print(data)

			return cls(information=data)





#
#   MAIN
#
