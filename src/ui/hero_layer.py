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
from ui.button import Button


# 
#   CLASS
# 

# constants

# definition

class HeroLayer(cocos.layer.ColorLayer):

    is_event_handler = False

    # init

    def __init__(self, scroller, target, width=1280, height=720):
        super().__init__(57, 67, 63, 0, width=width, height=height)
        
        picDir = '../res/popup_resources/choose_hero_popup.png'

        self.scroller = scroller
        self.opacity = 0
        self.target = target

        self.image = pyglet.image.load(picDir)
        self.spr = cocos.sprite.Sprite(self.image, position=(640,360))

        self.backButton = Button(1070,627, '../res/popup_resources/exit_button.png',self,self.hide)
        self.backButton.setHasHighlight('../res/popup_resources/exit_button_h.png')

        self.highlight = False
        self.onHover = False
        self.highlight = True

        self.add(self.backButton,1)
        self.add(self.spr,0)

        self.spr.do(Hide())
        self.backButton.spr.do(Hide())
        # self.target.unshow()

    # setters/getters
    def setHasHighlight(self, picDir):
        self.highlight = True
    
    def setTarget(self, target):
        self.target = target

    # methods
    def on_mouse_motion(self, x, y, dx, dy):

        pass

        # x,y = self.scroller.screen_to_world(x,y)

        # if (not self.onHover) and self.target.contains(x,y):
        #     self.onHover = True
        #     if self.highlight:
        #         self.opacity = 70
        #         # self.spr.do(Show())

        # elif self.onHover and (not self.target.contains(x,y)):
        #     self.onHover = False
        #     if self.highlight:
        #         self.opacity = 0
                # self.spr.do(Hide())

    def on_mouse_press(self, x, y, button, mod):
        # if self.onHover:
        #     self.spr.do(Show())

        pass

    def show(self):
        HeroLayer.is_event_handler = True
        self.opacity = 70
        self.spr.do(Show())
        self.backButton.spr.do(Show())

    def hide(self):
        HeroLayer.is_event_handler = False
        self.opacity = 0
        self.spr.do(Hide())        
        self.backButton.spr.do(Hide())

    def setSprite(self, img):
        self.spr.image = img

