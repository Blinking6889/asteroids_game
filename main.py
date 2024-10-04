import pygame

from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    dt = clock.tick(60)/1000
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    #pg.containers = (updatable, drawable)
    p = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        #print(f'Attempting to draw player.')  
        for i in drawable:
            i.draw(screen)
        for i in updatable:
            p.update(dt)
        #pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 40)
        pygame.display.flip()

if __name__ == "__main__":
    main()