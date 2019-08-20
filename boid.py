from p5 import Vector, stroke, circle, setup, draw, size, background, run

class Boid():
    def __init__(self, x,y, width,heigth):
        self.position = Vector(x,y)

    def show(self):
        stroke(255)
        circle((self.position.x, self.position.y), radius=10)
