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

class Bomb_Deployer(cocos.layer.Layer):

    is_event_handler = True

    # init

    def __init__(self,  parent, action):
        self.parent = parent
        self.action = action

        super().__init__()

    # setters/getters

    # methods

    def on_key_press(self, key, modifiers):
        global keys

    def on_key_release(self, key, modifiers):
        global keys
        # print("deployed")
        self.action()
