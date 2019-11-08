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

		self.animate_separation()

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
	
	def animate_separation(self):
		prev_base = self.bases[self.base-1]

		if prev_base == 'A':
			initLeft = pyglet.image.load('../res/helicase/left A.png')
			initRight = pyglet.image.load('../res/helicase/right T.png')
		elif prev_base == 'C':
			initLeft = pyglet.image.load('../res/helicase/left C.png')
			initRight = pyglet.image.load('../res/helicase/right G.png')
		elif prev_base == 'T':
			initLeft = pyglet.image.load('../res/helicase/left T.png')
			initRight = pyglet.image.load('../res/helicase/right A.png')
		else:
			initLeft = pyglet.image.load('../res/helicase/left G.png')
			initRight = pyglet.image.load('../res/helicase/right C.png')

		self.left = cocos.sprite.Sprite(initLeft, position=(640, 360))
		self.right = cocos.sprite.Sprite(initRight, position=(640, 360))

		self.add(self.left)
		self.add(self.right)

		self.separate_right()
		self.separate_left()

	def separate_right(self):
		self.right.velocity = (700, 0)
		self.right.do(cocos.actions.move_actions.Move())
	
	def separate_left(self):
		self.left.velocity = (-700, 0)
		self.left.do(cocos.actions.move_actions.Move())
