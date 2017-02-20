
import pygame
from pygame.locals import *
import os
import sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#screen dimensions
pygame.init()

#Finds the relative x to put an image in the middle of the screen
def screen_middle_x(screen,image):
    x = (screen.get_width()-image.get_width())/2
    return x

#Finds the relative y to put an image in the middle of the screen
def screen_middle_y(screen,image):
    y = (screen.get_height()-image.get_height())/2
    return y

def splash_screen(screen):
    main_running = True
    forwards = True

    background = pygame.Surface((screen.get_rect().width,screen.get_rect().height))
    background.fill(0)
    e = pygame.image.load("./resources/logo.png")
    e = e.convert()
    
    i=1
    while main_running == True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
        e.set_alpha(i)
        screen.blit(background,(0,0))
        screen.blit(e,(screen_middle_x(screen,e),screen_middle_y(screen,e)))
        pygame.time.wait(10)
        
        if forwards == True:
            i+=1
        else: 
            i-=1
        if i == 255:
            forwards = False
        elif i ==0:
            main_running = False
            pygame.time.wait(1000)
        pygame.display.update()
