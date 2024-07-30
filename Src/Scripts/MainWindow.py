import sys
import pygame
from Player import Player
from Platform import Platform

pygame.init()

vector =pygame.math.Vector2

WIDTH = 800
HEIGHT = 600
FPS = 60
ACCELERATION = 0.5
FRICTION = -0.12

FramesPerSecond = pygame.time.Clock()
displayWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

#Initialize player
player = Player(0, HEIGHT-20, 64, 64)
player.pos = vector((10,385))
player.vel = vector(0,0)
player.acc = vector(0,0)
#Initialize floor
floor = Platform(WIDTH, HEIGHT, WIDTH, 20)

#Create Sprite Group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(floor)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    displayWindow.fill((0,0,0))

    for entity in all_sprites:
        displayWindow.blit(entity.surface, entity.rectangle)

    pygame.display.update()
    FramesPerSecond.tick(FPS)