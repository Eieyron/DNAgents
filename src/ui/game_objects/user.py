#
#   User
# a sprite that represents the user, it can be added in a scene/layer and will move accordingly
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet

# froms


# class imports
from ui.movingsprite import MovingSprite

# 
#   CLASS
# 

# constants

# definition
class User(cocos.layer.ScrollableLayer):


# init
    def __init__(self, x,y, picDir, collision_layers):

        super().__init__()
        self.spr = MovingSprite((x,y), picDir, collision_layers)

        self.has_information_layer = False

        self.add(self.spr)

# setters/getters
    



# methods
