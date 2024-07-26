import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = y
        self.speed = 700
        self.gravity = 150
        self.velocity_y = 0
        self.is_on_ground = False
        self.jump_strength = -2000
        self.is_jumping = False 

    def update(self,keys,dt):
        move_speed = self.speed*dt
        jump_strength = self.jump_strength*dt
        gravity = self.gravity*dt

        if keys[pygame.K_d]:
            self.rect.x += move_speed
        if keys[pygame.K_a]:
            self.rect.x -= move_speed
        if keys[pygame.K_SPACE] and self.is_on_ground:
            self.is_jumping = True
        if self.is_jumping:
            self.velocity_y = jump_strength
            self.is_jumping = False

        #Gravity
        self.velocity_y+= gravity
        self.rect.y += self.velocity_y

        #Ground Check
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.velocity_y = 0
            self.is_on_ground = True
        else:
            self.is_on_ground = False

    def draw(self,surface):
        surface.blit(self.image,self.rect)