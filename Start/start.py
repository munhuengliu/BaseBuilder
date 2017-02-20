
import pygame
from pygame.locals import *
import os
import sys
import splash

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#screen dimensions
pygame.init()
width, height = 640,480
window = pygame.display.set_mode((width,height))

#switch to run or not Run
running = True

#generic splash screen
splash.splash_screen(window)

while running:
    #red screen (R,G,B)
    window.fill(0)
    #Update Screen
    pygame.display.update()

#Controls and Events
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
