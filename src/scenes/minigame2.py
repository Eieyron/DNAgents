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

        self.buttons['back'] = Button(53,666, '../res/main_left.png', self, self.back)
        self.buttons['back'].setHasHighlight('../res/main_left_h.png')

        self.characters = {}
        self.characters['primase'] = Button(64,75, '../res/minigame2/primase_smol.png', self, self.back)
        self.characters['polymerase'] = Button(190,75, '../res/minigame2/polymerase_smol.png', self, self.back)


        self.popup_anchor = (640,360)
        self.buttons['A'] = Button(520,90,'../res/minigame2/nucleotide_a.png', self, self.put_a)
        self.buttons['T'] = Button(580,90,'../res/minigame2/nucleotide_t.png', self, self.put_t)
        self.buttons['C'] = Button(640,90,'../res/minigame2/nucleotide_c.png', self, self.put_c)
        self.buttons['G'] = Button(700,90,'../res/minigame2/nucleotide_g.png', self, self.put_g)

        self.dna = []
        # self.dna.append(Button())
        # init = 0
        for num, base in enumerate(self.bases):
            # if init
            # init += 1
            # if num < self.alive_nucleotides:
            temp = Button(2000,2000, '../res/minigame2/nucleotide_'+base+'.png', self, self.back)
            # print(self.bases[-init])
            # if init < 6:
            temp.identity = base
            temp.setHasInactive('../res/minigame2/nucleotide_hide.png')
            # init = False
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
                self.characters['primase'].work((536, 459), self.change_button_sprite)
            

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
            # time.sleep(0.5)

            # self.dna[self.game_counter-1].setSprite()
            # self.wait_thread_reconfigure(img)
                # time.sleep(0.12)

    def wait_thread_reconfigure(self):

        time.sleep(0.5)

        tempindex = self.alive_nucleotides # is the index of the position of the sprites
        # self.buffer
        maxx = self.alive_nucleotides+self.buffer
        minn = self.buffer

        print('tempindex', tempindex)
        print('maxx', maxx)
        print('minn', minn)

        for index, nucleotide in enumerate(self.dna):
            
            # print(index)

            if not index in range(minn, maxx+1):
                    nucleotide.disable()
                    nucleotide.shift(2000,2000)
                    print('disabled')                                          
            else:
                if not nucleotide.enabled:
                    nucleotide.enable()
                    print('enabled')
                
                
                nucleotide.shift(*self.do_list[tempindex])
                
                tempindex -= 1

        if self.game_counter >= len(self.bases):
            print('back')
            self.back()


