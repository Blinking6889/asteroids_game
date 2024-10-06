import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

    #Define Canvas Variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    dt = clock.tick(60)/1000

    #Define sprite groups
    #Player Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    #Asteroid Group
    agroup = pygame.sprite.Group()
    Asteroid.containers = (agroup, updatable, drawable)

    #AsteroidField Group
    afgroup = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    
    #pg.containers = (updatable, drawable)
    #Initialize player
    p = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))

    #Initialize Asteroid field
    aobj = AsteroidField()

    #Main Logic Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        #Update player frames
        for i in drawable:
            i.draw(screen)
        for i in updatable:
            i.update(dt)
        for i in agroup:
            if i.detectCollision(p) == True:
                print("Game Over!")
                exit()

        #Refresh display
        pygame.display.flip()

if __name__ == "__main__":
    main()