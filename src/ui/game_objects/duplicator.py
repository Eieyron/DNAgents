#
#   Duplicator
# a sprite that represents a duplicator, it is a static sprite that when hit, duplicates(changes) the sprite of the sprite hit
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet

# froms


# class imports
from ui.staticsprite import StaticSprite

# 
#   CLASS
# 

# constants

# definition
class Duplicator(cocos.layer.ScrollableLayer):


# init
    def __init__(self, x,y, objName):

        super().__init__()
        self.spr = StaticSprite((x,y), objName, 8)

        self.add(self.spr)

# setters/getters
    



# methods
