#
#   BUTTON
# An abstraction of a button where you can change the 
#   button position
#   hover sprite
#   action  
#

#
#   IMPORT STATEMENTS
#

# imports

import cocos
import pyglet
import copy
import _thread as th
import os

# froms
from cocos.actions import *
from pyglet.window import key


# 
#   CLASS
# 

# constants

class KeyMove(cocos.actions.Move):

    def step(self, dt):
        super(KeyMove, self).step(dt)
        # print(keys)
        xvel = ((key.RIGHT in keys) - (key.LEFT in keys)) * 50
        yvel = ((key.UP in keys) - (key.DOWN in keys)) * 50
        self.target.velocity = (xvel, yvel)
        print(self.target.position)

# definition

class Button(cocos.layer.Layer):

    is_event_handler = True

    # init

    def __init__(self, x, y, picDir, parent, action, isSpriteSheet=False, name=None, toAdjust=False):
        global keys, container

        # is_event_handler = toAdjust

        keys = set()
        container = parent

        self.toAdjust = toAdjust
        self.parent = parent
        self.action = action
        self.name = name

        self.origin_position = (x,y)

        self.highlight = False
        self.hasLabel = False
        self.hidden = False
        self.enabled = True
        self.hasInactiveSprite = False
        self.hasClickedSprite = False
        self.hasProjection = False

        super().__init__()

        img = pyglet.image.load(picDir)
        self.image = img        
        # frames = img.width // img.height
        #     # print(frames)
        # img = pyglet.image.ImageGrid(img, 1, frames, item_width=img.width, item_height=img.height)
        # spritify = pyglet.image.Animation.from_image_sequence(img[0:], 0.25, loop=True)

        if isSpriteSheet: #is not square
            frames = img.width // img.height
            # print(frames)
            img = pyglet.image.ImageGrid(img, 1, frames, item_width=img.height, item_height=img.height)
            im2 = pyglet.image.Animation.from_image_sequence(img[0:], 0.25, loop=True)
            self.image = im2
    
        self.spr = cocos.sprite.Sprite(self.image, position=(x,y))
        self.spr.velocity = (0,0)

        self.onHover = False

        self.add(self.spr, 1)

        if toAdjust:
            self.spr.do(KeyMove())

    # setters/getters

    # general button methods
    def setHasHighlight(self, picDir):
        self.highlight = True
        self.image_h = pyglet.image.load(picDir)

    def setHasInactive(self, picDir):
        self.hasInactiveSprite = True
        self.image_i = pyglet.image.load(picDir)
        self.disable()

    def setHasClicked(self, picDir):
        self.hasClickedSprite = True 
        self.image_c = pyglet.image.load(picDir)

    def setHasLabel(self, label):
        self.hasLabel = True
        pos = (self.spr.position[0]+50, self.spr.position[1]-50)
        self.label = cocos.text.Label(str((label if label != 0 else "")),font_name="Agency FB", font_size=25, anchor_x='center', anchor_y='center', position=pos)
        # print("label enabled @",pos," with color ",self.label.element.)
        return self

    def setHasProjection(self, picDir, position=(640,360)):
        self.hasProjection = True
        pos = self.spr.position
        pos = (pos[0]-15, pos[1]+216)
        self.project_sprite = cocos.sprite.Sprite(pyglet.image.load(picDir), position=pos)
        self.project_sprite.do(Hide())
        self.add(self.project_sprite, 0)

    # button movement methods
    def set_position(self, x, y):
        self.spr.do(MoveTo((x,y),0))
        
    def shift(self, x, y): # 0.5
        self.spr.do(MoveTo((x,y),0.5))

    def shift_then_show(self, x, y): # 0.5
        self.spr.do(Hide()+MoveTo((x,y),0.5)+Show())

    def work(self, pos, work, extra_work): # 0.75
        # self.set_image = img
        # origin = self.spr.position
        work = MoveTo(pos,0.5)+CallFunc(work)+MoveTo(self.origin_position,0.25)+CallFunc(extra_work)

        self.spr.do(work)

    def move_right_inf(self):
        repeat_forever = Repeat(MoveBy((50, 0),0.25))
        self.spr.do(repeat_forever)

    def move_up_and_down(self):
        repeat_forever = Repeat(MoveBy((0, 12),0.75)+MoveBy((0, -12),0.75))
        self.spr.do(repeat_forever)

    def finish_moving(self, work):
        repeat_forever = MoveBy((-1280, 0),3)+CallFunc(work)
        self.spr.do(repeat_forever)

    def deploy(self, target):
        self.target = target
        # move = Show()+MoveTo((970,83),0.75)+Repeat(MoveBy((50, 0),0.25))
        move = Show()+MoveTo((970,83),0.75)+CallFunc(self.deploy_if_hit_target)
        self.spr.do(move)

    def clicked(self):
        self.spr.do(CallFunc(self.change_sprite_when_clicked))

    def change_sprite_when_clicked(self):
        self.spr.image = self.image_c

    def click_sprite(self):
        self.spr.image = self.image_c

    def release_sprite(self):
        self.spr.image = self.image

    # def push_button(self, button):

    def deploy_if_hit_target(self):

        if self.spr.get_rect().intersects(self.target.spr.get_rect()):
            self.target.spr.do(Show())
            print('success')
            self.target_hit_action()

        else:
            print('failed')
            self.target_miss_action()
        
        self.spr.do(Hide())

    def target_hit_action(self):
        pass

    def target_miss_action(self):
        pass
            # return
        # print('failed')

    def new_label(self, label):
        pos = (self.spr.position[0]+50, self.spr.position[1]-50)
        newlabel = cocos.text.Label(str((label if label != 0 else "")),font_name="Agency FB", font_size=25, anchor_x='center', anchor_y='center', position=pos)

        self.label.parent.add(newlabel)
        self.label.parent.remove(self.label)
        self.label = newlabel
        self.label.do(Hide())

    # def setVelocity(self, point):
    #     self.velocity = point

    # methods
    def on_mouse_motion(self, x, y, dx, dy):
        if not self.enabled:
            return
        if (not self.onHover) and self.spr.contains(x,y):
            self.onHover = True
            if self.highlight:
                self.setSprite(self.image_h)
            if self.hasProjection:
                self.project_sprite.do(Show())

        elif self.onHover and (not self.spr.contains(x,y)):
            self.onHover = False
            if self.highlight:
                self.setSprite(self.image)
            if self.hasProjection:
                self.project_sprite.do(Hide())


    def on_mouse_press(self, x, y, button, mod):
        # print("buttin is disabled")
        if self.onHover and self.enabled and not self.hidden:
            # self.onHover = False
            self.action()
            if self.hasClickedSprite:
                self.click_sprite()


    def on_mouse_release(self, x, y, button, mod):
        if self.hasClickedSprite:
            self.release_sprite()

    def on_key_press(self, key, modifiers):
        global keys
        if self.toAdjust:
            keys.add(key)


    def on_key_release(self, key, modifiers):
        global keys
        if self.toAdjust:
            keys.remove(key)

    def setSprite(self, img=None, imgDir=None):
        if imgDir:
            self.spr.image = pyglet.image.load(imgDir)
        else:
            self.spr.image = img

    # def setSetSprite(self):
    #     self.spr.image = self.set_image

    def thread_action(self):
        pass

    # def change_sprite(self, img):
    #     new = copy.deepcopy(self.spr)
    #     new.image = img
    #     self.spr = new.spr

    def setSpriteandLabel(self, img, label):
        self.setSprite(img)
        # print(self.label.__dict__)
        self.new_label(label)
        # self.label.element._document._text = str(label)
        # print(self.label.element._document._text)

    def enable(self):

        # print(self.name,"enabled")
        if self.hasInactiveSprite and not self.enabled:
            if self.onHover:
                self.spr.image = self.image_h
            else:
                self.spr.image = self.image
        self.enabled = True


    def disable(self):
        # print(self.name,"disabled")
        if self.hasInactiveSprite and self.enabled:
            self.spr.image = self.image_i
        self.enabled = False

    def hide(self):
        self.hidden = True
        self.spr.do(Hide())
        if self.hasLabel:
            self.label.do(Hide())

    def show(self):
        self.hidden = False
        self.spr.do(Show())
        if self.hasLabel:
            self.label.do(Show())


    # def start_checker(self):
    #     while 1:

