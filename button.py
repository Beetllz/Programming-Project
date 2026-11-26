import pygame
import time

#button class
class Button():
    def __init__(self, x, y, image, altimage):
        self.image = image
        self.temp = image
        self.altimage = altimage
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    #drawing the button on the screen
    def draw(self, surface):
        action = False
        #checking to see if the mouse is clicked and then changing the button image to the pressed version
        pos = pygame.mouse.get_pos()
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.image = self.altimage
        else:
            self.image = self.temp

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        surface.blit(self.image, (self.rect.x, self.rect.y))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action