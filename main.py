'''
Created on Feb 20, 2015

@author: SIU853541579
'''

import sys
import pygame
from CollisionManager import *
from PlayerInputManager import *
from ActionPlayer import *
from Colors import *
from Entity import *
from baseBullet import *
from BulletManager import *
from StationaryBlock import *
from PowerUp import *
from DoubleSpeedMod import *

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    myPlayer = PlayerInputManager.buildActionPlayer(pygame.K_w, 
                                                    pygame.K_s, 
                                                    pygame.K_a, 
                                                    pygame.K_d, 
                                                    pygame.K_SPACE, 
                                                    SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 
                                                    100, 100, 
                                                    5, 5)
    #debug routine  
    #for i in range(10):
    #    BulletManager.buildBaseBullet(10,10,1,1,i)
    
    testBlock = StationaryBlock(0, 0,
                                SCREEN_WIDTH/3, SCREEN_HEIGHT/3)
    test2XSpeed = PowerUp(SCREEN_WIDTH-250, SCREEN_HEIGHT-250, 50,50,
                          DoubleSpeedMod())
    while(True):
        screen.fill(Color.black)

        PlayerInputManager.update(pygame.key.get_pressed())
        #eventually we'll need the collision manager update here as well
        myPlayer.update(screen, [200,200], [SCREEN_WIDTH-200, SCREEN_HEIGHT-200])
        testBlock.update(screen)
        if(test2XSpeed.isAlive == True):
            test2XSpeed.update(screen)
        #else:
            #del test2XSpeed
            
        BulletManager.update(screen, [0,0], [SCREEN_WIDTH, SCREEN_HEIGHT])
        CollisionManager.update()
        
        msElapsed = clock.tick(30) #SYNC RATE 30 FPS
        pygame.display.update() #SYNC 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();


if __name__ == '__main__':
    main()