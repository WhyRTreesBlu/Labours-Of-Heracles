import sys, pygame

#pygame setup
pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, pygame.RESIZABLE) #thus creates the screen, automatically makes it full screen and resizable
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size() #this gives us the constants for screen width and height no matter what the size of the screen is
clock = pygame.time.Clock() #clock for like frames and stuff
running = True #is the game active?
dt = 0 #for caLculations independent of frame rate (not using yet)

heracles = pygame.image.load('Labours-Of-Heracles\media\images\heracles_temp.jpg') #loads the image for heracles
SPRITE_WIDTH, SPRITE_HEIGHT = heracles.get_size() #same thing as for the screen, gets the sprite width and height (sprite liekly to change later)
#level
background = pygame.image.load("Labours-Of-Heracles\media\images\g_temp.jpg") #loads the bg image
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scales it up to the size of the screen (may change later)
screen.blit(background, (0,0)) #puts the image onto the screen at 0,0 which is the top left, changes pixels to be that of the image

pygame.display.update() #makes all this graphics actually occur
#functions
def keyboard_input():
    #handles keyboard input pretty self explanatory
    keys = pygame.key.get_pressed()
    #vertical movement
    if keys[pygame.K_w]:
        player.move(up=True)
    if keys[pygame.K_s]:
        player.move(down=True)
    #horizontal movement
    if keys[pygame.K_a]:
        player.move(left=True)
    if keys[pygame.K_d]:
        player.move(right=True)
    #ending game with escape
    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))

#classses
class GameObject: #idk if we will use this, but i adapted it from a tutorial
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height) #gets the position and stuff for the image
    def move(self, left=False, right=False, up=False, down=False):
        #movement stuff, remember moving up and left is negative, down and right is positive
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed
        #stuff to stop going off screen
        if self.pos.right > SCREEN_WIDTH:
            self.pos.left = 0
        if self.pos.top > SCREEN_HEIGHT-SPRITE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < SPRITE_WIDTH:
            self.pos.right = SCREEN_WIDTH
        if self.pos.top < 0:
            self.pos.top = SCREEN_HEIGHT-SPRITE_HEIGHT

#player
player = GameObject(heracles, 76, 1) #creates the object


#mainline

while running:
    #break case
    for event in pygame.event.get(): #we can use events to activate things, in this case, pressing the escape key posts the quit event
        if event.type == pygame.QUIT: #the quit event is detected (think of it like a spotify queue, when posting an event it is added to the queue, you play the songs added to the queue first)
            running = False
            sys.exit() #quits the program
    screen.blit(background, player.pos, player.pos) #this puts the background image on top of the player image
    keyboard_input() #runs the function
    player.move() #the player moves
    screen.blit(player.image, player.pos) #the players new location adopts the sprite image
    pygame.display.update() #updates visuals
    clock.tick(60) #this happens 60 times a second