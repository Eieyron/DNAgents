#minigame2.py

#
#   2nd MINIGAME 
# a a game that simulates the movements of a split-dna being completed by the primase and the polymerase
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import _thread as th
import time
import random
import copy

# class imports
from ui.button import Button
from ui.arm_deployer import Arm_Deployer
from ui.gamebackground import GameBackground
from cocos.actions import *
# 
#   CLASS
# 


# definition
class MiniGame1(cocos.scene.Scene):

# init
    def __init__(self, director, victory_action, fail_action, strand=None):
        
        self.director = director
        self.victory_action = victory_action
        self.fail_action = fail_action

        super().__init__()

        self.finish_level_pictures = {}
        # self.finish_level_pictures['0']=cocos.
        for i in range(0,5):
            self.finish_level_pictures[str(i)] = cocos.sprite.Sprite(pyglet.image.load('../res/minigame1/End/'+str(i)+'.png'), position=(640,360))

        # bg = GameBackground('../res/minigame1/end/click anywhere to continue.png')

        self.dp = cocos.sprite.Sprite(pyglet.image.load('../res/Profile_picture/Helicase_Active_Agent.png'), position=(350,665))
        # self.dp = Button(350,665, '../res/Profile_picture/Helicase_Active_Agent.png', self, self.back, toAdjust=True)
        self.add(self.dp, 11)

        # jill_dorothy_monzon

        self.accomplished_targets = 0
        self.target_eliminated = False

        self.bg_index = 0

        self.completed = False
        self.victory = False

        self.img_to_assign = pyglet.image.load('../res/minigame1/punch.png')

        self.to_clean = []

        self.buttons = {}

        self.buttons['back'] = Button(53,666, '../res/main_left.png', self, self.back)
        self.buttons['back'].setHasHighlight('../res/main_left_h.png')

        self.finish_button = Button(640, 360, '../res/minigame1/finish_level_button.png', self, self.next_image)
        self.finish_button.disable()


        # if strand == None:
        # self.strand = list('a') # defines the left strand
        # else:
        #     self.strand = strand

        self.strand = [ 'a' if x == 0 else 
                        't' if x == 1 else
                        'c' if x == 2 else
                        'g' if x == 3 else
                        'b' for x in [random.randrange(0,4) for i in range(0,20)]]
        self.strand.reverse()
        self.counter_strand = [ 'a' if x == 't' else 
                                't' if x == 'a' else
                                'c' if x == 'g' else
                                'g' if x == 'c' else
                                'b' for x in self.strand]

        print('strand', self.strand)
        self.game_counter = len(self.strand)-1
        print('counter_strand', self.counter_strand)

        self.backgrounds = []
        for index, base in enumerate(self.strand):
            bg_pair = [cocos.sprite.Sprite(pyglet.image.load('../res/minigame1/left_'+base+'.png'),position=(640,360)),
                                cocos.sprite.Sprite(pyglet.image.load('../res/minigame1/right_'+self.counter_strand[index]+'.png'),position=(640,360))]
            self.backgrounds.append(bg_pair)
            self.add(bg_pair[0], 1)
            self.add(bg_pair[1], 1)

        self.targets = []
        for base in self.strand:
            for i in range(0,3):
                random_coordinate = (random.randint(200, 1080), random.randint(200, 520))
                target = Button(*random_coordinate, '../res/minigame1/TARGET.png', self, self.target_clicked, isSpriteSheet=True)
                target.hide()
                self.targets.append(target)
                self.add(target,3)

        for button in self.buttons.values():
            self.add(button, 2)

        self.ad = Arm_Deployer(self,self.back)

        self.add(self.ad,4)
        # self.add(self.finish_level_pictures[0],0)   
        for i in range(4,-1,-1):
            self.add(self.finish_level_pictures[str(i)],0)

        self.add(self.finish_button,0)

        # th.start_new_thread(self.run_game, ())
        self.generate_target()

# methods
    def back(self):
        # self.victory = False
        # self.completed = True
        self.director.pop()
        print("select stage back")

    def next_image(self):
        # pass
        if not self.bg_index == 4: 
            self.finish_level_pictures[str(self.bg_index)].do(FadeOut(1))
            self.bg_index += 1
        else:
            self.finish_level()


    def finish_level(self):
        # self.victory = True
        # self.completed = True
        # self.director.pop()
        print("finished_level")
        self.victory_action()

    def fail_level(self):
        # self.dire

        self.fail_action()

    def generate_target(self):

        self.current_target = self.targets[self.accomplished_targets]
        self.current_target.show()

    def target_clicked(self):
        print('clkiecked')
        # self.cuurspr.do()
        self.accomplished_targets += 1
        self.target_eliminated = True
       
        self.to_clean.append(self.current_target)
        
        self.current_target.spr.do(CallFunc(self.change_button_sprite)+CallFunc(self.next_background))
        self.current_target.disable()


        if self.game_counter >= 0:
            self.generate_target()
        else:
            self.finish_button.enable()

    def next_background(self):

        if self.accomplished_targets%3 == 0:

            print('next bg')
            bg_pair = self.backgrounds[self.game_counter]
            bg_pair[0].do(MoveBy((-640,0),1))
            bg_pair[1].do(MoveBy((640,0),1)+CallFunc(self.clean))
            for button in self.to_clean:
                button.spr.do(MoveBy((640 * (-1 if button.spr.position[0] < 640 else 1),0),1))

            for obj in bg_pair: self.to_clean.append(obj)

            self.game_counter -= 1

    # def change_s
    def clean(self):

        for obj in self.to_clean:            
            self.remove(obj)
        self.to_clean = []

    def change_button_sprite(self):
        try:
            self.current_target.spr.image = self.img_to_assign
            self.current_target.x -= 125
        except Exception as e:
            print(e)
            # self.back()

    # def

