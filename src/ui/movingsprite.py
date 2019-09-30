#
#   Moving Sprite
# sprite that moves
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
import os, os.path
import _thread

# froms
from cocos import mapcolliders

# class imports

# 
#   CLASS
# 

# constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
STATIC = 4

TERRAIN_RECTANGLES = 0
INTERACTION_BLOCKS = 1

def createMPCH(collision_layers):
    # creates mapcolliders and collision handlers
    mps = [] # map colliders
    chs = [] # collision handlers for the user
    
    for index, layer in enumerate(collision_layers):
        mp = mapcolliders.TmxObjectMapCollider()
        mp.id = index
        mp.on_bump_handler = mp.on_bump_bounce
        mps.append(mp)

        ch = mapcolliders.make_collision_handler(mp, collision_layers[index])
        ch.id = index
        chs.append(ch)

    return (mps, chs)

# definition
class MovingSprite(cocos.sprite.Sprite):
# init
    def __init__(self, position, objName, collision_layers):
        
        self.name = objName
        self.sprites = {}
        self.mapcolliders, self.collision_handlers = createMPCH(collision_layers)
        self.move_blocks = 0

        # sprite state
        self.velocity = (0,0)
        self.onground = False
        self.jumping = False
        self.y_anchor = 0
        self.currentState = 0
        self.gravity = -500
        self.face_stack = [] # stack for what position the sprite is facing
        self.faces_enabled = {  'left':False,
                                'right':False,
                                'up':False,
                                'down':False,
                                'static':False,
                                'none':False} # left, right, up, down -- a list that signifies which faces have sprites to be read
        
        for name in os.listdir('../res/'+objName+'_sprite/'):

            # loads the sprite and puts it in a spritesheet
            img = pyglet.image.load('../res/'+objName+'_sprite/'+name)
            frames = img.width // 120
            img = pyglet.image.ImageGrid(img, 1, frames, item_width=120, item_height=120)
            spritify = pyglet.image.Animation.from_image_sequence(img[0:], 0.1, loop=True)
            # self.sprites.append(spritify)

            # sets which sprites are active
            if(name == objName+'_left.png'):
                self.faces_enabled['left'] = True;
                self.sprites['left'] = spritify
            elif(name == objName+'_right.png'):
                self.faces_enabled['right'] = True;
                self.sprites['right'] = spritify
            elif(name == objName+'_up.png'):
                self.faces_enabled['up'] = True;
                self.sprites['up'] = spritify
            elif(name == objName+'_down.png'):
                self.faces_enabled['down'] = True;
                self.sprites['down'] = spritify
            elif(name == objName+'_static.png'):
                self.faces_enabled['static'] = True;
                self.sprites['static'] = spritify

        super(MovingSprite, self).__init__(self.sprites['static'], position=position)

 
        # collision
        
        # set collider functions
        for collider in self.mapcolliders:

            if collider.id == TERRAIN_RECTANGLES:
                collider.bumped_y = False # initialize bumped_y
                collider.collide_bottom = self.collide_bottom

            elif collider.id == INTERACTION_BLOCKS:
                collider.collide_right = self.interaction_block_collide_right
                collider.collide_left = self.interaction_block_collide_left
                collider.collide_bottom = self.interaction_block_collide_bottom
                collider.collide_up = self.interaction_block_collide_up


        # set collide map function
        self.collide_map = self.collision_handlers[TERRAIN_RECTANGLES]

# setters/getters
    def setStatic(self, obj):
        self.setSprite(0)
        self.currentState = 0
        self.onground = False

    def setStandby(self, obj):
        if self.currentState != len(self.sprites)-1:
            self.setSprite(len(self.sprites)-1)
            self.currentState = len(self.sprites)-1
            self.onground = True

    def setSprite(self, spriteName):
        # print('set sprite to',spriteName)
        if self.faces_enabled[spriteName]:
            self.image = self.sprites[spriteName]

    def reset(self):
        self.velocity = (0,0)
        self.onground = False
        self.currentState = 0

# methods
    def portal_hit(self):
        pass

    # interaction block methods
    def interaction_block_collide_right(self, obj):
        # print(obj)
        self.general_collide(obj)
        

    def interaction_block_collide_left(self, obj):
        
        self.general_collide(obj)

    def interaction_block_collide_bottom(self, obj):

        self.general_collide(obj)


    def interaction_block_collide_up(self, obj):
        
        self.general_collide(obj)

    def general_collide(self, obj):

        # general collide function

        if obj.name == "portal":
            print("portal")
            self.portal_hit()
        elif obj.name == "protein":
            # obj.moveBy(120)
            if self.move_blocks != 0:
                for block in self.move_blocks:
                    if block.spr.name == "protein" and block.spr.tmxObj == obj:
                        block.spr.vanish()
        else:
            print(obj.name)

    # set standby animation (default walk right)
    def collide_bottom(self, obj):
        # self.setStandby(obj)
        pass
