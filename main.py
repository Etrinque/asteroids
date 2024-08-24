import pygame
from constants import *
from overlay import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}" + "\n" + f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0,0,0))
        display_fps()
        dt = clock.tick(60) / 1000
        
        pygame.display.flip()



if __name__ == "__main__":
    main()


