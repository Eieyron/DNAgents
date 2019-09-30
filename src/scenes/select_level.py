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
import _thread

# class imports
from scenes.select_mitosis_level import SelectMitosisLevel
from ui.button import Button

# 
#   CLASS
# 


# definition
class SelectLevel(cocos.scene.Scene):

# init
    def __init__(self, director):
        
        self.director = director

        super().__init__()

        initBG = pyglet.image.load('../res/selectStage.png')
        self.initSprite = cocos.sprite.Sprite(initBG, position=(640,360))

        back_button = Button(73, 651, '../res/back.png', self, self.back)
        back_button.setHasHighlight('../res/back_h.png')

        sel_mit = Button(381, 297, '../res/selectMitosis.PNG', self, self.on_mitosis_select)
        sel_mit.setHasHighlight('../res/selectMitosis_h.PNG')
        sel_mei = Button(892, 304, '../res/selectMeiosis.PNG', self, self.on_meiosis_select)
        sel_mei.setHasHighlight('../res/selectMeiosis_h.PNG')


        #   416 281
        #   890 281

        self.add(sel_mit, 1)
        self.add(sel_mei, 1)
        self.add(back_button, z=1)
        self.add(self.initSprite, z=0)

# setters/getters

# methods
    def back(self):
        self.director.pop()
        print("select stage back")


    def on_mitosis_select(self):
        print("mitosis")
        self.director.push(SelectMitosisLevel(self.director))

    def on_meiosis_select(self):
        print("meiosis")

