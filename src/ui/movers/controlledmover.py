#
#   Sprite Mover
# moves the sprite
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import _thread
import time

# froms
from pyglet.window import key
from cocos.actions import *
from cocos import mapcolliders


# 
#   CLASS
# 

# global
# constants

TERRAIN_RECTANGLES = 0
INTERACTION_BLOCKS = 1

# for Velocity List
XVELOCITY = 0
YVELOCITY = 1

class KeyMove(cocos.actions.Move):

    def __init__(self, width, height, doesCollide):
        super().__init__(width, height)
        self.doesCollide = doesCollide
    
    def step(self, dt):

        # super(KeyMove, self).step(dt)

        # catches the keyboard movements
        xvel = ((key.D in keys) - (key.A in keys)) * 5
        yvel = ((key.W in keys) - (key.S in keys)) * 3

        # print((key.W in keys) - (key.S in keys))

        if(self.doesCollide):


            last = self.target.get_rect()

            new = last.copy()
            new.x += xvel
            new.y += yvel


            for ch in self.target.collision_handlers:

                # if the collision handler is for terrain, it will have an effect on the velocity of the object
                if ch.id == TERRAIN_RECTANGLES:
                    self.target.velocity = ch(last, new, xvel, yvel)

                
                # if the col_handler is for interaction blocks, it will still return the fact that the target hit the block
                elif ch.id == INTERACTION_BLOCKS:

                    cp_new = new.copy()

                    ch(last, cp_new, xvel, yvel)

            self.target.position = new.center

            scrl.set_focus(*self.target.position)

        else:

            # this is used in finding the position that is best for the sprite
            xvel = ((key.RIGHT in keys) - (key.LEFT in keys)) 
            yvel = ((key.UP in keys) - (key.DOWN in keys)) 
            self.target.velocity = (xvel, yvel)
            # print(self.target.position)

        # print(self.target.velocity)


# definition
class ControlledMover(cocos.layer.Layer):

    is_event_handler = True

# init
    def __init__(self, target, scroller, doesCollide):
        global scrl, keys

        super(ControlledMover, self).__init__()

        keys = set()
        scrl = 0
        
        # target.reset()
        self.target = target
        scrl = scroller

        self.target.do(KeyMove(1920,1080, doesCollide))

    def on_key_press(self, k, modifiers):
        global keys
        keys.add(k)

        self.target.setSprite((
            'left' if k == key.A else
            'right' if k == key.D else
            'up' if k == key.W else
            'down' if k == key.S else 'none'
            ))
        # print(keys)

    def on_key_release(self, key, modifiers):
        global keys
        keys.remove(key)

        self.target.setSprite(('static' if len(keys) == 0 else 'none'))

        # print(keys)

# setters/getters

# methods