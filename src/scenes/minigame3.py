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

# class imports
from ui.button import Button
from ui.bomb_deployer import Bomb_Deployer
from ui.gamebackground import GameBackground
from cocos.actions import *
# 
#   CLASS
# 


# definition
class MiniGame3(cocos.scene.Scene):

# init
    def __init__(self, director, mainGameLayer, victory_action):
        
        self.director = director
        self.mainGameLayer = mainGameLayer
        self.victory_action = victory_action

        super().__init__()

        bg = GameBackground('../res/minigame3/minigame3_background.png')        
        bg2 = GameBackground('../res/minigame3/nearplane.png')        
        self.pos = [1280, 720]

        self.buttons = {}

        # self.buttons['boi'] = Button(640,360, '../res/boi.png', self, self.back, isSpriteSheet=True)

        # self.do_list.reverse()
        self.game_counter = 0
        self.alive_nucleotides = 5
        self.buffer = 0

        self.objects_hit = 0
        self.missed = 0

        self.buttons['back'] = Button(53,666, '../res/main_left.png', self, self.back)
        self.buttons['back'].setHasHighlight('../res/main_left_h.png')

        self.strand = 'atcgatcgaatcgatcgaatcgatcgaatcgatcga'
        # self.land_blocks = {}
        self.dna = []
        anchor = [0,0]
        for base in self.strand:
            block = Button(1236+anchor[0],162+anchor[1],'../res/minigame3/block_'+base+'.png',self, self.back)
            block.move_right_inf()

            self.dna.append(block)

            anchor = [anchor[0]-120,anchor[1]]


        # self.counter_strand = 'atcgabctgagcbtagcbtagbctagbctagbctag'
        self.counter_strand = ['a' if x == 't' else
                                'g' if x == 'c' else
                                'c' if x == 'g' else
                                't' if x == 'a' else
                                'b' for x in self.strand]

        # self.num_to_random = [x for x in ]
        self.num_to_random = 6
        # counter = self.num_to_random
        self.rand_list = random.sample(range(7,len(self.strand)),self.num_to_random)
        self.rand_list.sort()
        # self.rand_list.reverse()

        # self.blank_counter_strand = ['b' if index in self.rand_list else x for index, x in enumerate(self.counter_strand)]

        self.counter_dna = []
        self.ammo = []

        anchor = [0,0]
        for index, base in enumerate(self.counter_strand):
            # print('yo')
            # if not base == 'b':
            block = Button(1200+anchor[0],83+anchor[1],'../res/minigame3/block_'+base+'.png',self, self.back)
            block.move_right_inf()

            self.counter_dna.append(block)

            anchor = [anchor[0]-120,anchor[1]]

            if index in self.rand_list:

                block.spr.do(Hide())
                print('ammo index', index)

                self.ammo.append('a' if self.strand[index] == 't' else
                                'g' if self.strand[index] == 'c' else
                                'c' if self.strand[index] == 'g' else
                                't' if self.strand[index] == 'a' else
                                'b')

        self.dna.reverse()
        # self.counter_dna.reverse()
        # self.ammo.reverse()

        self.deployed_ammo = 0
        self.ammo_blocks = []
        # anchor = [0,0]
        for index, base in enumerate(self.ammo):
            # print('yo')
            # if not base == 'b':
            block = Button(970, 549, '../res/minigame3/block_'+base+'.png',self, self.back)
            block.target_hit_action = self.hit_object
            block.target_miss_action = self.missed_object
            block.spr.do(Hide())
            # block.move_right_inf()

            self.ammo_blocks.append(block)


        # self.ammo_blocks.reverse()

        self.characters = {}
        self.characters['squirrelboi'] = Button(970,549,'../res/minigame3/squirrelboi.png', self, self.back)
        self.characters['squirrelboi'].move_up_and_down()

        for button in self.buttons.values():
            self.add(button, 5)

        for block in self.dna:
            self.add(block, 1)

        self.counter_dna.reverse()
        for block in self.counter_dna:
            self.add(block, 2)
        self.counter_dna.reverse()

        for block in self.ammo_blocks:
            self.add(block, 1)

        for block in self.characters.values():
            self.add(block, 3)



        # for nucleotide in self.dna:
        #     self.add(nucleotide, 2)

        self.add(bg, 0)
        self.add(bg2, 3)
        self.add(Bomb_Deployer(self, self.deployed))

        th.start_new_thread(self.endgame_checker, ())

# methods
    def back(self):
        self.director.pop()
        print("select stage back")

    # def finish_level(self):
    #     self.

    def change_button_sprite(self):
        try:
            self.button_to_assign.spr.image = pyglet.image.load(self.img_to_assign)
        except Exception as e:
            self.back()

    def deployed(self):
        print('deployed nigga',self.rand_list[self.deployed_ammo])
        self.ammo_blocks[self.deployed_ammo].deploy(self.counter_dna[self.rand_list[self.deployed_ammo]])
        self.deployed_ammo += 1
        # if self.hit_object == self.num_to_random:
        #     self.characters['squirrelboi'].finish_moving()


    def endgame_checker(self):

        while 1:
            # print('missed',self.missed)
            time.sleep(0.1)
            if self.objects_hit == self.num_to_random:
                self.characters['squirrelboi'].finish_moving(self.victory_action)
            if self.missed > 0:
                self.back()

    def hit_object(self):
        self.objects_hit += 1
        print('hit objects', self.objects_hit)

    def missed_object(self):
        print('missed')
        self.missed += 1

    # def

