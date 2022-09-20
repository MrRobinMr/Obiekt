import pygame as pg, random
from pygame.math import Vector2

class Enemy(object):
    def __init__(self, game):
        #init
        self.game = game
        self.pos = []

    def tick(self):
        self.create()

    def draw(self):
        for pos in self.pos:
            pg.draw.rect(self.game.screen,(255, 0, 0), pg.Rect(int(pos[0]), int(pos[1]), 20, 20))

    def create(self):
        # set random position of point
        self.size = self.game.screen.get_size()
        while len(self.pos) < self.game.player.score:
            self.pos.append(Vector2(random.randint(25, self.size[0] - 25), random.randint(25, self.size[1]) - 25))