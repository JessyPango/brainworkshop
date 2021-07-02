import pyglet
import time

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

#pyglet.options['audio'] = ('directsound', 'openal', 'alsa',)
source = pyglet.media.load('/home/jessy/brainworkshop/res/sounds/nato/o.wav')
print(source)

player = pyglet.media.Player()
player.queue(source)
#player.EOS_LOOP = 'loop'
player.play()

pyglet.app.run()
