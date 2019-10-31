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
		self.left = cocos.sprite.Sprite(self.initLeft, position=(320, 360))
		self.right = cocos.sprite.Sprite(self.initRight, position=(960, 360))

		self.add(self.left)
		self.add(self.right)


# setters/getters

# methods
	def set_background(self, base):
		self.base = base

		self.set_bases()
		self.left.image = self.initLeft
		self.right.image = self.initRight

	def set_bases(self):
		current_base = self.bases[self.base]

		self.initLeft = pyglet.image.load('../res/helicase/'+ current_base +'.png')
		if current_base == 'A':
			self.initRight = pyglet.image.load('../res/helicase/T.png')
		elif current_base == 'C':
			self.initRight = pyglet.image.load('../res/helicase/G.png')
		elif current_base == 'T':
			self.initRight = pyglet.image.load('../res/helicase/A.png')
		else:
			self.initRight = pyglet.image.load('../res/helicase/C.png')
		