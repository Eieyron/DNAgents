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
    def __init__(self, director):
        
        self.director = director

        super().__init__()

        bg = GameBackground('../res/minigame2/minigame2_background.png')        
        self.pos = [1280, 720]

        self.buttons = {}

        self.bases = 'atcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcggatcgg'
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

        self.reconfigure_dna(init=True)

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
                # self.img_to_assign = pyglet.image.load(imgDir)
                self.characters['polymerase'].work((536, 459), self.change_button_sprite)
            else:
                self.img_to_assign='../res/minigame2/nucleotide_primer.png'
                # self.img_to_assign = pyglet.image.load(imgDir)
                self.throw_ball(self.characters['primase'].spr.get_rect().center, (536, 459), self.change_button_sprite)
                # self.characters['primase'].work((536, 459), self.change_button_sprite)
            

            # time.sleep(0.5)    
            # self.dna[5].setSprite('../res/minigame2/nucleotide_primer.png')
            if self.alive_nucleotides < 11:
                self.alive_nucleotides += 1
            else:
                self.buffer += 1
            # self.alive_nucleotides += 1 if self.alive_nucleotides < 11 else 0
            

            self.game_counter += 1
            self.reconfigure_dna()

            # if self.game_counter >= len(self.bases):
            #     self.back

        else:
            self.back()
        # print(self.game_counter)

    def change_button_sprite(self):
        try:
            self.button_to_assign.spr.image = pyglet.image.load(self.img_to_assign)
        except Exception as e:
            self.back()

    def reconfigure_dna(self, init=False):


        if init:

            tempindex = self.alive_nucleotides
            for index, nucleotide in enumerate(self.dna):
                if index > self.alive_nucleotides:
                    return
                else: 
                    nucleotide.set_position(*self.do_list[tempindex])
                    nucleotide.enable()
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

        # print('tempindex', tempindex)
        # print('maxx', maxx)
        # print('minn', minn)

        for index, nucleotide in enumerate(self.dna):
            
            # print(index)

            if not index in range(minn, maxx+1):
                    nucleotide.disable()
                    nucleotide.shift(2000,2000)
                    # print('disabled')                                          
            else:
                if not nucleotide.enabled:
                    nucleotide.enable()
                    # print('enabled')
                
                if nucleotide.spr.position == (2000,2000):
                    nucleotide.shift_then_show(*self.do_list[tempindex])                    
                else:
                    nucleotide.shift(*self.do_list[tempindex])
                
                tempindex -= 1

        if self.game_counter >= len(self.bases):
            print('back')
            self.back()


