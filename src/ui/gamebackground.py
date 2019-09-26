#
#   Game Background
# a 1920x1080 scrollable layer background
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet

# froms

# class imports

# 
#   CLASS
# 

# constants
TERRAIN = 0
TERRAIN_RECTANGLES = 1
INTERACTION_BLOCKS = 2
PASS_THROUGH = 3

def getTMXObjectCenter(tmxObj):
    return(tmxObj._x+(tmxObj._width/2),tmxObj._y+(tmxObj._height/2))

# definition
class GameBackground(cocos.layer.ScrollableLayer):

# init
    def __init__(self, picDir):
        super(GameBackground, self).__init__()
        
        img = pyglet.image.load(picDir)
        bg = cocos.sprite.Sprite(img, position=(img.width/2,img.height/2))

        self.px_width = img.width
        self.px_height = img.height

        self.add(bg)

class GameLayer:

    def __init__(self, phasename):

        maplayers = cocos.tiles.load("maps/"+phasename+".tmx")

        # get layers from maplayers
        self.layers = [layer for layer in maplayers.contents.values() if not isinstance(layer, dict)]

        # gets interaction blocks positions
        self.interaction_blocks = [block for block in self.layers[INTERACTION_BLOCKS].objects]

        # gets positions of pass-through blocks
        self.pass_through = [block for block in self.layers[PASS_THROUGH].objects]
            
        # for p in self.layers[INTERACTION_BLOCKS].objects:
        #     print(p.__class__)
        #     self.interaction_blocks[p.name] = p
        

# setters/getters

# methods
