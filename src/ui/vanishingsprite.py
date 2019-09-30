#
#   Pushable Sprite
# sprite that is pushable
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import os, os.path
import time

# froms
from cocos.actions import *
from cocos import mapcolliders

# 
#   CLASS
# 

# constants

# definition
class VanishingSprite(cocos.sprite.Sprite):

# init
    def __init__(self, parent, tmxObj, objName, frames=8, pushable=True):
        
        self.name = objName
        self.sprites = {}
        self.tmxObj = tmxObj
        self.parent = parent

        for name in os.listdir('../res/'+objName+'_sprite/'):
            
            # loads the sprite and puts it in a spritesheet
            img = pyglet.image.load('../res/'+objName+'_sprite/'+name)
            frames = img.width // 120
            img = pyglet.image.ImageGrid(img, 1, frames, item_width=120, item_height=120)
            spritify = pyglet.image.Animation.from_image_sequence(img[0:], 0.1, loop=True)
            # self.sprites.append(spritify)

            # sets which sprites are active
            if(name == objName+'_static.png'):
                self.sprites['static'] = spritify

        super(VanishingSprite, self).__init__(self.sprites['static'], position=self.tmxObj.get_center())
  
# setters/getters


# methods
    def vanish(self):
        self.tmxObj._x, self.tmxObj._y = (2000,2000) # sets it apart
        # print(self.tmxObj.__dict__)
        self.parent.parent.remove(self.parent)