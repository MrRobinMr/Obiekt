import pygame as pg, collision
from pygame.math import Vector2

class Rocket(object):
    i = 0
    def __init__(self, game):
        self.game = game
        self.speed = 1.0
        self.gravity = 0.5
        self.score = 0

        self.size = self.game.screen.get_size()

        self.pos = Vector2(self.size[0]/2, self.size[1]/2)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)


    def add_force(self, force):
        self.acc += force

    def tick(self):
        #input
        presed = pg.key.get_pressed()
        if presed[pg.K_w] and self.pos.y > 0:
            self.add_force(Vector2(0, -self.speed))
        if presed[pg.K_s] and self.pos.y < self.size[1]-25:
            self.add_force(Vector2(0, self.speed))
        if presed[pg.K_a] and self.pos.x > 25:
            self.add_force(Vector2(-self.speed, 0))
        if presed[pg.K_d] and self.pos.x < self.size[0]-25:
            self.add_force(Vector2(self.speed, 0))

        #physics
        self.vel *= 0.8
        if self.pos.y < self.size[1]-25:
            self.vel -= Vector2(0, -self.gravity)
        else:
            self.vel *= 0.9

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        #colision detection
        if collision.check(self.game.point.pos, self.pos):
            self.game.point.new()
            self.score += 1
        if collision.checksome(self.game.enemy.pos, self.pos):
            self.game.game = 1


    def draw(self):
        # Set score on window title
        pg.display.set_caption('Score: ' + str(self.score))
        #base triangle
        points = [Vector2(0, -10), Vector2(5, 5), Vector2(-5, 5)]
        #rotate points
        angle = self.vel.angle_to(Vector2(0, 1))
        points = [p.rotate(angle) for p in points]
        points = [Vector2(p.x, p.y*-1) for p in points]
        #add curent position
        points = [self.pos+p*2 for p in points]
        #draw triangle
        pg.draw.polygon(self.game.screen, (0, 100, 255), points)
