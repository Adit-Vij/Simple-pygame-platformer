import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x: int,y: int):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 700
        self.gravity = 150
        self.velocity_y = 0
        self.is_on_ground = False
        self.jump_strength = -2000
        self.is_jumping = False

        '''
        ----Variables Advanced For Advanced Features----
        '''
        self.dash_speed = 4000
        self.jump_dash_count = 0

    def update(self,keys,dt):
        #self.default_speed = self.speed
        self.move_speed = self.speed*dt
        jump_strength = self.jump_strength*dt
        gravity = self.gravity*dt
        dash_speed = self.dash_speed*dt
        #Movement Handling
        '''
        ----Basic Movement----
        Left, Right, Jump
        '''
        if keys[pygame.K_d]:    #Move Right
            self.rect.x += self.move_speed
        if keys[pygame.K_a]:    #Move Left
            self.rect.x -= self.move_speed
        if keys[pygame.K_SPACE] and self.is_on_ground:  #Jump Trigger
            self.is_jumping = True
        if self.is_jumping:    #Jump
            self.velocity_y = jump_strength
            self.is_jumping = False
            self.jump_dash_count += 2
        '''
        ----Advanced Movement----
        Jump Dash
        '''
        if keys[pygame.K_q] and self.jump_dash_count>1:    #Jump Dash
            self.rect.x += dash_speed
            self.jump_dash_count -= 1
            
        #Gravity
        self.velocity_y+= gravity
        self.rect.y += self.velocity_y

        #Ground Check
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.velocity_y = 0
            #self.jump_dash_count = 2
            self.is_on_ground = True
        else:
            self.is_on_ground = False

    def draw(self,surface):
        surface.blit(self.image,self.rect)