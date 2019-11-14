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

#
#   CLASS
#


# definition

class MainMenu(cocos.scene.Scene):

# init

    def __init__(self, director):

        super().__init__()

        self.director = director

        initBG = pyglet.image.load('../res/startScreen.png')
        self.initSprite = cocos.sprite.Sprite(initBG, position=(initBG.width/2,initBG.height/2))

        menuItems = []
        menu = cocos.menu.Menu()
           
        menuItems.append(cocos.menu.MenuItem("New Game", self.on_new_game))
        menuItems.append(cocos.menu.MenuItem("Continue", self.on_info))
        menuItems.append(cocos.menu.MenuItem("Credits", self.on_credits))
        menuItems.append(cocos.menu.MenuItem("Quit", self.on_quit))

        menu.create_menu(menuItems, cocos.menu.shake(), cocos.menu.shake_back())
        menu.on_quit = self.on_quit
        menu.position = 150,-200

        self.add(menu, z=1)
        self.add(self.initSprite, z=0)

# methods

    def on_new_game(self):
        print("newgame")

        cutscene = Cutscene(self.director, 1, nextScene=MainGame(self.director, 'newgame'))
        self.director.push(cutscene)

    def on_info(self):
        print("continue")
        self.director.push(MainGame(self.director, 'continue'))

    def on_credits(self):
        print("credits")

    def on_quit(self):
        print("quit")
        self.director.window.close()

    def random(self):
        while True:
            print(self.keyboard)