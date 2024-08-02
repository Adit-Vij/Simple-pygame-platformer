import pygame
import Platform

class Player (pygame.sprite.Sprite):
    def __init__(self,x: int,y: int, w: int, h: int ):
        super().__init__()
        self.vector =pygame.math.Vector2
        self.surface = pygame.Surface((w,h))
        self.surface.fill((134, 196, 243))
        self.rect = self.surface.get_rect(topleft = (x,y))
        self.pos = self.vector(x+(w/2),y)
        self.vel = self.vector(0, 0)
        self.acc = self.vector(0, 0)
        self.jumping = False
    
    def move(self, accelaration, friction, gravity):
        self.acc = self.vector(0, gravity)

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_a]:
            self.acc.x = -accelaration
        if pressed_key[pygame.K_d]:
            self.acc.x = accelaration

        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.bottomleft = self.pos
    
    def get_world_objects(self, player, platforms: pygame.sprite.Group):
        self._player = player
        self._platforms = platforms
        
    def update(self):
        hits = pygame.sprite.spritecollide(self._player,self._platforms,False)
        if self._player.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.jumping = False
                self.pos.y = hits[0].rect.top+1         

    def jump(self):
        hits = pygame.sprite.spritecollide(self._player,self._platforms,False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15
    
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump_handler(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.cancel_jump()