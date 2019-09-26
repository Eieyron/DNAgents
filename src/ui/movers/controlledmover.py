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
GRAVITY = -500

# constants

TERRAIN_RECTANGLES = 0
INTERACTION_BLOCKS = 1

# for Velocity List
XVELOCITY = 0
YVELOCITY = 1

class KeyMove(cocos.actions.WrappedMove):

    def __init__(self, width, height, doesCollide):
        super().__init__(width, height)
        self.doesCollide = doesCollide
    
    def step(self, dt):

        # catches the keyboard movements
        xvel = ((key.D in keys) - (key.A in keys)) * 500
        yvel = 1

        if(self.doesCollide):


            if key.SPACE in keys:

                if not self.target.jumping and self.target.onground:
                    self.target.jumping = True
                    self.target.y_anchor = self.target.y+180

                if self.target.y >= self.target.y_anchor:
                    # if the anchor is reached
                    self.target.jumping = False
                
                if self.target.jumping and self.target.y < self.target.y_anchor:
                    # while still jumping, add yvelocity
                    yvel += 2000

                self.target.setStatic(0)


            if not self.target.mapcolliders[TERRAIN_RECTANGLES].bumped_y:
                # if falling
                self.target.setStatic(0)

            yvel += GRAVITY
            dx = xvel * dt
            dy = yvel * dt

            last = self.target.get_rect()

            new = last.copy()
            new.x += dx
            new.y += dy


            for ch in self.target.collision_handlers:

                # if the collision handler is for terrain, it will have an effect on the velocity of the object
                if ch.id == TERRAIN_RECTANGLES:
                    self.target.velocity = ch(last, new, xvel, yvel)

                
                # if the col_handler is for interaction blocks, it will still return the fact that the target hit the block
                elif ch.id == INTERACTION_BLOCKS:

                    cp_new = new.copy()

                    ch(last, cp_new, xvel, yvel)

            # WRAP algorithm
            x, y = new.center
            w, h = self.target.width, self.target.height
            # XXX assumes center anchor
            if x > self.width + w/2:
                x -= self.width + w
            elif x < 0 - w/2:
                x += self.width + w
            if y > self.height + h/2:
                y -= self.height + h
            elif y < 0 - h/2:
                y += self.height + h
            self.target.position = (x, y)

            scrl.set_focus(*self.target.position)

        else:

            # this is used in finding the position that is best for the sprite
            xvel = ((key.RIGHT in keys) - (key.LEFT in keys)) 
            yvel = ((key.UP in keys) - (key.DOWN in keys)) 
            self.target.velocity = (xvel, yvel)
            print(self.target.position)

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

    def on_key_press(self, key, modifiers):
        global keys
        keys.add(key)

        # print(keys)

    def on_key_release(self, key, modifiers):
        global keys
        keys.remove(key)

        # print(keys)

# setters/getters

# methods