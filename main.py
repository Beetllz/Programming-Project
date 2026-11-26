import os
import pygame # pyright: ignore[reportMissingImports]
import button

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

#button class, included in main.py for now until I can move it to a seperate file to import it
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
    
#creating button objects
mnew = Button(750, 300, newmain, pnewmain)
mload = Button(750, 400, loadmain, ploadmain)
msettings = Button(750, 500, settingsmain, psettingsmain)
mquit = Button(750, 600, quitmain, pquitmain)

#game loop begins
running = True
while running:

    game_display = screen.blit(bg, (0, 0))
    if mnew.draw(screen):
        print("New Game button pressed")
    if mload.draw(screen):
        print("Load Game button pressed")
    if msettings.draw(screen):
        print("Settings button pressed")
    if mquit.draw(screen):
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
