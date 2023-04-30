# importing required library
import pygame
 
# activate the pygame library .
pygame.init()
X = 600
Y = 600





def viewImage(argument):
    scrn = pygame.display.set_mode((X, Y))
    pygame.display.set_caption(argument)
    imp = pygame.image.load(argument).convert()
     
    scrn.blit(imp, (0, 0))

    pygame.display.flip()
    status = True
    while (status):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
pygame.quit()