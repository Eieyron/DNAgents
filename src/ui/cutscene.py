#
#   Cutscene
# A scene that plays a video file
#

#
#   IMPORT STATEMENTS
#

# imports
import cocos
import pyglet
# pyglet.lib.load_library('avbin64')
# pyglet.have_avbin=True
import _thread as th
import time

# froms
from ui.button import Button
# class imports

# 
#   CLASS
# 

# constants
class VideoLayer (cocos.layer.Layer):
    def __init__(self, video_name):
        super(VideoLayer, self).__init__()

        source = pyglet.media.load(video_name)
        # print(source.__dict__)
        self.duration = source._duration
        print("vidlength is",self.duration )
        format = source.video_format
        if not format:
            print('No video track in this source.')
            return

        self.media_player = pyglet.media.Player()
        self.media_player.queue(source)
        self.media_player.volume = 0.005
        # self.media_player.play()

    def draw(self):
        self.media_player.get_texture().blit(0,0)

    def pause(self):
    	self.media_player.pause()

    def play(self):
    	self.media_player.play()

# definition
class Cutscene(cocos.scene.Scene):
	"""docstring for Cutscene"""
	def __init__(self, director, video_number, nextScene=None):
		super(Cutscene, self).__init__()

		self.director = director
		self.backscene = self.director.scene
		# self.profile = profile
		self.video_number = video_number
		self.videoDirectory = '../res/cutscenes/cutscene'+str(video_number)+'.mp4'
		self.nextScene = nextScene

		print("loading: ", self.videoDirectory)

		self.skipped = False

		# self.skippable = profile.get_cutscenes_watched()[video_number-1]

		self.skippable = True

		# print

		self.vidLayer = VideoLayer(self.videoDirectory)

		back_button = Button(83, 638, '../res/main_left.png', self, self.back)
		back_button.setHasHighlight('../res/main_left_h.png')

		if self.skippable:
			# print("skippable")
			skip_button = Button(1187, 638, '../res/main_right.png', self, self.skip)
			skip_button.setHasHighlight('../res/main_right_h.png')
			self.add(skip_button,1)

		self.add(back_button, 1)
		self.add(self.vidLayer, 0)

		self.vidLayer.play()
		th.start_new_thread( self.endChecker, (self.vidLayer.media_player, ) )


	def back(self):
		self.vidLayer.pause()
		self.director.pop()
		print("Cutscene back")
		# if self.do_misc:
		self.do_misc()

	def skip(self):
		self.vidLayer.pause()
		self.skipped = True
		print("skip skipped?",self.skipped)

		if self.nextScene:
			self.director.replace(self.nextScene)
		else:
			self.back()

		print("Cutscene skipped")

	def do_misc(self):
		pass

	def endChecker(self, mediaPlayer):

		print("Cutscene showing...")

		time.sleep(int(self.vidLayer.duration))
		self.vidLayer.pause()

		self.next_scene()

	def next_scene(self):

		# self.profile.set_skippable(self.video_number)
		print("next_scene skipped?",self.skipped)
		if not self.skipped:
			if self.nextScene:
				self.director.replace(self.nextScene)
			else:
				self.director.pop()
				self.do_misc()

	# def play(self):
	# 	self.vidLayer.play()


# init

# setters/getters

# methods

#
#   MAIN
#
