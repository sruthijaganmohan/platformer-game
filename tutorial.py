import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()
pygame.display.set_caption("Platformer")

BG_COLOR = (255, 255, 255)
WIDTH = 1000
HEIGHT = 800
FPS = 60
PLAYER_VELOCITY = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)