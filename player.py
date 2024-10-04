import pygame

from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        #print(f"Player class has been called at {x} and {y}!")
        

# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,sobj):
        pygame.draw.polygon(sobj,"white",self.triangle(),2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED*dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            ndt = 0-dt
            self.rotate(ndt)

        if keys[pygame.K_d]:
            ndt = 0+dt
            self.rotate(ndt)
        
        if keys[pygame.K_w]:
            ndt = 0+dt
            self.move(ndt)

        if keys[pygame.K_s]:
            ndt = 0-dt
            self.move(ndt)
    
    
