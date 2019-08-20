from p5 import Vector, stroke, circle
import numpy as np

class Boid():
    def __init__(self, x,y, width,heigth):
        self.position = Vector(x,y)

        #set velocity vector
        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = Vector(*vec)

        #set acceleration vector
        vec = (np.random.rand(2) - 0.5)*10
        self.acceleration = Vector(*vec)

    def show(self):
        stroke(255)
        circle((self.position.x, self.position.y), radius=10)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration
