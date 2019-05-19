import pyglet
import config
import math
import numpy as np
from PIL import Image, ImageFilter

class Track():
    def __init__(self, *args, **kwargs):
        self.border_image = pyglet.image.load('assets\\images\\track1\\background.png')
        self.tarmac_image = pyglet.image.load('assets\\images\\track1\\tarmac.png')
        self.border_sprite = pyglet.sprite.Sprite(self.border_image, 0, 0)
        self.tarmac_sprite = pyglet.sprite.Sprite(self.tarmac_image, 0, 0)
        self.border_sprite.update(scale=1.3)
        self.tarmac_sprite.update(scale=1.3)
        self.getShape()

    def getShape(self):
        img = Image.open('assets\\images\\track1\\background.jpg')
        edges = img.filter(ImageFilter.FIND_EDGES)
        arr = np.array(edges)
        

    def draw_self(self):
        self.border_sprite.draw()
        self.tarmac_sprite.draw()
        # pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        # ('v2i', ([100, 150, 100,300 ]))
        # )