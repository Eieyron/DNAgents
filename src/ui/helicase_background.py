#
#   Game Background
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet

# froms

# class imports

# 
#   CLASS
# 

# definition
class HelicaseBackground(cocos.layer.Layer):

# init
	def __init__(self, bases, base):
		super(HelicaseBackground, self).__init__()

		self.bases = bases
		self.base = base

		self.set_bases()
		self.background = cocos.sprite.Sprite(self.initBackground, position=(640, 360))
		
		self.add(self.background)

# setters/getters

# methods
	def set_background(self, base):
		self.base = base

		self.set_bases()
		self.background.image = self.initBackground

	def set_bases(self):
		current_base = self.bases[self.base]

		if current_base == 'A':
			self.initBackground = pyglet.image.load('../res/helicase/block_AT.png')
		elif current_base == 'C':
			self.initBackground = pyglet.image.load('../res/helicase/block_CG.png')
		elif current_base == 'T':
			self.initBackground = pyglet.image.load('../res/helicase/block_TA.png')
		else:
			self.initBackground = pyglet.image.load('../res/helicase/block_GC.png')
		