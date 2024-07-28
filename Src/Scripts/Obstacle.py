import pygame
from Player import Player

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x: int, y: int, w: int, h: int, player: Player):
        super().__init__()
        self.image = pygame.Surface((w,h))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-h
        self.player = player

    def update(self, keys, dt):
        if self.player.rect.colliderect(self.rect):
            '''
            ---Player is falling on the object---
            Checks: 
                -> Player's Y-Axis velocity is positive (falling)
                -> Player's bottom side is below the obstacle's top side 
                -> Player's top side is above obstacle's top side
            '''
            if self.player.velocity_y > 0 and self.player.rect.bottom > self.rect.top and self.player.rect.top < self.rect.top:
                self.player.rect.bottom = self.rect.top
                self.player.velocity_y = 0
                self.player.is_on_ground = True

            '''
            ---Player is pushing on the object from the below---
            Checks: 
                -> Player's Y-Axis velocity is negative (jumping)
                -> Player's top side is above the obstacle's bottom side 
                -> Player's bottom side is below obstacle's top side
            '''
            if self.player.velocity_y < 0 and self.player.rect.top < self.rect.top and self.player.rect.bottom > self.rect.bottom:
                self.player.rect.top = self.rect.bottom
                self.player.velocity_y = 0

            '''
            ---Player is pushing on the object from the left---
            Checks: 
                -> Player's right side is grater than obstacle's left side
                -> Player's left side is less than obstacle's left side
            '''
            if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.left:
                self.player.rect.right = self.rect.left
                self.player.move_speed = 0
            
            '''
            ---Player is pushing on the object from the right---
            Checks: 
                -> Player's left side is less than obstacle's right side
                -> Player's right side is greter than obstacle's right side
            '''
            if self.player.rect.left < self.rect.right and self.player.rect.right > self.rect.right:
                self.player.rect.left = self.rect.right
                self.player.move_speed = 0


    def draw(self,surface):
        surface.blit(self.image,self.rect)    