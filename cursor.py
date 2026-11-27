import pygame

#cursor class
class Cursor():
    def __init__(self, image):
        self.image = image
        self.root = pygame.display.get_surface()
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    #drawing the cursor to the root
    def draw(self):
        self.root.blit(self.image, (self.x, self.y))

    #updating the cursor so that it follows the player's mouse
    def update (self):
        self.x = pygame.mouse.get_pos()[0] -16 #-__ to make sure that the images
        self.y = pygame.mouse.get_pos()[1] -16 #tracks the player's mouse well
