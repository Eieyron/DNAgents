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

# froms
from pyglet.window import key


# 
#   CLASS
# 

# constants

class KeyMove(cocos.actions.Move):

    def step(self, dt):
        super(KeyMove, self).step(dt)
        # print(keys)
        xvel = ((key.RIGHT in keys) - (key.LEFT in keys)) * 50
        yvel = ((key.UP in keys) - (key.DOWN in keys)) * 50
        self.target.velocity = (xvel, yvel)
        print(self.target.position)

# definition

class Button(cocos.layer.Layer):

    is_event_handler = True

    # init

    def __init__(self, x, y, picDir, parent, action, toAdjust=False):
        global keys, container

        # is_event_handler = toAdjust

        keys = set()
        container = parent

        self.toAdjust = toAdjust
        self.parent = parent
        self.action = action
        self.highlight = False
        self.active = True
        super().__init__()

        self.image = pyglet.image.load(picDir)

        self.spr = cocos.sprite.Sprite(self.image, position=(x,y))
        self.spr.velocity = (0,0)

        self.onHover = False

        self.add(self.spr)

        if toAdjust:
            self.spr.do(KeyMove())

    # setters/getters
    def setHasHighlight(self, picDir):
        self.highlight = True
        self.image_h = pyglet.image.load(picDir)

    def setInactive(self, picDir):
        self.active = False
        self.image_h = pyglet.image.load(picDir)


    # def setVelocity(self, point):
    #     self.velocity = point

    # methods
    def on_mouse_motion(self, x, y, dx, dy):
        if (not self.onHover) and self.spr.contains(x,y):
            self.onHover = True
            if self.highlight:
                self.setSprite(self.image_h)
        elif self.onHover and (not self.spr.contains(x,y)):
            self.onHover = False
            if self.highlight:
                self.setSprite(self.image)

    def on_mouse_press(self, x, y, button, mod):
        if self.onHover and self.active:
            self.action()

    def on_key_press(self, key, modifiers):
        global keys
        if self.toAdjust:
            keys.add(key)

    def on_key_release(self, key, modifiers):
        global keys
        if self.toAdjust:
            keys.remove(key)

    def setSprite(self, img):
        self.spr.image = img

