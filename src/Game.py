# 
#   GameLauncher
# This class calls the MainMenu Class, it also passes the directorActions needed
# 

# 
#   IMPORT STATEMENTS
# 

# imports
import cocos
import pyglet
import _thread

# froms
from cocos.actions import *
from cocos.director import director
from pyglet.window import key

# class imports
from scenes.mainmenu import MainMenu
from scenes.minigame1 import MiniGame1
from scenes.minigame2 import MiniGame2
from scenes.minigame3 import MiniGame3

#
#   MAIN
#

def main():

    director.init(  width=1280,
                    height=720,
                    caption="DNAgents")
    
    director.window.pop_handlers()

    director.run(MainMenu(director))

if __name__ == '__main__':
    main()