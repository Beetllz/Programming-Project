import os
import pygame # pyright: ignore[reportMissingImports]
from button import *
from cursor import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#create game window
pygame.display.set_caption("Hospital Point and Click Game")
screen = pygame.display.set_mode((1440,810))
transp = pygame.Surface((1440,810))
transp.fill((0,0,0))
transp.set_alpha(160)

timer = pygame.time.Clock()
fps = 30
playerx = 300
playery = 300
playerspeed = 4
xdirection = 0
ydirection = 0

up = pygame.K_w
down = pygame.K_s
left = pygame.K_a
right = pygame.K_d

keyaction = {
    up : "moveup",
    down : "movedown",
    left : "moveleft",
    right : "moveright",
}

#actionfunction = {
    #"moveup" : player.move_up,
    #"movedown" : player.move_down,
    #"moveleft" : player.move_left,
    #"moveright" : player.move_right,
#}

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
#pause menu buttons
resume = pygame.image.load("images/resume.png")
resume = pygame.transform.scale(resume, (350, 65))
presume = pygame.image.load("images/resumepressed.png")
presume = pygame.transform.scale(presume, (350, 65))
savedata = pygame.image.load("images/savedata.png")
savedata = pygame.transform.scale(savedata, (350, 65))
psavedata = pygame.image.load("images/savedatapressed.png")
psavedata = pygame.transform.scale(psavedata, (350, 65))
settingspause = pygame.image.load("images/settingspause.png")
settingspause = pygame.transform.scale(settingspause, (350, 65))
psettingspause = pygame.image.load("images/settingspressedpause.png")
psettingspause = pygame.transform.scale(psettingspause, (350, 65))
quitpause = pygame.image.load("images/quitgamepause.png")
quitpause = pygame.transform.scale(quitpause, (350, 65))
pquitpause = pygame.image.load("images/quitgamepressedpause.png")
pquitpause = pygame.transform.scale(pquitpause, (350, 65))
#inventory images
iinventory = pygame.image.load("images/inventory.png")
iinventory = pygame.transform.scale(iinventory, (1000, 540))
iback = pygame.image.load("images/iback.png")
iback = pygame.transform.scale(iback, (120, 80))
#inventory sprites
#cursor images

#creating cursor objects
c = Cursor(iback)

#creating button objects
#main menu buttons
mnew = Button(750, 300, newmain, pnewmain)
mload = Button(750, 400, loadmain, ploadmain)
msettings = Button(750, 500, settingsmain, psettingsmain)
mquit = Button(750, 600, quitmain, pquitmain)
#settings menu buttons
audio1 = aButton(10, 10, saudio, saudio)
#pause menu buttons
paresume = Button(570, 300, resume, presume)
pasave = Button(570, 375, savedata, psavedata)
pasettings = Button(570, 450, settingspause, psettingspause)
paquit = Button(570, 525, quitpause, pquitpause)
#inventory menu buttons
iback = Button(1120, 150, iback, iback)

def draw_player():
    pygame.draw.rect(screen, "yellow", (playerx, playery, 100, 100), 0)

def inventory():
    pygame.display.set_caption("Inventory")
    screen.blit(transp, (0,0))

    running = True
    while running:

        pygame.mouse.set_visible(0)
        screen.blit(iinventory, (240, 150))

        if iback.draw(screen):
            running = False

        c.draw()
        c.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

def pause(): #in game pause menu
    pygame.display.set_caption("Paused")
    screen.blit(transp, (0,0))

    running = True
    while running:

        pygame.mouse.set_visible(0)

        if paresume.draw(screen):
            running = False
        if pasave.draw(screen):
            print("save data menu opened")
        if pasettings.draw(screen):
            settings()
        if paquit.draw(screen):
            pygame.quit()
        
        c.draw()
        c.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()

def play(): #game environment
    pygame.display.set_caption("Game Environment")

    running = True
    while running:

        pygame.mouse.set_visible(0)
        timer.tick(fps)
        mousepos = pygame.mouse.get_pos()
        global playerx
        global playery
        global xdirection
        global ydirection
        screen.fill("white") #when i have finished drawing the background i will blit it here instead

        draw_player()
        c.draw()
        c.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == right:
                    xdirection = 1
                if event.key == left:
                    xdirection = -1
                if event.key == up:
                    ydirection = -1
                if event.key == down:
                    ydirection = 1
                if event.key == pygame.K_ESCAPE:
                    pause()
                if event.key == pygame.K_f:
                    inventory()
            if event.type == pygame.KEYUP:
                if event.key == right:
                    xdirection = 0
                if event.key == left:
                    xdirection = 0
                if event.key == up:
                    ydirection = 0
                if event.key == down:
                    ydirection = 0
        playerx += playerspeed * xdirection
        playery += playerspeed * ydirection

        pygame.display.update()

def settings():
    pygame.display.set_caption("Settings Menu")

    running = True
    while running:
        
        pygame.mouse.set_visible(0)
        game_display = screen.blit(bg, (0, 0))
        screen.blit(audio, (146, 250))

        c.draw()
        c.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

def main_menu(): #main menu function
    running = True
    while running:

        pygame.mouse.set_visible(0)
        game_display = screen.blit(bg, (0, 0))
        if mnew.draw(screen):
            play()
        if mload.draw(screen):
            print("Load Game button pressed")
        if msettings.draw(screen):
            settings()
        if mquit.draw(screen):
            running = False

        c.draw()
        c.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

main_menu()