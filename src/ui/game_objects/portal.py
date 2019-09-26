#
#   Portal
# a sprite that represents a portal
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
class Portal(cocos.layer.ScrollableLayer):

# init
    def __init__(self, x,y, objName):

        super().__init__()
        self.spr = StaticSprite((x,y), objName, 8)

        self.add(self.spr)

# setters/getters

# methods