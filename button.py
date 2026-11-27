import pygame

#button class
class Button():
    def __init__(self, x, y, image, altimage):
        #assigninh attri
        self.image = image
        self.temp = image
        self.altimage = altimage
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    #drawing the button on the screen
    def draw(self, surface):
        action = False
        #checking to see if the mouse is hovering over the button and then changing it to the alternate image if it is
        pos = pygame.mouse.get_pos()
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.image = self.altimage
        else:
            self.image = self.temp

        #checking for if the button is clicked and returning the True value
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        surface.blit(self.image, (self.rect.x, self.rect.y))

        #this allows buttons to be clicked more than once when running the program
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action #returns True when a button has been clicked

#creating a second button class, where the draw method instead changed
#the image of the button when it is clicked not when it is hovered over.
class aButton(Button):
    
    #when the button is pressed it will change to the altenate image using this function
    def ispressed(self):
        self.image = self.altimage

    #checking to see if the button has been clicked, changing how the image
    #looks and returning a True if it has been
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            action = True
            aButton.ispressed()
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action