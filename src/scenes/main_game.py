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
import random

# class imports
from ui.button import Button
from ui.gamebackground import GameBackground
from ui.scrollable_button import ScrollableButton
from ui.hero_layer import HeroLayer
from ui.cutscene import Cutscene
from ui.main_game_layer import MainGameLayer
from profiles.profile import Profile
from cocos.actions import *
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
        # self.bg = GameBackground('../res/main_game_backgrounds/background.png')   

        super().__init__()

        self.save_dir = 'profiles/save.json'
        if self.state == 'newgame':
            self.profile = Profile()
        else:
            self.profile = Profile() if not os.path.exists(self.save_dir) else Profile.read_save(self.save_dir)

        self.popups = {}
        self.shown_popup = None
        # for name in os.
        self.popups['finish_helicase'] = cocos.sprite.Sprite(pyglet.image.load('../res/popups/finish_helicase.png'), position=(640,360))
        self.popups['fail_helicase'] = cocos.sprite.Sprite(pyglet.image.load('../res/popups/fail_helicase.png'), position=(640,360))
        self.popups['finish_pp'] = cocos.sprite.Sprite(pyglet.image.load('../res/popups/finish_pp.png'), position=(640,360))
        self.popups['fail_pp'] = cocos.sprite.Sprite(pyglet.image.load('../res/popups/fail_pp.png'), position=(640,360))
        self.popups['finish_ligase'] = cocos.sprite.Sprite(pyglet.image.load('../res/popups/finish_ligase.png'), position=(640,360))
        self.popups['fail_ligase'] = cocos.sprite.Sprite(pyglet.image.load('../res/popups/fail_ligase.png'), position=(640,360))

        for pop in self.popups.values():
            self.add(pop, 4)
            pop.do(Hide())

        self.case = self.profile.information['case']

        self.pos = [600, 0]

        self.life_num = self.profile.get_lives()
        print('new life number', self.life_num)
        self.lives = cocos.sprite.Sprite(pyglet.image.load('../res/lives_'+str(self.life_num)+'.png'), position=(224,637))

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
        self.add(self.lives, z=1)
        self.scroller.add(self.MGLayer, z=0)
        self.add(self.scroller, z=0)
        
        # initial view position
        self.scroller.set_focus(*self.pos)
      
# setters/getters

# methods

    def on_enter(self):
        super(cocos.scene.Scene, self).on_enter()
        # super.on_enter()
        self.profile.save(self.save_dir)
        self.MGLayer.ch_layer.hide()
        print(self.MGLayer.ch_layer.__class__.is_event_handler)

    
    def main_next(self):

        if self.check_probs():
            self.profile.information['case'] += 1
            self.case += 1
            self.fix_probs()
        self.profile.save(self.save_dir)
        self.profile = Profile() if not os.path.exists(self.save_dir) else Profile.read_save(self.save_dir)

        # if self.case == 8:
            # cutscene = Cutscene(self.director, 2)
            # self.director.replace(cutscene)
        # else:
            # if victory:
        self.remove(self.MGLayer.ch_layer)
        self.scroller.remove(self.MGLayer)
        # instantiate new Main Game Layer
        self.MGLayer = MainGameLayer(self.director, self.scroller, self, self.case, self.profile, self.dna)
        self.scroller.add(self.MGLayer, z=1)
        self.director.pop()

    def check_probs(self): # checks if all probs are done

        for i in self.profile.information['problems']:
            if i == False:
                return False
        return True

    def show_popup(self, popup_name):
        self.popups[popup_name].do(Show())
        self.shown_popup = popup_name

    def hide_popup(self):
        self.popups[self.shown_popup].do(Hide())
        self.shown_popup = None
        if self.case == 8:
            cutscene = Cutscene(self.director, 2)
            self.director.replace(cutscene)

    def fix_probs(self): # checks if case has 2 probs
        if self.case in [2,4,6,7]:
            self.profile.information['problems'] = [False, False]
        else:
            self.profile.information['problems'] = [False]

    def failed_minigame(self):
        self.subtract_life()
        self.profile.subtract_lives()
        # self.profile.save(self.save_dir)
        print(self.profile)
        self.back()

    def subtract_life(self):
        if self.life_num > 1:
            self.life_num -= 1
            print(self.life_num)
            self.lives.image = pyglet.image.load('../res/lives_'+str(self.life_num)+'.png')
        else:
            self.back()
            print('failed game')

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
        else:
            self.pos[0] = self.pos[0] - 16/2