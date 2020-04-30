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

class mySprite():
    def __init__(self, image, name='', x=0, y=0 ):
        self.image = image
        self.rect = image.get_rect()
        self.rect = self.rect.move(x,y)
        self.name = name

class myEnemy(mySprite):
    def __init__(self, vector=[0,0]):
        super().__init__(image=pygame.image.load("images/ghost.png").convert_alpha())
        self.vector = vector

class myPlayer(mySprite):
    def __init__(self):
        super().__init__(image=pygame.image.load("images/pika2.png").convert_alpha())
        self.pressed = [False,False,False,False]
    
    def control(self, event):
       if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                self.pressed[0] = True 
            if event.key == K_s:
                self.pressed[1] = True 
            if event.key == K_d:
                self.pressed[2] = True 
            if event.key == K_a:
                self.pressed[3] = True

       if event.type == pygame.KEYUP:
            if event.key == K_w:
                self.pressed[0] = False
            if event.key == K_s:
                self.pressed[1] = False
            if event.key == K_d:
                self.pressed[2] = False
            if event.key == K_a:
                self.pressed[3] = False

       self.move()
    
    def move(self):
        if self.pressed[0]:
            self.rect = self.rect.move([0,-1])
        if self.pressed[1]:
            self.rect = self.rect.move([0,1])
        if self.pressed[2]:
            self.rect = self.rect.move([1,0])
        if self.pressed[3]:
            self.rect = self.rect.move([-1,0])

def main():
    print("Game is starting... ")
    
    pygame.init()
    size = width, height = 1280, 720
    black = 0,0,0
    sprites = []

    screen = pygame.display.set_mode(size) # sets screen size
    pygame.display.set_caption('My Crazy Game')

    sprites.append(myEnemy())
    player = myPlayer()
    sprites.append(player)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
       
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                player.pressed[0] = True 
            if event.key == K_s:
                player.pressed[1] = True 
            if event.key == K_d:
                player.pressed[2] = True 
            if event.key == K_a:
                player.pressed[3] = True

        if event.type == pygame.KEYUP:
            if event.key == K_w:
                player.pressed[0] = False
            if event.key == K_s:
                player.pressed[1] = False
            if event.key == K_d:
                player.pressed[2] = False
            if event.key == K_a:
                player.pressed[3] = False

            player.move()
        
        screen.fill(black) # Colors the whole screen black
        screen.blit(player.image, player.rect)
        pygame.display.flip() # Writes the next image to our window

if __name__ == "__main__":
    main()
