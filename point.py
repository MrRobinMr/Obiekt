import pygame as pg, random
from pygame.math import Vector2

class Point(object):
    def __init__(self, game):
        #init
        self.game = game

        #set random position of point
        self.size = self.game.screen.get_size()
        self.pos = Vector2(random.randint(25, self.size[0]-25), random.randint(25, self.size[1])-25)

    def tick(self):
        pass

    def draw(self):
        pg.draw.circle(self.game.screen, (255, 255, 255), (int(self.pos.x),int(self.pos.y)), 5)

    def new(self):
        #set new random position after destroing
        self.pos = Vector2(random.randint(25, self.size[0]-25), random.randint(25, self.size[1])-25)