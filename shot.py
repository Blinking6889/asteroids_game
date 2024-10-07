import pygame

from circleshape import CircleShape
from constants import * 

class Shot(CircleShape):
    def __init__(self, x, y,radius, rotation):
        super().__init__(x,y, radius)
        self.velocity = pygame.Vector2(0, 1)
        self.rotation = rotation
        
    def draw(self, sobj):
        pygame.draw.circle(sobj,"white",self.position, self.radius, 2)

    def update(self, dt):
        forward = self.velocity.rotate(self.rotation)
        self.position += forward * PLAYER_SHOT_SPEED * dt


    def rotate(self, pr):
        self.rotation += pr
    
    def move(self, dt):
        forward = self.velocity.rotate(self.rotation)
        self.position += forward * PLAYER_SHOT_SPEED * dt
        
        

