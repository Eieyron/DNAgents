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
STATIC = 0
STANDBY = 1
WALK_LEFT = 2
WALK_RIGHT = 3

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
    def __init__(self, position, objName, frames, collision_layers):
        
        self.name = objName
        self.sprites = []
        self.mapcolliders, self.collision_handlers = createMPCH(collision_layers)
        self.move_blocks = 0

        for name in os.listdir('../res/'+objName+'_sprite/'):
            if(name == objName+'_ss.png'):
                break
            self.sprites.append(pyglet.image.load('../res/'+objName+'_sprite/'+name))

        img = pyglet.image.load('../res/'+objName+'_sprite/'+objName+'_ss.png')
        ss = pyglet.image.ImageGrid(img, 1, frames, item_width=120, item_height=120)
        self.sprites.append(pyglet.image.Animation.from_image_sequence(ss[0:], 0.1, loop=True))

        super(MovingSprite, self).__init__(self.sprites[len(self.sprites)-1], position=position)

        # sprite state
        self.velocity = (0,0)
        self.onground = False
        self.jumping = False
        self.y_anchor = 0
        self.currentState = 0
        self.gravity = -500
 
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

    def setSprite(self, int):
        self.image = self.sprites[int]

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
        if obj.name == "portal":
            print("portal")
            self.portal_hit()
        elif obj.name == "button":
            print("button")
        elif obj.name == "chromatin":
            # obj.moveBy(120)
            if self.move_blocks != 0:
                for block in self.move_blocks:
                    if block.spr.name == "chromatin" and block.spr.tmxObj == obj:
                        block.spr.moveRight()
        elif obj.name == "centrosome":
            # obj.moveBy(120)
            if self.move_blocks != 0:
                for block in self.move_blocks:
                    if block.spr.name == "centrosome" and block.spr.tmxObj == obj:
                        block.spr.moveRight()
        else:
            print(obj.name)

    def interaction_block_collide_left(self, obj):
        if obj.name == "portal":
            self.portal_hit()
        elif obj.name == "button":
            pass
        elif obj.name == "chromatin":
            # obj.moveBy(120)
            if self.move_blocks != 0:
                for block in self.move_blocks:
                    if block.spr.name == "chromatin" and block.spr.tmxObj == obj:
                        block.spr.moveLeft()
        elif obj.name == "centrosome":
            # obj.moveBy(120)
            if self.move_blocks != 0:
                for block in self.move_blocks:
                    if block.spr.name == "centrosome" and block.spr.tmxObj == obj:
                        block.spr.moveLeft()
        else:
            print(obj.name)

    def interaction_block_collide_bottom(self, obj):
        # print(obj.name == "portal")
        if obj.name == "portal":
            self.portal_hit()
        elif obj.name == "button":
            pass
        else:
            print(obj.name)

    def interaction_block_collide_up(self, obj):
        # print(obj.name == "portal")
        if obj.name == "portal":
            self.portal_hit()
        elif obj.name == "button":
            pass
        else:
            print(obj.name)

    # set standby animation (default walk right)
    def collide_bottom(self, obj):
        self.setStandby(obj)
