#
#   Chromatin
# a sprite that represents a Chromatin
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet

# froms


# class imports
from ui.pushablesprite import PushableSprite

# 
#   CLASS
# 

# constants

# definition
class Chromatin(cocos.layer.ScrollableLayer):

# init
    def __init__(self, tmxObj, collision_layers):

        super().__init__()
        self.spr = PushableSprite(tmxObj, "chromatin", collision_layers, frames=1)

        self.add(self.spr)

# setters/getters

# methods