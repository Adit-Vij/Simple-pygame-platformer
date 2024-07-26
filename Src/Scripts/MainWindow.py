import sys
import pygame
from Player import Player

#Initialize pygame
pygame.init()

#Window SetUp
window_w= 800
window_h= 600

window_size = (window_w,window_h)

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Sample")

#Create a Player Imstance
player = Player (window_w // 2, window_h // 2)

#Create sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Clock
clock = pygame.time.Clock()

#Main Loop
running = True

while running:
    dt = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys= pygame.key.get_pressed()
    all_sprites.update(keys, dt)
        
    window.fill((0,0,0))
    all_sprites.draw(window)
        
    pygame.display.flip()
        

pygame.quit()
sys.exit()