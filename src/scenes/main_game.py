#select_level.py

#
#   SELECT LEVEL 
# a scene where you can select the stage you want to play, mitosis or meiosis
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import _thread as th
import time

# class imports
from ui.button import Button
from ui.gamebackground import GameBackground
from ui.scrollable_button import ScrollableButton
from ui.hero_layer import HeroLayer
# 
#   CLASS
# 


# definition
class MainGame(cocos.scene.Scene):

# init
    def __init__(self, director):
        
        self.director = director

        super().__init__()

        bg = GameBackground('../res/main_game_background.png')        
        self.pos = [1280, 720]

        self.scroller = cocos.layer.ScrollingManager() 
        self.scroller.add(bg, 0)
        back_button = Button(73, 640, '../res/main_left.png', self, self.back)
        back_button.setHasHighlight('../res/main_left_h.png')

        left_button = Button(1050, 90, '../res/main_left.png', self, self.set_pos_left)
        left_button.setHasHighlight('../res/main_left_h.png')
        right_button = Button(1190, 90, '../res/main_right.png', self, self.set_pos_right)
        right_button.setHasHighlight('../res/main_right_h.png')
        
        self.add(back_button, z=1)
        self.add(left_button, z=1)
        self.add(right_button, z=1)
        self.add(self.scroller, z=0)
        
        # initial view position
        self.scroller.set_focus(*self.pos)

        self.add_pin(1403, 926)
        self.add_pin(755, 656)
        self.add_pin(127, 438)
        
        '''
                1280, 720
            960, 540
        640, 360
        '''

# setters/getters

# methods
    def back(self):
        self.director.pop()
        print("select stage back")       

    def choose_hero(self):
        self.hero_popup.show()
    
    def add_pin(self, x, y):
        pin_button = ScrollableButton(x, y, '../res/pin.png', self, self.choose_hero)
        pin_button.setHasHighlight('../res/pin_h.png')        
        self.scroller.add(pin_button, 0)
        self.hero_popup = HeroLayer(self.scroller, pin_button.spr)
        self.add(self.hero_popup, z=1)
    
    def set_pos_right(self):
        th.start_new_thread(self.pos_right, ())

    def set_pos_left(self):
        th.start_new_thread(self.pos_left, ())            

    def pos_right(self):
        if self.pos[0] < 960:
            while self.pos[0] < 960:
                time.sleep(0.025)
                self.pos_op ('add')
                self.scroller.set_focus(*self.pos)   
        elif self.pos[0] >= 960:
            while self.pos[0] < 1280:
                time.sleep(0.025)
                self.pos_op ('add')
                self.scroller.set_focus(*self.pos)

    def pos_left(self):    
        if self.pos[0] > 960:
            while self.pos[0] > 960:
                time.sleep(0.025)
                self.pos_op ('min')
                self.scroller.set_focus(*self.pos)   
        elif self.pos[0] <= 960:
            while self.pos[0] > 640:
                time.sleep(0.025)
                self.pos_op('min')
                self.scroller.set_focus(*self.pos)
        return

    def pos_op(self, op):
        if op == 'add':
            self.pos[0] = self.pos[0] + 16/2
            self.pos[1] = self.pos[1] + 9/2
        else:
            self.pos[0] = self.pos[0] - 16/2
            self.pos[1] = self.pos[1] - 9/2
