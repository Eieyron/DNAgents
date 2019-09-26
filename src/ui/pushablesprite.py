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

# class imports
GRAVITY = -300
AIR_RESIST = 100

class CollideHandler(WrappedMove):
    """docstring for Pusher"""
    def __init__(self, width, height, doesCollide):
        super(CollideHandler, self).__init__(width, height)
        self.doesCollide =  doesCollide
        
    def step(self, dt):

        xvel, yvel = self.target.velocity

        if self.doesCollide:

            if self.target.isMoving:

                if self.target.isMovingRight:
                    # print("self x", self.target.x, " >= ", self.target.x_anchor)
                    xvel += 1500 - (150 * self.target.move_counter)
                    if xvel < 0:
                        self.target.isMoving = False
                    elif xvel > 1700:
                        self.target.isMoving = False
                    else:
                        self.target.move_counter += 1
                else:
                    # print("self x", self.target.x, " < ", self.target.x_anchor)
                    xvel -= 1500 - (150 * self.target.move_counter)
                    if xvel > 0:
                        self.target.isMoving = False
                    elif xvel < -1700:
                        self.target.isMoving = False
                    else:
                        self.target.move_counter += 1
            
                xvel += AIR_RESIST * (-1 if self.target.isMovingRight else 1) 
                # print("air resist:",AIR_RESIST * (-1 if self.target.isMovingRight else 1))
            
            yvel += GRAVITY

            dx = xvel * dt
            dy = yvel * dt

            last = self.target.get_rect()

            new = last.copy()
            new.x += dx
            new.y += dy

            for ch in self.target.collision_handlers:

                # if the collision handler is for terrain, it will have an effect on the velocity of the object
                if ch.id == 0:
                    self.target.velocity = ch(last, new, xvel, yvel)

                # if the col_handler is for interaction blocks, it will still return the fact that the target hit the block
                elif ch.id == 1:
                    self.target.velocity = ch(last, new, *(self.target.velocity))

                # if the col_handler is for pass_through blocks, the velocity will not change
                elif ch.id == 2:
                    # pass
                    # print("",end='')
                    # ch(last, new, *(self.target.velocity))
                    cp_new = new.copy()

                    ch(last, cp_new, xvel, yvel)

            # # WRAP algorithm
            x, y = new.center
            w, h = self.target.width, self.target.height
            # XXX assumes center anchor
            if x > self.width + w/2:
                x -= self.width + w
            elif x < 0 - w/2:
                x += self.width + w
            if y > self.height + h/2:
                y -= self.height + h
            elif y < 0 - h/2:
                y += self.height + h
            self.target.position = (x, y)

            self.target.tmxObj._x, self.target.tmxObj._y = self.target.position

            # print(self.target.velocity)


# 
#   CLASS
# 

# constants
def createMPCH(collision_layers):
    # creates mapcolliders and collision handlers

    mps = [] # map colliders
    chs = [] # collision handlers for the user
    
    for index, layer in enumerate(collision_layers):
        mp = mapcolliders.TmxObjectMapCollider()
        mp.id = index
        mp.on_bump_handler = mp.on_bump_stick
        mps.append(mp)

        ch = mapcolliders.make_collision_handler(mp, collision_layers[index])
        ch.id = index
        chs.append(ch)

    return (mps, chs)

# definition
class PushableSprite(cocos.sprite.Sprite):
# init
    def __init__(self, tmxObj, objName, collision_layers, frames=8, pushable=True):
        
        self.sprites = []
        self.mapcolliders, self.collision_handlers = createMPCH(collision_layers)
        self.tmxObj = tmxObj
        self.name = objName

        for name in os.listdir('../res/'+objName+'_sprite/'):
            if(name == objName+'_ss.png'):
                break
            self.sprites.append(pyglet.image.load('../res/'+objName+'_sprite/'+name))

        img = pyglet.image.load('../res/'+objName+'_sprite/'+objName+'_ss.png')
        ss = pyglet.image.ImageGrid(img, 1, frames, item_width=120, item_height=120)
        self.sprites.append(pyglet.image.Animation.from_image_sequence(ss[0:], 0.1, loop=True))

        super(PushableSprite, self).__init__(self.sprites[len(self.sprites)-1], position=self.tmxObj.get_center())

        self.gravity = -500
        self.velocity = (0,0)
        self.isMoving = False
        self.isMovingRight = False
        self.move_counter = 0
        self.x_anchor = 0

        for collider in self.mapcolliders:

            if collider.id == 0:
                pass
            elif collider.id == 1:
                collider.collide_right = self.interaction_block_collide_right
                collider.collide_left = self.interaction_block_collide_left
            elif collider.id == 2:
                collider.collide_bottom = self.interaction_block_collide_bottom


        self.do(CollideHandler(1920, 1080, True))
            
# setters/getters


# methods
    def moveRight(self):
        self.isMoving = True
        self.isMovingRight = True
        self.move_counter = 0

    def moveLeft(self):
        self.isMoving = True
        self.isMovingRight = False
        self.move_counter = 0

    def portal_hit(self):
        self.opacity = 0

    def duplicate(self):
        # print(self.sprite )
        # print("what")
        pass
        # self.image = self.sprites[1]
        # self.velocity = (0,0)

    # interaction block methods
    def interaction_block_collide_right(self, obj):
        print(obj.name)
        if obj.name == "portal":
            print("portal")
            self.portal_hit()
        else:
            print(obj.name)

    def interaction_block_collide_left(self, obj):
        print(obj.name)
        if obj.name == "portal":
            print("portal")
            self.portal_hit()
        else:
            print(obj.name)

    def interaction_block_collide_bottom(self, obj):
        # print(obj.name)
        if obj.name == "duplicator":
            # self.duplicate()
            self.image = self.sprites[1]
            print("duplicates")
        else:
            print(obj.name)

    def interaction_block_collide_up(self, obj):
        pass
