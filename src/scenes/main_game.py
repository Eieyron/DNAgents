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
import os

# class imports
from ui.button import Button
from ui.gamebackground import GameBackground
from ui.scrollable_button import ScrollableButton
from ui.hero_layer import HeroLayer
from ui.main_game_layer import MainGameLayer
from profiles.profile import Profile
# 
#   CLASS
# 


# definition
class MainGame(cocos.scene.Scene):

# init
    def __init__(self, director, state):
        
        self.director = director
        self.state = state
        
        self.dna = GameBackground('../res/main_game_backgrounds/main.png')   

        super().__init__()

        self.save_dir = 'profiles/save.json'
        if self.state == 'newgame':
            self.profile = Profile()
        else:
            self.profile = Profile() if not os.path.exists(self.save_dir) else Profile.read_save(self.save_dir)
        

        self.case = self.profile.information['case']

        self.pos = [600, 0]

        self.scroller = cocos.layer.ScrollingManager() 
        self.MGLayer = MainGameLayer(self.director, self.scroller, self, self.case, self.profile, self.dna)

        back_button = Button(1199, 658, '../res/back_button.png', self, self.back)
        back_button.setHasHighlight('../res/back_button_h.png')

        left_button = Button(1050, 90, '../res/BUTTON LEFT.png', self, self.set_pos_left)
        left_button.setHasHighlight('../res/BUTTON LEFT HIGHLIGHTED.png')
        right_button = Button(1190, 90, '../res/BUTTON RIGHT.png', self, self.set_pos_right)
        right_button.setHasHighlight('../res/BUTTON RIGHT HIGHLIGHTED.png')
        
        self.add(back_button, z=1)
        self.add(left_button, z=1)
        self.add(right_button, z=1)
        self.scroller.add(self.MGLayer, z=1)
        self.add(self.scroller, z=0)
        
        # initial view position
        self.scroller.set_focus(*self.pos)
      
# setters/getters

# methods
    
    def main_next(self):
        #self.save_dir = 'profiles/save.json'
        if self.check_probs():
            self.profile.information['case'] += 1
            self.case += 1
            self.fix_probs()
        self.profile.save(self.save_dir)
        self.profile = Profile() if not os.path.exists(self.save_dir) else Profile.read_save(self.save_dir)        

        self.scroller.remove(self.MGLayer)
        # instantiate new Main Game Layer
        self.MGLayer = MainGameLayer(self.director, self.scroller, self, self.case, self.profile, self.dna)
        self.scroller.add(self.MGLayer, z=1)

    def check_probs(self): # checks if all probs are done
        for i in self.profile.information['problems']:
            if i == False:
                return False
        return True

    def fix_probs(self): # checks if case has 2 probs
        if self.case == 2:
            self.profile.information['problems'] = [False, False]
        elif self.case == 4:
            self.profile.information['problems'] = [False, False]
        elif self.case == 6:
            self.profile.information['problems'] = [False, False]
        elif self.case == 7:
            self.profile.information['problems'] = [False, False]
        else:
            self.profile.information['problems'] = [False]

    def back(self):
        self.director.pop()
        print("select stage back")       
    
    def set_pos_right(self):
        th.start_new_thread(self.pos_right, ())

    def set_pos_left(self):
        th.start_new_thread(self.pos_left, ())            

    def pos_right(self):
        if self.pos[0] < 854:
            while self.pos[0] < 854:
                time.sleep(0.025)
                self.pos_op ('add')
                self.scroller.set_focus(*self.pos)
        elif self.pos[0] >= 854:
            while self.pos[0] < 1067:
                time.sleep(0.025)
                self.pos_op ('add')
                self.scroller.set_focus(*self.pos)
        return

    def pos_left(self):    
        if self.pos[0] > 854:
            while self.pos[0] > 854:
                time.sleep(0.025)
                self.pos_op ('min')
                self.scroller.set_focus(*self.pos)   
        elif self.pos[0] <= 854:
            while self.pos[0] > 640:
                time.sleep(0.025)
                self.pos_op('min')
                self.scroller.set_focus(*self.pos)
        return

    def pos_op(self, op):
        if op == 'add':
            self.pos[0] = self.pos[0] + 16/2
            #self.pos[1] = self.pos[1] + 9/2
        else:
            self.pos[0] = self.pos[0] - 16/2
            #self.pos[1] = self.pos[1] - 9/2
