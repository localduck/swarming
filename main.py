from p5 import setup, draw, size, background, run
import numpy as np
from boid import Boid

width = 1000
heigth = 1000

flock = [Boid(*np.random.rand(2)*1000, width,heigth) for _ in range(20)]

def setup():
    #once call at RUN
    #set-up: canvas size
    size(width,heigth)

def draw():
    #everytime call event
    background(30,30,47)

    for boid in flock:
        boid.show()
        boid.behavir_commit(flock)
        boid.update()
        boid.edges()

#p5 calling: setup(),d draw() ...
run()
