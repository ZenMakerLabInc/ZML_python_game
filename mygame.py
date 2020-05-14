# filename: mygame.py
#
# Date: April 22, 2020
# Email: zachary.anderson@zenmakerlab.com
# purpose: To do cool stuff with pygame

import sys
import pygame
from pygame.locals import *
import pygame.time as time
import pygame.font as font

#Relative speed of sprites to framerate
fps = 60 
sp = 800 / fps

class mySprite():
    def __init__(self, image, name='', x=0, y=0 ):
        self.image = image
        self.rect = image.get_rect()
        self.rect = self.rect.move(x,y)
        self.name = name

class myEnemy(mySprite):
    def __init__(self, vector=[0*sp,0*sp]):
        super().__init__(image=pygame.image.load("images/ghost.png").convert_alpha())
        self.vector = vector

class myPlayer(mySprite):
    def __init__(self):
        super().__init__(image=pygame.image.load("images/pika2.png").convert_alpha())
    
    def move(self, keys):
        if keys[K_w]:
            self.rect = self.rect.move([0,-sp])
        if keys[K_s]:
            self.rect = self.rect.move([0,sp])
        if keys[K_d]:
            self.rect = self.rect.move([sp,0])
        if keys[K_a]:
            self.rect = self.rect.move([-sp,0])

def main():
    print("Game is starting... ")
    
    pygame.init()
    size = width, height = 1280, 720
    black = 0,0,0
    sprites = []

    screen = pygame.display.set_mode(size) # sets screen size
    clock = pygame.time.Clock()
    pygame.display.set_caption('My Crazy Game')

    sprites.append(myEnemy())
    player = myPlayer()
    sprites.append(player)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill(black) # Colors the whole screen black
        screen.blit(player.image, player.rect)
        pygame.display.flip() # Writes the next image to our window   
        clock.tick(fps)

if __name__ == "__main__":
    main()
