import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
background = pygame.Surface(screen.get_size())
background.fill([0,0,0])
clock = pygame.time.Clock()
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)


class Character(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/Vault_Boy_Stand.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    
    def move(self):
        if self.rect.left <= screen.get_rect().left or self.rect.right >=  screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos


my_character = Character('sprites\Vault_Boy_Stand.png', [10,0], [20,20])
pygame.time.set_timer(pygame.USEREVENT, 500)
held_down = False
direction = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            my_character.rect.centery = my_character.rect.centery + (30*direction)
            if my_character.rect.top <=0 or my_character.rect.bottom >= screen.get_rect().bottom:
                direction = -direction
        '''
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
            if held_down:
                my_character.rect.center = event.pos
        '''
        '''
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                my_character.rect.top = my_character.rect.top - 10
            elif event.key == pygame.K_s:
                my_character.rect.top = my_character.rect.top + 10
        '''
    clock.tick(20)
    screen.blit(background, (0,0))
    my_character.move()
    screen.blit(my_character.image, my_character.rect)
    pygame.display.flip()
pygame.quit()