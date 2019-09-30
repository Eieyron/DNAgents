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
        self.media_player.get_texture().blit(320, 180)

    def pause(self):
    	self.media_player.pause()

    def play(self):
    	self.media_player.play()

# definition
class Cutscene(cocos.scene.Scene):
	"""docstring for Cutscene"""
	def __init__(self, director, videoDirectory, nextScene):
		super(Cutscene, self).__init__()
		self.director = director
		self.backscene = self.director.scene
		self.videoDirectory = videoDirectory
		self.nextScene = nextScene

		self.vidLayer = VideoLayer(self.videoDirectory)

		back_button = Button(83, 638, '../res/back.png', self, self.back)
		back_button.setHasHighlight('../res/back_h.png')

		self.add(back_button, 1)
		self.add(self.vidLayer, 0)

		self.vidLayer.play()
		th.start_new_thread( self.endChecker, (self.vidLayer.media_player, ) )


	def back(self):
		self.director.pop()
		self.vidLayer.pause()
		print("Cutscene back")

	def endChecker(self, mediaPlayer):

		print("Cutscene showing...")

		time.sleep(int(self.vidLayer.duration))
		self.director.replace(self.nextScene)


	# def play(self):
	# 	self.vidLayer.play()


# init

# setters/getters

# methods

#
#   MAIN
#
