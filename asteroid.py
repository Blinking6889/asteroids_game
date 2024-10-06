import pygame

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        #self.vect = (x,y)
        #print("Asteroid Object has been initialized")

    def draw(self, sobj):
        #print("Asteroid Object has been drawn")
        pygame.draw.circle(sobj,"white",self.position, self.radius, 2)

    def update(self, dt):
        #print("Asteroid Object has been updated")
        #forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += (self.velocity * dt)