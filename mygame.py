# filename: mygame.py
#
# Date: April 22, 2020
# Email: zachary.anderson@zenmakerlab.com
# purpose: To do cool stuff with pygame

import sys
import pygame
from pygame.locals import *

def main():
    print("Game is starting... ")
    
    pygame.init()
    size = width, height = 1280, 720
    black = 0,0,0
    vector = [1,1]
    w_pressed = False

    screen = pygame.display.set_mode(size) # sets screen size

    ghost = pygame.image.load("images/pika2.png") # loading the image of our character
    ghostrect = ghost.get_rect()

    player_rect = ghost.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    w_pressed = True
           
            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    w_pressed = False

        if w_pressed:
            player_rect = player_rect.move([1,0])
        
        ghostrect = ghostrect.move(vector)

        if ghostrect.left < 0 or ghostrect.right > width:
            vector[0] = -vector[0]
        if ghostrect.top < 0 or ghostrect.bottom > height:
            vector[1] = -vector[1]

        

        screen.fill(black) # Colors the whole screen black
        screen.blit(ghost, ghostrect) # Draws our ghost on the screen
        screen.blit(ghost, player_rect)
        pygame.display.flip() # Writes the next image to our window


if __name__ == "__main__":
    main()
