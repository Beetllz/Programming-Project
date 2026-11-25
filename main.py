import os
import pygame # pyright: ignore[reportMissingImports]
import sys
import OOP

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#create game window
pygame.display.set_caption("Hospital Point and Click Game")
screen = pygame.display.set_mode((1440,810))

#importing images
#backgrounds
bg = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg, (1440,810))
#buttons
newmain = pygame.image.load("images/newgamemain.png")
pnewmain = pygame.image.load("images/newpressedmain.png")
loadmain = pygame.image.load("images/loaddatamain.png")
ploadmain = pygame.image.load("images/loadpressedmain.png")
settingsmain = pygame.image.load("images/settingsmain.png")
psettingsmain = pygame.image.load("images/settingspressedmain.png")
quitmain = pygame.image.load("images/quitgamemain.png")
pquitmain = pygame.image.load("images/quitpressedmain.png")

#creating button objects
newgame = Button(700, 400, newmain)

#game loop begins
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_display = screen.blit(bg, (0, 0))
    pygame.display.update()
