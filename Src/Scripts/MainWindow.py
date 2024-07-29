import pygame

pygame.init()

vector =pygame.math.Vector2

WIDTH = 800
HEIGHT = 600
FPS = 60
ACCELERATION = 0.5
FRICTION = -0.12

FramesPerSecond = pygame.time.Clock()
displayWindow = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Platformer")