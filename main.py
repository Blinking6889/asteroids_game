import pygame

from constants import *

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    dt = clock.tick(60)/1000
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))  
        pygame.display.flip()

if __name__ == "__main__":
    main()