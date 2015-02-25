'''
Created on Feb 20, 2015

@author: SIU853541579
'''

import sys
import pygame
from CollisionManager import *
from Colors import *
from Entity import *

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print "HI!"
    temp = CollisionManager.buildCollisionBox(0, 0, 10, 10, pygame.Rect(0,0,1,1))
    entityTest = Entity(10,10,100,100,2,2)
    CollisionManager.test()
    while(True):
        entityTest.debugDraw(screen)
        
        msElapsed = clock.tick(30) #SYNC RATE 30 FPS
    
        pygame.display.update() #SYNC 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();


if __name__ == '__main__':
    main()