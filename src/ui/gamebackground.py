#
#   Game Background
# a 1920x1080 scrollable layer background
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
class GameBackground(cocos.layer.ScrollableLayer):

# init
	def __init__(self, picDir):
		super(GameBackground, self).__init__()

		img = pyglet.image.load(picDir)
		self.bg = cocos.sprite.Sprite(img, position=(img.width/2,img.height/2))

		self.px_width = img.width
		self.px_height = img.height

		self.bg_center = (img.width/2, img.height/2)
		print(self.bg_center)

		self.add(self.bg)


# setters/getters

# methods
	def set_background(self, background):
		backgrd = '../res/main_game_backgrounds/DNA '
		self.bg.image = pyglet.image.load(backgrd + str(background) + '.png')
		# print(backgrd)