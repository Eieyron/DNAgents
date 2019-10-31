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
from ui.pin_button import PinButton
from ui.hero_layer import HeroLayer
from scenes.helicase import HelicaseMinigame

# 
#   CLASS
# 


# definition
class MainGameLayer(cocos.layer.ScrollableLayer):

# init
    def __init__(self, director, scroller, scene, case, profile, bg):

        super().__init__()
        
        self.bg = bg
        self.director = director
        self.scroller = scroller
        self.scene = scene
        self.case = case
        self.profile = profile
        self.scroller.add(self.bg, 0)

        # self.add_pin_test(1280, 418)
        
        # handling cases and problems in main game
        self.problem = {}

        # MINI GAMES
        '''
            helicase    
            pripoly (primase and polymirase)
            ligase
        '''

        if case == 1:
            self.problem['1'] = PinButton(64, 421, '../res/pin.png', 'helicase', self, self.profile, 0, self.choose_hero)
            self.bg.set_background(1)
        elif case == 2:
            self.problem['1'] = PinButton(143, 312, '../res/pin.png', 'pripoly', self, self.profile, 0, self.choose_hero) if not self.profile.information['problems'][0] else None
            self.problem['2'] = PinButton(599, 458, '../res/pin.png', 'pripoly', self, self.profile, 1, self.choose_hero) if not self.profile.information['problems'][1] else None
            if self.profile.information['problems'][0]:
                self.bg.set_background(3)
            elif self.profile.information['problems'][1]:
                self.bg.set_background(4)
            else:
                self.bg.set_background(2)
        elif case == 3:
            self.problem['1'] = PinButton(761, 407, '../res/pin.png', 'helicase', self, self.profile, 0, self.choose_hero)
            self.bg.set_background(5)    
        elif case == 4:
            self.problem['1'] = PinButton(732, 355, '../res/pin.png', 'pripoly', self, self.profile, 0, self.choose_hero) if not self.profile.information['problems'][0] else None
            self.problem['2'] = PinButton(1105, 482, '../res/pin.png', 'pripoly', self, self.profile, 1, self.choose_hero) if not self.profile.information['problems'][1] else None
            if self.profile.information['problems'][0]:
                self.bg.set_background(7)
            elif self.profile.information['problems'][1]:
                self.bg.set_background(8)
            else:
                self.bg.set_background(6)
        elif case == 5:
            self.problem['1'] = PinButton(1280, 418, '../res/pin.png', 'helicase', self, self.profile, 0, self.choose_hero)
            self.bg.set_background(9)
        elif case == 6:
            self.problem['1'] = PinButton(438, 544, '../res/pin.png', 'pripoly', self, self.profile, 0, self.choose_hero) if not self.profile.information['problems'][0] else None
            self.problem['2'] = PinButton(625, 189, '../res/pin.png', 'pripoly', self, self.profile, 1, self.choose_hero) if not self.profile.information['problems'][1] else None
            if self.profile.information['problems'][0]:
                self.bg.set_background(11)
            elif self.profile.information['problems'][1]:
                self.bg.set_background(12)
            else:
                self.bg.set_background(10)
        elif case == 7:
            self.problem['1'] = PinButton(1442, 991, '../res/pin.png', 'ligase', self, self.profile, 0, self.choose_hero) if not self.profile.information['problems'][0] else None
            self.problem['2'] = PinButton(1560, 789, '../res/pin.png', 'ligase', self, self.profile, 1, self.choose_hero) if not self.profile.information['problems'][1] else None
            if self.profile.information['problems'][0]:
                self.bg.set_background(14)
            elif self.profile.information['problems'][1]:
                self.bg.set_background(15)
            else:
                self.bg.set_background(13)
        else:
            self.bg.set_background(16)
        
        for button in self.problem.values():
            if button == None: continue
            self.add_pin(button)

# setters/getters

# methods

    def choose_hero(self):
        #self.hero_popup.show()
        
        self.go_to_minigame()
        self.scroller.remove(self.pin_button)
        self.scene.main_next()


    def go_to_minigame(self):
        #print(self.profile.information['minigame']) 
        self.minigame = self.profile.information['minigame']
        if self.minigame == 'helicase':
            print('helicase')
            self.director.push(HelicaseMinigame(self.director))
        elif self.minigame == 'pripoly':
            print('pripoly')
        else:
            print('ligase')


    def add_pin(self, pin_button):
        self.pin_button = pin_button
        self.pin_button.setHasHighlight('../res/pin_h.png')        
        
        self.scroller.add(self.pin_button, 0)
        self.hero_popup = HeroLayer(self.scroller, self.pin_button.spr)
        self.scene.add(self.hero_popup, z=2)

    def add_pin_test(self, x, y):
        pin_button = PinButton(x, y, '../res/pin.png', 'wew', self, self.profile, 0, self.choose_hero, True)
        pin_button.setHasHighlight('../res/pin_h.png')        
        
        self.scroller.add(pin_button, 0)