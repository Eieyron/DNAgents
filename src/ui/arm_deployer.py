#
#   BUTTON
# An abstraction of a button where you can change the 
#   button position
#   hover sprite
#   action  
#

#
#   IMPORT STATEMENTS
#

# imports

import cocos
import pyglet
import copy
import _thread as th
import os

# froms
from cocos.actions import *
from pyglet.window import key


# 
#   CLASS
# 

# constants

# definition

class Arm_Deployer(cocos.layer.Layer):

    is_event_handler = True

    # init

    def __init__(self,  parent, action):
        self.parent = parent
        self.action = action

        super().__init__()

        self.ua = pyglet.image.load('../res/minigame1/upright_arms.png')
        self.sa = pyglet.image.load('../res/minigame1/smash_arms.png')

        self.arm_sprite = cocos.sprite.Sprite(self.ua, position=(640,360))
        self.add(self.arm_sprite)

    # setters/getters

    # methods

    def on_mouse_motion(self, x, y, dx, dy):
        # print(x,y)
        # self.arm_sprite.do(MoveTo((x,y),0.1))
        self.arm_sprite.position = (x,y)

    def on_mouse_press(self, x, y, button, mod):
        # pass
        self.arm_sprite.image = self.sa

    def on_mouse_release(self, x, y, button, mod):
        self.arm_sprite.image = self.ua
