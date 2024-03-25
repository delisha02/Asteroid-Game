import pygame
import math
# set game window dimensions
sw = 800
sh = 800

# load the images
bg = pygame.image.load('asteroidsPics/starbg.png')
alienImg = pygame.image.load('asteroidsPics/alienShip.png')
playerRocket = pygame.image.load('asteroidsPics/spaceRocket.png')
star = pygame.image.load('asteroidsPics/star.png')
asteroid50 = pygame.image.load('asteroidsPics/asteroid50.png')
asteroid100 = pygame.image.load('asteroidsPics/asteroid100.png')
asteroid150 = pygame.image.load('asteroidsPics/asteroid150.png')

# set title of game window
pygame.display.set_caption('Asteroids')
# initialize the game window with sw,sh
win = pygame.display.set_mode((sw, sh))
# to control frame rate
clock = pygame.time.Clock()

gameover = False

class Player(object):
    def __init__(self):
        self.img = playerRocket
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh//2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img,self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
        

    def draw(self,win):
        #win.blit(self.img, [self.x, self.y, self.w,self.h])
        win.blit(self.rotatedSurf, self.rotatedRect)
    
    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x , self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine +self.w//2, self.y - self.sine * self.h//2)
        
    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x , self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine +self.w//2, self.y - self.sine * self.h//2)

    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x , self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine +self.w//2, self.y - self.sine * self.h//2)


# to draw bg image on game window
def redrawGameWindow():
    win.blit(bg,(0,0))
    player.draw(win)
    pygame.display.update() #  to make the changes visible on the screen.

player = Player()
run = True
while run:
    clock.tick(60)   # settting frame rate to 60
    if not gameover:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_UP]:
            player.moveForward()
    # iterates over all the events that have occurred since the last time the event queue was checked.
    for event in pygame.event.get():  # returns a list of all the events that have happened since the last call to pygame.event.get().
        if event.type == pygame.QUIT:
            run = False
    
    redrawGameWindow()
pygame.quit()   # pygame.QUIT event is triggered when the user attempts to close the game window (e.g., by clicking the close button or pressing Alt+F4 on Windows).