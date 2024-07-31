import pygame
import Platform

class Player (pygame.sprite.Sprite):
    def __init__(self,x: int,y: int, w: int, h: int ):
        super().__init__()
        self.vector =pygame.math.Vector2
        self.surface = pygame.Surface((w,h))
        self.surface.fill((134, 196, 243))
        self.rectangle = self.surface.get_rect(topleft = (x,y))
        self.pos = self.vector(x+(w/2),y)
        self.vel = self.vector(0, 0)
        self.acc = self.vector(0, 0)
    
    def move(self, accelaration, friction, screen_width):
        self.acc = self.vector(0, 0.5)

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_a]:
            self.acc.x = -accelaration
        if pressed_key[pygame.K_d]:
            self.acc.x = accelaration

        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        
        self.rectangle.midbottom = self.pos
    
    def get_world_objects(self, player, platforms: pygame.sprite.Group, boolean):
        self._player = player
        self._platforms = platforms
        self._boolean = boolean
    


    def update(self):
        hits = pygame.sprite.spritecollide(PLAYER)
