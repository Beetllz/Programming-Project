import os
import pygame
import sys
from main import *

#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get.rect()
        self.rect.topleft = (x, y)

    #draw button on screen
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))