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
from scenes.select_mitosis_level import SelectMitosisLevel
from ui.button import Button
from ui.gamebackground import GameBackground, GameLayer
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

        back_button = Button(73, 651, '../res/back.png', self, self.back)
        back_button.setHasHighlight('../res/back_h.png')

        left_button = Button(1050, 90, '../res/main_left.png', self, self.set_pos_left)

        right_button = Button(1190, 90, '../res/main_right.png', self, self.set_pos_right)

        self.add(back_button, z=1)
        self.add(left_button, z=1)
        self.add(right_button, z=1)
        self.add(self.scroller, z=0)

        # initial view position
        self.scroller.set_focus(*self.pos)

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
                print(*self.pos)
                self.scroller.set_focus(*self.pos)   
        elif self.pos[0] <= 960:
            while self.pos[0] > 640:
                time.sleep(0.025)
                self.pos_op('min')
                print(*self.pos)
                self.scroller.set_focus(*self.pos)
        return

    def pos_op(self, op):
        if op == 'add':
            self.pos[0] = self.pos[0] + 16/2
            self.pos[1] = self.pos[1] + 9/2
        else:
            self.pos[0] = self.pos[0] - 16/2
            self.pos[1] = self.pos[1] - 9/2
