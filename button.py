import pygame

#button class
class Button():
    def __init__(self, x, y, image, altimage):
        self.image = image
        self.altimage = altimage
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def ispressed(self):
        self.image = self.altimage
    
    #drawing the button on the screen
    def draw(self, surface):
        action = False
        #checking to see if the mouse is clicked and then changing the button image to the pressed version
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.ispressed()
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action