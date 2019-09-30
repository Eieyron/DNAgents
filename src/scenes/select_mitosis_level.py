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
from ui.cutscene import Cutscene
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

        back_button = Button(83, 638, '../res/back.png', self, self.back)
        back_button.setHasHighlight('../res/back_h.png')

        interphase_button = Button(325, 444, '../res/mitosis_levels/interphase.png', self, self.on_interphase_select)
        interphase_button.setHasHighlight('../res/mitosis_levels/interphase_h.png')

        prophase_button = Button(638, 444, '../res/mitosis_levels/prophase.png', self, self.on_prophase_select)
        prophase_button.setHasHighlight('../res/mitosis_levels/prophase_h.png')

        metaphase_button = Button(950, 444, '../res/mitosis_levels/metaphase.png', self, self.on_metaphase_select)
        metaphase_button.setHasHighlight('../res/mitosis_levels/metaphase_h.png')

        anaphase_button = Button(325, 184, '../res/mitosis_levels/anaphase.png', self, self.on_anaphase_select)
        anaphase_button.setHasHighlight('../res/mitosis_levels/anaphase_h.png')

        telophase_button = Button(638, 184, '../res/mitosis_levels/telophase.png', self, self.on_telophase_select)
        telophase_button.setHasHighlight('../res/mitosis_levels/telophase_h.png')

        cytokinesis_button = Button(950, 184, '../res/mitosis_levels/cytokinesis.png', self, self.on_cytokinesis_select)
        cytokinesis_button.setHasHighlight('../res/mitosis_levels/cytokinesis_h.png')


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
        # self.director.push(Cutscene(self.director,'../res/interphase_cutscenes/cutscene1.mp4', Interphase(self.director)))

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