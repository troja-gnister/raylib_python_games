from settings import *


class Sprite:
    def __init__(self, texture, pos):
        self.texture = texture
        self.pos = pos


    def draw(self):
        draw_texture_ex(self.texture, self.pos, 0, SCALE, WHITE)
