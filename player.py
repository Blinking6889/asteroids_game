import pygame

from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown_timer = 0
        
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
        
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown_timer <= 0:
                self.shoot(dt)
                self.shoot_cooldown_timer = PLAYER_SHOOT_COOLDOWN
        
        if self.shoot_cooldown_timer > 0:
            self.shoot_cooldown_timer -= dt
    
    def shoot(self, dt):
        shot = Shot(self.position[0],self.position[1],SHOT_RADIUS,self.rotation)
        print(f'Player Rotation: {self.rotation}\nOriginal Shot Rotation:{shot.rotation}')
        print(f'Updated Shot roation: {shot.rotation}')
        shot.update(dt)
    
    
