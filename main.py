import pygame as pg, sys
from rocket import Rocket
from point import Point
from enemy import Enemy

class Game(object):
    def __init__(self):
        #configs
        self.tps_max = 100.0
        self.game = 0

        #init
        pg.init()
        self.screen = pg.display.set_mode((1080, 550))
        self.tps_clock = pg.time.Clock()
        self.tps_delta = 0.0
        self.player = Rocket(self)
        self.point = Point(self)
        self.enemy = Enemy(self)

        while True:
            #events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    sys.exit(0)

            #tic
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            # game mode 0-game, 1-game over
            if self.game == 1:
                self.over(self.player.score)
                pres=pg.key.get_pressed()
                if pres[pg.K_e]:
                    Game()
            if self.game == 0:
                # draw
                self.screen.fill((0, 0, 0))
                self.draw()
                pg.display.flip()


    def tick(self):
        self.player.tick()
        self.point.tick()
        self.enemy.tick()

    def draw(self):
        self.player.draw()
        self.point.draw()
        self.enemy.draw()

    def over(self, score):
        pg.display.set_caption("Game Over")
        self.screen.fill((20, 100, 0))
        txt = pg.font.Font(pg.font.get_default_font(), 30)
        txt_p = pg.font.Font(pg.font.get_default_font(), 20)
        text = txt.render("Your score: "+str(score), True, (0,0,0))
        text_p = txt_p.render("Press 'e' to play again", True, (0,0,0))
        self.screen.blit(text, text.get_rect())
        self.screen.blit(text_p, (0,100))
        pg.display.flip()


if __name__ == "__main__":
    Game()