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
        bg = cocos.sprite.Sprite(img, position=(img.width/2,img.height/2))

        self.px_width = img.width
        self.px_height = img.height

        self.add(bg)
        

# setters/getters

# methods
