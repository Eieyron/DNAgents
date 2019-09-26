#select_level.py

#
#   SELECT MITOSIS LEVEL 
# a scene where you can select the mitosis stage you want to play
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet

# froms
from pyglet.window import key
from ui.movers.controlledmover import ControlledMover


# class imports
from ui.button import Button
from scenes.interphase import Interphase

# 
#   CLASS
# 


# definition
class SelectMitosisLevel(cocos.scene.Scene):

# init
    def __init__(self, director):
        
        self.director = director

        super().__init__()

        initBG = pyglet.image.load('../res/mitosis.PNG')
        self.initSprite = cocos.sprite.Sprite(initBG, position=(640,360))

        back_button = Button(65, 650, '../res/back.png', self, self.back)
        back_button.setHasHighlight('../res/back_h.png')

        interphase_button = Button(688, 571, '../res/interphase.png', self, self.on_interphase_select)

        prophase_button = Button(1066, 571, '../res/interphase.png', self, self.on_prophase_select)

        metaphase_button = Button(688, 367, '../res/interphase.png', self, self.on_metaphase_select)

        anaphase_button = Button(1066, 367, '../res/interphase.png', self, self.on_anaphase_select)

        telophase_button = Button(688, 160, '../res/interphase.png', self, self.on_telophase_select)

        cytokinesis_button = Button(1066, 160, '../res/interphase.png', self, self.on_cytokinesis_select)

        #   688 571     1066 571     
        #   688 367     1066 367
        #   688 160     1066 160
        
        self.add(back_button, 1)

        self.add(interphase_button,1)
        self.add(prophase_button, 1)
        self.add(metaphase_button, 1)
        self.add(anaphase_button, 1)
        self.add(telophase_button, 1)
        self.add(cytokinesis_button, 1)

        self.add(self.initSprite, 0)

# setters/getters

# methods
    def back(self):
        self.director.pop()
        print("mitosis back")

    def on_interphase_select(self):
        print("interphase")
        self.director.push(Interphase(self.director))

    def on_prophase_select(self):
        print("on_prophase_select")

    def on_metaphase_select(self):
        print("on_metaphase_select")

    def on_anaphase_select(self):
        print("on_anaphase_select")

    def on_telophase_select(self):
        print("on_telophase_select")

    def on_cytokinesis_select(self):
        print("on_cytokinesis_select")