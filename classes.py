import os
import pygame
from main import * #import main python file

#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get.rect()
        self.rect.topleft = (x, y)

    #draw button on screen
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))