# MainMenu.py

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import _thread as th
import time
import random

# class imports
from ui.button import Button
from ui.helicase_background import HelicaseBackground
from ui.crackable_button import CrackButton
from ui.crack_layer import CrackLayer

#
#   CLASS
#


# definition

class HelicaseMinigame(cocos.scene.Scene):

# init

	def __init__(self, director):

		super().__init__()

		self.director = director

		self.bases = ['A', 'C', 'T' ,'G', 'A']
		self.base = 0
		self.crack_layer = CrackLayer(2000, 2000)
		self.count = 0
		self.crack_flag = False

		self.background = HelicaseBackground(self.bases, self.base)

		self.add(self.background, z=0)
		self.add(self.crack_layer, z=1)

		self.crack_buttons()


# methods
	def initiate_crack_button(self):
		th.start_new_thread(self.init_crack_button, ())

	def init_crack_button(self):
		if self.crack_flag == False:
			time.sleep(3)
			self.x_pos = random.randint(200, 1080)
			self.y_pos = random.randint(200, 520)
			print('WEWEWEW')
			self.crack_button = CrackButton(self.x_pos, self.y_pos, '../res/helicase/ekis.png', self, self.make_crack)
			self.add(self.crack_button, z=1)
			self.crack_flag = True


	def crack_buttons(self):
		if self.base < (len(self.bases)-1):
			if self.count < 3:
				#self.initiate_crack_button()
				# print(self.count)
				if self.crack_flag == False:
					#time.sleep(3)
					self.x_pos = random.randint(200, 1080)
					self.y_pos = random.randint(200, 520)
					self.crack_button = CrackButton(self.x_pos, self.y_pos, '../res/helicase/ekis.png', self, self.make_crack)
					#print('WEWEWEW')
					self.add(self.crack_button, z=1)
					self.crack_flag = True
			else:
				self.count = 0
				self.base += 1
				#print(self.base)
				self.fix_background()
				self.crack_buttons()
		else:
			print('DOOOOONNNNEEE')
			self.director.pop()

	def fix_background(self):
		self.crack_layer.remove_cracks()
		self.background.set_background(self.base)
		

	def make_crack(self):
		self.crack_layer.add_crack(self.x_pos, self.y_pos, self.count)
		#######################################
		self.count += 1
		self.crack_flag = False
		self.remove(self.crack_button)
		self.crack_buttons()


