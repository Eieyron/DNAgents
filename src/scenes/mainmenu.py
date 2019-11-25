# MainMenu.py

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import _thread

# class imports
from scenes.main_game import MainGame
from ui.cutscene import Cutscene
from ui.button import Button

#
#   CLASS
#


# definition

class MainMenu(cocos.scene.Scene):

# init

    def __init__(self, director):

        super().__init__()

        self.director = director

        initBG = pyglet.image.load('../res/start_screen.png')
        self.initSprite = cocos.sprite.Sprite(initBG, position=(initBG.width/2,initBG.height/2))

        menu_buttons = {}

        menu_buttons['play_game'] = Button(1127, 300, '../res/play_game.png',self,self.on_new_game)
        menu_buttons['play_game'].setHasHighlight('../res/play game_highlight.png') 
        menu_buttons['continue'] = Button(1127, 241, '../res/continue.png',self,self.on_continue)
        menu_buttons['continue'].setHasHighlight('../res/continue_highlight.png') 
        menu_buttons['about'] = Button(1127, 182, '../res/about.png',self,self.on_about)
        menu_buttons['about'].setHasHighlight('../res/about_highlight.png') 
        menu_buttons['credits'] = Button(1127, 123, '../res/credits.png',self,self.on_credits)
        menu_buttons['credits'].setHasHighlight('../res/credits_highlight.png') 
        menu_buttons['exit'] = Button(1127, 64, '../res/exit.png',self,self.on_quit)
        menu_buttons['exit'].setHasHighlight('../res/exit_highlight.png') 

        for button in menu_buttons.values():
            self.add(button, 1)

        # self.add(menu, z=1)
        self.add(self.initSprite, z=0)

# methods

    def on_new_game(self):
        print("newgame")

        cutscene = Cutscene(self.director, 1, nextScene=MainGame(self.director, 'newgame'))
        self.director.push(cutscene)

    def on_continue(self):
        print("continue")
        self.director.push(MainGame(self.director, 'continue'))

    def on_credits(self):
        print("credits")

    def on_about(self):
        print("about")

    def on_quit(self):
        print("quit")
        self.director.window.close()

    def random(self):
        while True:
            print(self.keyboard)