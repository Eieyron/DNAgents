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
import math


# class imports
from ui.button import Button
from ui.gamebackground import GameBackground
from cocos.actions import *

# 
#   CLASS
# 


# definition
class MiniGame2(cocos.scene.Scene):

# init
    def __init__(self, director, victory_action, fail_action):
        
        self.director = director
        # self.mainGameLayer = mainGameLayer
        self.victory_action = victory_action
        self.fail_action = fail_action

        super().__init__()

        bg = GameBackground('../res/minigame2/minigame2_background.png')        
        self.pos = [1280, 720]

        # self.youre_next = cocos.sprite.Sprite('../res/minigame2/')

        self.buttons = {}

        self.bases = [  'a' if x == 0 else 
                        't' if x == 1 else
                        'c' if x == 2 else
                        'g' if x == 3 else
                        'b' for x in [random.randrange(0,4) for i in range(0,20)]]

        # self.is_num = len(self.bases)-1
            # if index in range(0,5): 
            #     sug.do(Hide())

        # self.sugar = cocos.sprite.Sprite(pyglet.image.load('../res/minigame2/sugar.png'), position=(2000,2000))

        self.do_list = [(34, 348),
                        (106, 307),
                        (224, 295),
                        (303, 364),
                        (417, 414),
                        (536, 459),
                        (654, 388),
                        (751, 279),
                        (871, 320),
                        (956, 392),
                        (1076, 444),
                        (1200, 384)
                    ]

        # self.position_sugar(self.sugar, self.do_list[3], self.do_list[4])
        # self.add(self.sugar, z=11)

        # self.do_list.reverse()
        self.game_counter = 0
        self.alive_nucleotides = 5
        self.buffer = 0

        self.buttons['back'] = Button(78,666, '../res/back_button.png', self, self.back)
        self.buttons['back'].setHasHighlight('../res/back_button_h.png')

        self.characters = {}
        self.characters['primase'] = Button(64,75, '../res/minigame2/primase_smol.png', self, self.back)
        self.characters['polymerase'] = Button(190,75, '../res/minigame2/polymerase_smol.png', self, self.back)

        self.popup_anchor = (640,360)
        self.buttons['A'] = Button(476,90,'../res/minigame2/buttons/a.png', self, self.put_a)
        self.buttons['A'].setHasClicked('../res/minigame2/buttons/a_p.png')
        self.buttons['T'] = Button(576,90,'../res/minigame2/buttons/t.png', self, self.put_t)
        self.buttons['T'].setHasClicked('../res/minigame2/buttons/t_p.png')
        self.buttons['C'] = Button(676,90,'../res/minigame2/buttons/c.png', self, self.put_c)
        self.buttons['C'].setHasClicked('../res/minigame2/buttons/c_p.png')
        self.buttons['G'] = Button(776,90,'../res/minigame2/buttons/g.png', self, self.put_g)
        self.buttons['G'].setHasClicked('../res/minigame2/buttons/g_p.png')

        self.dna = []

        for num, base in enumerate(self.bases):

            temp = Button(2000,2000, '../res/minigame2/nucleotide_'+base+'.png', self, self.back)
            temp.identity = base
            temp.setHasInactive('../res/minigame2/nucleotide_hide.png')
            self.dna.append(temp)

        self.interval_sugars = [cocos.sprite.Sprite(pyglet.image.load('../res/minigame2/upper_sugar.png'), position=(2000,2000)) for i in range(0,19)]
        for index, sug in enumerate(self.interval_sugars):
            self.add(sug, 1)
            sug.do(Hide())


        self.reconfigure_dna(init=True)
        
        # for index, nucleotide in enumerate(self.dna):
        #     print('dddd')
        #     if not index == 19:
        #         self.position_sugar(self.interval_sugars[index], self.dna[index].spr.position, nucleotide.spr.position)

        for button in self.buttons.values():
            self.add(button, 2)

        for character in self.characters.values():
            self.add(character, 3)

        for nucleotide in self.dna:
            self.add(nucleotide, 2)

        self.add(bg, 0)

# methods
    def back(self):
        self.director.pop()
        print("select stage back")

    def position_sugar(self, sugar, block_coord, block2_coord,show=False, up=True):
        # angle_of_rotate = -math.degrees(math.atan2((block2_coord[1]-block_coord[1]),(block2_coord[0]-block_coord[0])))
        sugar.do(MoveTo(((block_coord[0]+block2_coord[0])/2, (block_coord[1]+block2_coord[1])/2), 0.5))
        sugar.do(RotateTo(-math.degrees(math.atan2((block2_coord[1]-block_coord[1]),(block2_coord[0]-block_coord[0]))), 0.5)+Show())

    def immediate_position_sugar(self, sugar, block_coord, block2_coord,show=False, up=True):
        # angle_of_rotate = -math.degrees(math.atan2((block2_coord[1]-block_coord[1]),(block2_coord[0]-block_coord[0])))
        sugar.do(MoveTo(((block_coord[0]+block2_coord[0])/2, (block_coord[1]+block2_coord[1])/2), 0)+Show())
        sugar.do(RotateTo(-math.degrees(math.atan2((block2_coord[1]-block_coord[1]),(block2_coord[0]-block_coord[0]))), 0))

    def put_a(self):
        self.put_block('a')

    def put_t(self):
        self.put_block('t')

    def put_c(self):
        self.put_block('c')

    def put_g(self):
        self.put_block('g')

    def put_block(self, letter):

        if self.game_counter < len(self.bases): 
            imgDir = ''
            
            self.button_to_assign = self.dna[self.game_counter]

            if self.game_counter > 9:
                self.img_to_assign='../res/minigame2/nucleotide_'+self.dna[self.game_counter].identity+letter+'.png'
                self.characters['polymerase'].work((536, 459), self.change_button_sprite, self.check_victory)
            else:
                self.img_to_assign='../res/minigame2/nucleotide_primer_'+self.dna[self.game_counter].identity+'.png'
                self.throw_ball(self.characters['primase'].spr.get_rect().center, (536, 459), self.change_button_sprite)

            if self.alive_nucleotides < 11:
                self.alive_nucleotides += 1
            else:
                self.buffer += 1

            self.game_counter += 1
            self.reconfigure_dna()

        else:
            self.back()
        # print(self.game_counter)

    def check_victory(self):
        if self.game_counter >= len(self.bases):
            self.victory_action()

    def change_button_sprite(self):
        try:
            self.button_to_assign.spr.image = pyglet.image.load(self.img_to_assign)
        except Exception as e:
            self.fail_action()

    def reconfigure_dna(self, init=False):


        if init:

            tempindex = self.alive_nucleotides
            for index, nucleotide in enumerate(self.dna):
                if index > self.alive_nucleotides:
                    return
                else: 
                    nucleotide.set_position(*self.do_list[tempindex])
                    nucleotide.enable()
                    if not tempindex == 0:
                        self.immediate_position_sugar(self.interval_sugars[index],self.do_list[tempindex],self.do_list[tempindex-1])
                        
                    tempindex -= 1


        else:

            th.start_new_thread(self.wait_thread_reconfigure, ())

    def throw_ball(self, throw_position, target_position, effect):
        ball = cocos.sprite.Sprite(pyglet.image.load('../res/minigame2/ball.png'), position=throw_position)
        self.add(ball)
        act = MoveTo(target_position, 0.5)+CallFunc(effect)+Hide()
        ball.do(act)

    def wait_thread_reconfigure(self):

        time.sleep(0.5)

        tempindex = self.alive_nucleotides # is the index of the position of the sprites
        # self.buffer
        maxx = self.alive_nucleotides+self.buffer
        minn = self.buffer

        for index, nucleotide in enumerate(self.dna):

            if not index in range(minn, maxx+1):
                    nucleotide.disable()
                    nucleotide.shift(2000,2000)
                    try:
                        # pass
                        self.position_sugar(self.interval_sugars[index],[2000,2000],[2000,2000])    
                    except Exception as e:
                        # raise e
                        print('lmao')
                    # print('disabled')                                          
            else:
                if not nucleotide.enabled:
                    nucleotide.enable()
                    # print('enabled')
                
                if nucleotide.spr.position == (2000,2000):
                    nucleotide.shift_then_show(*self.do_list[tempindex])                    
                else:
                    nucleotide.shift(*self.do_list[tempindex])
                

                # print(index)
                # print(nucleotide.spr.position)
                # print(self.dna[index+1].spr.position)
                if not tempindex == 0:
                    if self.do_list[tempindex][0] > 654:
                        # print('lampas naaa')
                        temp_coord = [self.do_list[tempindex][0],self.do_list[tempindex][1]]
                        temp_coord[1] = temp_coord[1]+60

                        temp_coord2 = [nucleotide.spr.position[0], nucleotide.spr.position[1]]
                        temp_coord2[1] = temp_coord2[1]+60

                        self.position_sugar(self.interval_sugars[index],temp_coord,temp_coord2)

                    elif self.do_list[tempindex][0] > 536:
                        
                        temp_coord = [self.do_list[tempindex][0],self.do_list[tempindex][1]]
                        temp_coord[1] = temp_coord[1]+60

                        self.position_sugar(self.interval_sugars[index],temp_coord,nucleotide.spr.position)

                    else:
                        # try:
                        self.position_sugar(self.interval_sugars[index],self.do_list[tempindex],nucleotide.spr.position)

                tempindex -= 1

            # if index%2==0:
            # print(index)


