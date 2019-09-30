#
#   InformationLayer
# An information layer that floats when the sprite it is connected to is highlighted  
#
#

#
#   IMPORT STATEMENTS
#

# imports

import cocos
import pyglet

# froms 

from cocos.actions import *

# 
#   CLASS
# 

# constants

# definition

class InformationLayer(cocos.layer.ColorLayer):

    is_event_handler = True

    # init

    def __init__(self, scroller, target, width=1280, height=720):
        super().__init__(57, 67, 63, 0, width=width, height=height)
        
        picDir = '../res/info_layers/niccleus.png'

        self.scroller = scroller
        self.opacity = 0
        self.target = target

        self.image = pyglet.image.load(picDir)
        self.spr = cocos.sprite.Sprite(self.image, position=(640,360))

        self.highlight = False
        self.onHover = False
        self.highlight = True

        self.add(self.spr)
        self.spr.do(Hide())
        # self.target.unshow()

    # setters/getters
    def setHasHighlight(self, picDir):
        self.highlight = True
    
    def setTarget(self, target):
        self.target = target

    # methods
    def on_mouse_motion(self, x, y, dx, dy):

        x,y = self.scroller.screen_to_world(x,y)

        if (not self.onHover) and self.target.contains(x,y):
            self.onHover = True
            if self.highlight:
                self.opacity = 70
                self.spr.do(Show())

        elif self.onHover and (not self.target.contains(x,y)):
            self.onHover = False
            if self.highlight:
                self.opacity = 0
                self.spr.do(Hide())

    def on_mouse_press(self, x, y, button, mod):
        if self.onHover:
            self.action()

    def setSprite(self, img):
        self.spr.image = img

