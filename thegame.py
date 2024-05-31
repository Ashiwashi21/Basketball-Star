# import the module
import pygame
from pygame.locals import *
import random

# setting up the window
pygame.init()
Clock = pygame.time.Clock()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Basketball Star")

arrow_orig = pygame.image.load("thearrow.png").convert_alpha()
x_coord = 138.5
y_coord = 678

# make a ball class
class Ball (pygame.sprite.Sprite):
    
    def __init__ (self):
        super().__init__()
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("theball.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 604

class Hoop (pygame.sprite.Sprite):
    
    def __init__ (self):
        super().__init__()
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("thehoop.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = 658
        self.rect.y = 165

# make a group to add the ball
all_groups = pygame.sprite.Group()
ball = Ball()
all_groups.add(ball)

another_group = pygame.sprite.Group()
hoop = Hoop()
another_group.add(hoop)


angle = 0

# running events
run = True
while run:  
    
    angle += 2
    
    # closes the window only when user clicks "X"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # screen fill
    screen.fill((138, 183, 255)) 
    pygame.draw.circle(screen,(0,0,255),[138.5,679],46)

    
    # update the gropu location and draw it
    all_groups.update()
    all_groups.draw(screen)
    another_group.update()
    another_group.draw(screen)

    
    arrow_copy = pygame.transform.rotate(arrow_orig, angle)
    screen.blit(arrow_copy, (x_coord - int(arrow_copy.get_width() / 2), y_coord - int(arrow_copy.get_height() / 2)))
    
    # pole for the hoop
    pygame.draw.rect(screen, ([75,75,75]), pygame.Rect(850,125,25,600))
    
    # ground
    pygame.draw.rect(screen, ([124, 252, 0]), pygame.Rect(0,725,1000,75))
    pygame.draw.circle(screen, ([255,255,0]), [50,50], 100)
    
    # updates the screen
    pygame.display.update()
    Clock.tick(60)


    
pygame.quit()
