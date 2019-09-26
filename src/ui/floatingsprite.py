#
#   Floating Sprite
# A sprite that floats 
#
#

#
#   IMPORT STATEMENTS
#

# imports

import cocos
import pyglet

# froms 

# 
#   CLASS
# 

# constants

# definition

class FloatingSprite(cocos.sprite.Sprite):

    is_event_handler = True

    # init

    def __init__(self, image, position = (0,0)):
        super().__init__(image, position)
        self.image_o = image
        self.highlight = False
        self.onHover = False

    # setters/getters
    def setHasHighlight(self, picDir):
        self.highlight = True
        self.image_h = pyglet.image.load(picDir)

    # def setVelocity(self, point):
    #     self.velocity = point

    # methods
    def on_mouse_motion(self, x, y, dx, dy):
        print(self)
        if (not self.onHover) and self.contains(x,y):
            self.onHover = True
            if self.highlight:
                self.setSprite(self.image_o)
        elif self.onHover and (not self.contains(x,y)):
            self.onHover = False
            if self.highlight:
                self.setSprite(self.image_h)

    def on_mouse_press(self, x, y, button, mod):
        if self.onHover:
            self.action()

    def setSprite(self, img):
        self.image = img

