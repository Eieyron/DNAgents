#
#   Static Sprite
# sprite that does not move
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import os, os.path

# froms

# class imports

# 
#   CLASS
# 

# constants

# definition
class StaticSprite(cocos.sprite.Sprite):
# init
    def __init__(self, position, objName, frames=8, tmxObj=0):
        
        self.sprites = []
        self.name = objName

        for name in os.listdir('../res/'+objName+'_sprite/'):
            if(name == objName+'_ss.png'):
                break
            self.sprites.append(pyglet.image.load('../res/'+objName+'_sprite/'+name))

        img = pyglet.image.load('../res/'+objName+'_sprite/'+objName+'_ss.png')
        ss = pyglet.image.ImageGrid(img, 1, frames, item_width=120, item_height=120)
        self.sprites.append(pyglet.image.Animation.from_image_sequence(ss[0:], 0.1, loop=True))

        super(StaticSprite, self).__init__(self.sprites[len(self.sprites)-1], position=position)

        
# setters/getters


# methods

