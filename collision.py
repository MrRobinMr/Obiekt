from pygame.math import Vector2

def check(posa = Vector2(0,0), posb = Vector2(0,0)):
    if int(posa.x) in range(int(posb.x)-10, int(posb.x)+10) and int(posa.y) in range(int(posb.y)-10, int(posb.y)+10):
        return True
    else:
        return False

def checksome(posa, posb):
    for i in posa:
        if int(i.x) in range(int(posb.x) - 10, int(posb.x) + 10) and int(i.y) in range(int(posb.y) - 10, int(posb.y) + 10):
            return True