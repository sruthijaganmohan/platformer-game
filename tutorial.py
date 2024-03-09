import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
from pygame.sprite import Group

pygame.init()
pygame.display.set_caption("Platformer")

BG_COLOR = (255, 255, 255)
WIDTH = 1000
HEIGHT = 800
FPS = 60
PLAYER_VELOCITY = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, v):
        self.x_velocity = -v
        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    def move_right(self, v):
        self.x_velocity = v
        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_velocity, self.y_velocity)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)

def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_velocity = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VELOCITY)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VELOCITY)


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles  = []
    for i in range (WIDTH//width + 1):
        for j in range (HEIGHT//height + 1):
            pos = (i*width, j * height)
            tiles.append(pos)
    return tiles, image


def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
    player.draw(window)
    pygame.display.update()




def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Purple.png")
    player = Player(100, 100, 50, 50)
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)