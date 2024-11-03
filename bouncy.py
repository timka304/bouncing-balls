import pgzrun, pygame


TITLE = "Bouncy Ball"

HEIGHT = 600
WIDTH = 600

GRAVITY = 2000

class Ball():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.clr = ("blue")
        self.vx = 200
        self.vy = 0
        self.radius = r

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.clr)

#creating objects

ball = Ball(WIDTH/2, HEIGHT/2, 20)
ball2 = Ball(WIDTH/3, HEIGHT/3, 20)
ball3 = Ball(WIDTH/4, HEIGHT/4, 20)

def draw():
    screen.clear()
    ball.draw()
    ball2.draw()
    ball3.draw()

pgzrun.go()