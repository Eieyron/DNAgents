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
class CrackLayer(cocos.layer.Layer):

# init
	def __init__(self, x_pos, y_pos):
		super(CrackLayer, self).__init__()

		self.x_pos = x_pos
		self.y_pos = y_pos

		#just for init
		# init = pyglet.image.load('../res/helicase/crack.png')
		# self.crack = cocos.sprite.Sprite(init, position=(self.x_pos, self.y_pos))
		# self.add(self.crack)

# setters/getters

# methods
	def add_crack(self, x_pos, y_pos, crack_count):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.crack_count = crack_count

		#print('crack')
		init = pyglet.image.load('../res/helicase/punch.png')
		if self.crack_count == 0:
			self.crack1 = cocos.sprite.Sprite(init, position=(self.x_pos, self.y_pos))
			self.add(self.crack1)
		elif self.crack_count == 1:
			self.crack2 = cocos.sprite.Sprite(init, position=(self.x_pos, self.y_pos))
			self.add(self.crack2)
		else:
			self.crack3 = cocos.sprite.Sprite(init, position=(self.x_pos, self.y_pos))
			self.add(self.crack3)

	def remove_cracks(self):
		self.remove(self.crack1)
		self.remove(self.crack2)
		self.remove(self.crack3)



