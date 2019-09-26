#
#   Interphase
# a scene where the interphase(stage) is rendered
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet

# froms
from ui.movers.controlledmover import ControlledMover
from ui.game_objects.user import User
from ui.game_objects.portal import Portal
from ui.game_objects.duplicator import Duplicator
from ui.game_objects.chromatin import Chromatin
from ui.game_objects.centrosome import Centrosome
from ui.gamebackground import GameBackground, GameLayer
from ui.floatingsprite import FloatingSprite
from ui.informationlayer import InformationLayer
from ui.button import Button
from cocos import mapcolliders
# from test import Test

# class imports

# 
#   CLASS
# 

# constants
TERRAIN = 0
TERRAIN_RECTANGLES = 1
INTERACTION_BLOCKS = 2


def createBlocks(self, layers, collision_layers):
    other_blocks = []
    user = 0

    for block in layers.interaction_blocks:
        if block.name == "user":
            user = User(*(block.get_center()),"niccleus", collision_layers)
            user.spr.portal_hit = self.back
            other_blocks.append(user)
        elif block.name == "portal":
            other_blocks.append(Portal(*(block.get_center()), "portal"))
        elif block.name == "chromatin":
            other_blocks.append(Chromatin(block, collision_layers))
        elif block.name == "centrosome":
            other_blocks.append(Centrosome(block, collision_layers))
        else:
            print(str(block.name)+" @ "+str(block.get_center()))

    for block in layers.pass_through:
        if block.name == "duplicator":
            other_blocks.append(Duplicator(*(block.get_center()), "duplicator"))
        else:
            print(str(block.name)+" @ "+str(block.get_center()))

    return user, other_blocks

# definition
class Interphase(cocos.scene.Scene):

    # is_event_handler = True

# init
    def __init__(self, director):

        self.director = director

        super().__init__()


        bg = GameBackground('../res/mitosis_stage_bg.png')
        
        layers = GameLayer('interphase')

        # terrain management
        collision_layers = layers.layers[1:]

        # blocks management
        user, move_blocks = createBlocks(self, layers, collision_layers)
        user.spr.move_blocks = move_blocks


        # add visible layers to the scroller
        scroller = cocos.layer.ScrollingManager()
        scroller.add(bg,0)
        scroller.add(layers.layers[TERRAIN],1)
        for block in move_blocks:
            scroller.add(block,1)

        # to be added to static layer
        test_layer = InformationLayer(scroller, user.spr)

        back_button = Button(65, 650, '../res/back.png', self, self.back)
        back_button.setHasHighlight('../res/back_h.png')


        # add movers to the scene
        self.add(back_button, 2)
        self.add(test_layer, 1)
        self.add(scroller, 0)
        self.add(ControlledMover(user.spr, scroller, doesCollide=True), 0)


# setters/getters    

# methods
    def back(self):
        self.director.pop()
