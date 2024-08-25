import pygame
from constants import *
from overlay import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}" + "\n" + f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        SCREEN.fill(color=(0,0,0))
        display_fps()
        dt = clock.tick(60) / 1000
        player.update(dt)
        player.draw(SCREEN)

        pygame.display.flip()


if __name__ == "__main__":
    main()


