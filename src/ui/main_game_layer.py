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
from ui.choose_hero import Choose_Hero
from scenes.helicase_minigame import HelicaseMinigame
from scenes.minigame1 import MiniGame1
from scenes.minigame2 import MiniGame2
from scenes.minigame3 import MiniGame3

# 
#   CLASS
# 


# definition
class MainGameLayer(cocos.layer.ScrollableLayer):

# init
    def __init__(self, director, scroller, scene, case, profile, dna):

        super().__init__()
        
        self.dna = dna
        self.director = director
        self.scroller = scroller
        self.scene = scene
        self.case = case
        self.profile = profile

        self.to_pop = []

        self.minigame_completed = False

        self.background = GameBackground('../res/main_game_backgrounds/background.png')

        self.ch_layer = Choose_Hero(self, self.go_to_minigame)

        self.scroller.add(self.background, 0)
        self.scroller.add(self.dna, 0)
        self.scene.add(self.ch_layer,4)

        #self.add_pin_test(1000, 360)
        
        # handling cases and problems in main game
        self.problem = {}

        # MINI GAMES
        '''
            helicase    
            pripoly (primase and polymirase)
            ligase
        '''

        if case == 1:
            self.problem['1'] = PinButton(157, 424, '../res/pin.png', 'helicase', self, self.profile, 0, self.choose_hero)
            self.dna.set_background(1)
            self.ch_layer.set_heroes_to_select([0])
        elif case == 2:
            self.problem['1'] = PinButton(414, 481, '../res/pin.png', 'pripoly', self, self.profile, 0, self.choose_hero) if not self.profile.information['problems'][0] else None
            self.problem['2'] = PinButton(46, 257, '../res/pin.png', 'pripoly', self, self.profile, 1, self.choose_hero) if not self.profile.information['problems'][1] else None
            if self.profile.information['problems'][0]:
                self.dna.set_background(3)
            elif self.profile.information['problems'][1]:
                self.dna.set_background(4)
            else:
                self.dna.set_background(2)
            self.ch_layer.set_heroes_to_select([1,2])
        elif case == 3:
            self.problem['1'] = PinButton(538, 427, '../res/pin.png', 'helicase', self, self.profile, 0, self.choose_hero)
            self.dna.set_background(5)    
            self.ch_layer.set_heroes_to_select([0])
        elif case == 4:
            self.problem['1'] = PinButton(573, 321, '../res/pin.png', 'pripoly', self, self.profile, 0, self.choose_hero) if not self.profile.information['problems'][0] else None
            self.problem['2'] = PinButton(1029, 461, '../res/pin.png', 'pripoly', self, self.profile, 1, self.choose_hero) if not self.profile.information['problems'][1] else None
            if self.profile.information['problems'][0]:
                self.dna.set_background(7)
            elif self.profile.information['problems'][1]:
                self.dna.set_background(8)
            else:
                self.dna.set_background(6)
            self.ch_layer.set_heroes_to_select([1,2])
        elif case == 5:
            self.problem['1'] = PinButton(1167, 427, '../res/pin.png', 'helicase', self, self.profile, 0, self.choose_hero)
            self.dna.set_background(9)
        elif case == 6:
            self.problem['1'] = PinButton(1575, 521, '../res/pin.png', 'pripoly', self, self.profile, 0, self.choose_hero) if not self.profile.information['problems'][0] else None
            self.problem['2'] = PinButton(1132, 328, '../res/pin.png', 'pripoly', self, self.profile, 1, self.choose_hero) if not self.profile.information['problems'][1] else None
            if self.profile.information['problems'][0]:
                self.dna.set_background(11)
            elif self.profile.information['problems'][1]:
                self.dna.set_background(12)
            else:
                self.dna.set_background(10)
            self.ch_layer.set_heroes_to_select([1,2])
        elif case == 7:
            self.problem['1'] = PinButton(85, 225, '../res/pin.png', 'ligase', self, self.profile, 0, self.choose_hero) if not self.profile.information['problems'][0] else None
            self.problem['2'] = PinButton(79, 568, '../res/pin.png', 'ligase', self, self.profile, 1, self.choose_hero) if not self.profile.information['problems'][1] else None
            if self.profile.information['problems'][0]:
                self.dna.set_background(14)
            elif self.profile.information['problems'][1]:
                self.dna.set_background(15)
            else:
                self.dna.set_background(13)
            self.ch_layer.set_heroes_to_select([3])
        else:
            self.dna.set_background(16)
        
        for i in range(1,(len(self.problem)+1)):
            if self.problem[str(i)] == None: continue
            self.add_pin(self.problem[str(i)], i)

        # for button in self.problem.values():
        #     if button == None: continue
        #     self.add_pin(button)

# setters/getters

# methods

    def choose_hero(self):
        #self.hero_popup.show()
        # try:
        #     self.scroller.remove(self.pin_button1)
        #     #print('pin 1 removed')
        # except:
        #     print('')
            #print('pin doesnt exist')
        # if len(self.problem) != 1:
            
        #     try:
        #         self.scroller.remove(self.pin_button2)
        #         #print('pin 2 removed')
        #     except:
        #         print('')
                #print('pin doesnt exist')


        self.ch_layer.show()
        # self.go_to_minigame()

    def go_to_minigame(self):
        #print(self.profile.information['minigame']) 
        self.minigame = self.profile.information['minigame']

        miniG = None
        if self.minigame == 'helicase':
            print('helicase')
            miniG = MiniGame1(self.director, self, self.next_scene)
        elif self.minigame == 'pripoly':
            print('pripoly')
            miniG = MiniGame2(self.director, self, self.next_scene)
        else:
            print('ligase')
            # self.director.push(
            miniG = MiniGame3(self.director, self, self.next_scene)

        # th.start_new_thread(self.minigame_checker,  (miniG,))
        self.director.push(miniG)
        # self.scene.main_next()

    def next_scene(self):
        try:
            self.scroller.remove(self.pin_button1)
            #print('pin 1 removed')
        except:
            print('')
            print('pin doesnt exist')
        if len(self.problem) != 1:
            
            try:
                self.scroller.remove(self.pin_button2)
                #print('pin 2 removed')
            except:
                print('')
                print('pin doesnt exist')
        self.scene.main_next()

    # def 

    def add_pin(self, pin_button, i):
        i = i
        if i == 1:
            self.pin_button1 = pin_button
            self.pin_button1.setHasHighlight('../res/pin_h.png')        
            self.scroller.add(self.pin_button1, 1)
        elif i == 2:
            self.pin_button2 = pin_button
            self.pin_button2.setHasHighlight('../res/pin_h.png')        
            self.scroller.add(self.pin_button2, 1)

        # self.hero_popup = HeroLayer(self.scroller, self.pin_button.spr)
        # self.scene.add(self.hero_popup, z=2)

    def add_pin_test(self, x, y):
        pin_button = PinButton(x, y, '../res/pin.png', 'wew', self, self.profile, 0, self.choose_hero, True)
        pin_button.setHasHighlight('../res/pin_h.png')        
        
        self.scroller.add(pin_button, 1)