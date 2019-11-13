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
from ui.button import Button


# 
#   CLASS
# 

# constants

# definition

class Choose_Hero(cocos.layer.ColorLayer):

    is_event_handler = True

    # init

    def __init__(self,  parent, action, width=1280, height=720):
        self.parent = parent
        self.action = action
        self.to_select = []

        super().__init__(30, 48, 130, 0, width=width, height=height)

        # self.ua = pyglet.image.load('../res/minigame1/upright_arms.png')
        # self.sa = pyglet.image.load('../res/minigame1/smash_arms.png')

        self.bg_img = pyglet.image.load('../res/choose_hero/platform.png')
        self.bg = cocos.sprite.Sprite(self.bg_img, position=(640,360))
        self.selected = []
        # self.arm_sprite = cocos.sprite.Sprite(self.ua, position=(640,360))

        self.buttons = {}
        self.buttons['helicase'] = Button(295,125, '../res/choose_hero/helicase.png', self, self.helicase_clicked)
        self.buttons['helicase'].setHasProjection('../res/choose_hero/helicase_holo.png')

        self.buttons['primase'] = Button(525,125, '../res/choose_hero/primase.png', self, self.primase_clicked)
        self.buttons['primase'].setHasProjection('../res/choose_hero/primase_holo.png')
        
        self.buttons['polymerase'] = Button(755,125, '../res/choose_hero/polymerase.png', self, self.polymerase_clicked)
        self.buttons['polymerase'].setHasProjection('../res/choose_hero/polymerase_holo.png')

        self.buttons['ligase'] = Button(985,125, '../res/choose_hero/ligase.png', self, self.ligase_clicked,)
        self.buttons['ligase'].setHasProjection('../res/choose_hero/ligase_holo.png')


        
        for button in self.buttons.values():
            self.add(button, 1)

        self.add(self.bg, 0)

        self.hide()

    # setters/getters

    # methods

    def on_mouse_motion(self, x, y, dx, dy):
        # print(x,y)
        # self.arm_sprite.do(MoveTo((x,y),0.1))
        # self.arm_sprite.position = (x,y)
        pass

    def on_mouse_press(self, x, y, button, mod):
        # pass
        pass
        # self.arm_sprite.image = self.sa

    def on_mouse_release(self, x, y, button, mod):
        pass
        # self.arm_sprite.image = self.ua

    def set_heroes_to_select(self, hero_list):
        self.to_select = hero_list

    def helicase_clicked(self):
        self.selected.append(0)
        self.evaluate_clicked()

    def primase_clicked(self):
        self.selected.append(1)
        self.evaluate_clicked()

    def polymerase_clicked(self):
        self.selected.append(2)
        self.evaluate_clicked()

    def ligase_clicked(self):
        self.selected.append(3)
        self.evaluate_clicked()

    def evaluate_clicked(self):
        print('evaliating')

        print('self.to_select',self.to_select)
        print('self.selected',self.selected)

        if not len(self.to_select) == len(self.selected):
            return

        elif set(self.to_select) == set(self.selected):

            self.action()
            self.to_select = []
            self.selected = []
            self.hide()

        else:
            return

    def hide(self):

        Choose_Hero.is_event_handler = False

        self.opacity = 0

        self.bg.do(Hide())
        for button in self.buttons.values():
            button.do(Hide())

    def show(self):

        Choose_Hero.is_event_handler = True

        self.opacity = 200

        self.bg.do(Show())
        for button in self.buttons.values():
            button.do(Show())
