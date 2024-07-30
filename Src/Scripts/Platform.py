import pygame

class Platform (pygame.sprite.Sprite):
    def __init__(self,x: int, y: int, w: int, h: int):
        super().__init__()
        self.surface = pygame.Surface((w,h))
        self.surface.fill((228, 89, 76))
        self.rectangle = self.surface.get_rect(topleft = (x,y))