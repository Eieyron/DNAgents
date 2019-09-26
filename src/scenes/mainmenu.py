# MainMenu.py

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import _thread

# class imports
from scenes.select_level import SelectLevel

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

        # try:
        #    _thread.start_new_thread( self.random, () )
        # except:
        #    print("Error: unable to start thread")
           
        menuItems.append(cocos.menu.MenuItem("Start", self.on_new_game))
        menuItems.append(cocos.menu.MenuItem("Info", self.on_info))
        menuItems.append(cocos.menu.MenuItem("Credits", self.on_credits))
        menuItems.append(cocos.menu.MenuItem("Quit", self.on_quit))

        menu.create_menu(menuItems, cocos.menu.shake(), cocos.menu.shake_back())
        menu.position = -400,-80

        self.add(menu, z=1)
        self.add(self.initSprite, z=0)

# methods

    def on_new_game(self):
        print("newgame")
        self.director.push(SelectLevel(self.director))

    def on_info(self):
        print("info")

    def on_credits(self):
        print("credits")

    def on_quit(self):
        print("quit")
        self.director.window.close()

    def random(self):
        while True:
            print(self.keyboard)