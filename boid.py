from p5 import Vector, stroke, circle
import numpy as np
import random

class Boid():
    def __init__(self, x, y, width, heigth):
        self.position = Vector(x,y)
        self.width = width
        self.heigth = heigth
        self.max_speed = 10
        self.max_force = 1
        self.perception = 100

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

        if np.linalg.norm(self.velocity) > self.max_speed:
            self.velocity = self.velocity/np.linalg.norm(self.velocity)*self.max_speed

        self.acceleration = Vector(*np.zeros(2))

    def edges(self):
        if self.position.x > self.width:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = self.width

        if self.position.y > self.heigth:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = self.heigth

    #main behavior: 3/3
    # F = m * a (equal self.acceleration here)
    def align(self, boids, p=1):
        deviation = Vector(*np.zeros(2))
        total = 0
        avg_dir = Vector(*np.zeros(2))
        #check average direction(by boid.velocity)
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < self.perception*p:
                avg_dir += boid.velocity
                total += 1
        if total > 0:
            avg_dir = Vector(*(avg_dir/total))
            avg_dir = (avg_dir/np.linalg.norm(avg_dir))*self.max_speed
            deviation = avg_dir - self.velocity

        return deviation

    #barycent == center of mass
    #setup deviation by barycent of flok
    def cohesion(self, boids, p=1):
        deviation = Vector(*np.zeros(2))
        total = 0
        barycent = Vector(*np.zeros(2))
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < self.perception*p:
                barycent += boid.position
                total += 1
        if total > 0:
            barycent /= total
            barycent = Vector(*barycent)
            vec_to_com = barycent - self.position
            if np.linalg.norm(vec_to_com) > 0:
                vec_to_com = (vec_to_com/np.linalg.norm(vec_to_com)) * self.max_speed
            deviation = vec_to_com - self.velocity
            if np.linalg.norm(deviation) > self.max_force:
                deviation = (deviation/np.linalg.norm(deviation)) * self.max_force

        return deviation

    def separation(self, boids, p=1):
        deviation = Vector(*np.zeros(2))
        total = 0
        avg_dir = Vector(*np.zeros(2))
        for boid in boids:
            distance = np.linalg.norm(boid.position - self.position)
            if self.position != boid.position and distance < self.perception*p:
                delta_pos = self.position - boid.position
                delta_pos /= distance
                avg_dir += delta_pos
                total += 1
        if total > 0:
            avg_dir /= total
            avg_dir = Vector(*avg_dir)
            if np.linalg.norm(deviation) > 0:
                avg_dir = (avg_dir/np.linalg.norm(deviation))*self.max_speed
            deviation = avg_dir - self.velocity
            if np.linalg.norm(deviation) > self.max_force:
                deviation = (deviation/np.linalg.norm(deviation))*self.max_force

        return deviation

#    def percept_behavir(self, boids):
#        total = 0
#        ai = [1,1,1]
#        for boid in boids:
#            if np.linalg.norm(boid.position - self.position) < self.perception:
#                total += 1
#        if total > 3:
#            ai = [1,1,1]
#        return ai

    def behavir_commit(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)

        self.acceleration += alignment
        self.acceleration += cohesion
        self.acceleration += separation
