import os
import pygame # pyright: ignore[reportMissingImports]
from button import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#create game window
pygame.display.set_caption("Hospital Point and Click Game")
screen = pygame.display.set_mode((1440,810))
  
#importing images
#backgrounds
bg = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg, (1440,810))
#main menu buttons
newmain = pygame.image.load("images/newgamemain.png")
newmain = pygame.transform.scale(newmain, (450, 75))
pnewmain = pygame.image.load("images/newpressedmain.png")
pnewmain = pygame.transform.scale(pnewmain, (450, 75))
loadmain = pygame.image.load("images/loaddatamain.png")
loadmain = pygame.transform.scale(loadmain, (450, 75))
ploadmain = pygame.image.load("images/loadpressedmain.png")
ploadmain = pygame.transform.scale(ploadmain, (450, 75))
settingsmain = pygame.image.load("images/settingsmain.png")
settingsmain = pygame.transform.scale(settingsmain, (450, 75))
psettingsmain = pygame.image.load("images/settingspressedmain.png")
psettingsmain = pygame.transform.scale(psettingsmain, (450, 75))
quitmain = pygame.image.load("images/quitgamemain.png")
quitmain = pygame.transform.scale(quitmain, (450, 75))
pquitmain = pygame.image.load("images/quitpressedmain.png")
pquitmain = pygame.transform.scale(pquitmain, (450, 75))
#settings menu buttons
audio = pygame.image.load("images/audio.png")
audio = pygame.transform.scale(audio, (1150, 150))
saudio = pygame.image.load("images/noaudio.png")

#creating button objects
#main menu buttons
mnew = Button(750, 300, newmain, pnewmain)
mload = Button(750, 400, loadmain, ploadmain)
msettings = Button(750, 500, settingsmain, psettingsmain)
mquit = Button(750, 600, quitmain, pquitmain)
#settings menu buttons
audio1 = aButton(10, 10, saudio)


#def changeaudio(level):
    #for i in range(level):

def room1(): #game environment
    pygame.display.set_caption("Game Environment")

    running = True
    while running:

        mousepos = pygame.mouse.get_pos()
        screen.fill("black") #when i have finished drawing the background i will blit it here instead

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

def settings():
    pygame.display.set_caption("Settings Menu")

    running = True
    while running:
        
        game_display = screen.blit(bg, (0, 0))
        screen.blit(audio, (146, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

def main_menu(): #main menu function
    running = True
    while running:

        game_display = screen.blit(bg, (0, 0))
        if mnew.draw(screen):
            room1()
        if mload.draw(screen):
            print("Load Game button pressed")
        if msettings.draw(screen):
            settings()
        if mquit.draw(screen):
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

main_menu()