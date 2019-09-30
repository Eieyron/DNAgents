#
#   Protein
# a sprite that represents a Protein, vanishes if touched by the user
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet

# froms


# class imports
from ui.vanishingsprite import VanishingSprite

# 
#   CLASS
# 

# constants

# definition
class Protein(cocos.layer.ScrollableLayer):

# init
	def __init__(self, parent, tmxObj, objName):

		self.parent = parent

		super().__init__()
		self.spr = VanishingSprite(parent, tmxObj, objName, 8)

		self.add(self.spr)

# setters/getters

# methods
	def vanish(self):
		self.spr.vanish()