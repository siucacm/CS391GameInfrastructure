'''
Created on Mar 18, 2015

@author: SIU853541579
'''
from baseBullet import *
from BulletManager import *
import pygame

class MirvBullet(BaseBullet):
    '''
    classdocs
    '''
    def __init__(self, spawnX, spawnY, aimX, aimY, speed):
        '''
        Constructor
        '''
        BaseBullet.__init__(self, spawnX, spawnY, aimX, aimY, speed)
        self.delay = 400
        self.timing = pygame.time.get_ticks()
    
    def update(self, screen, lowBound, upBound):
        self.moveIt()
        self.handleBoundHit(self.collisionBox.checkBoundHit(lowBound, upBound))
        
        if(pygame.time.get_ticks() - self.timing >= self.delay):
            BulletManager.buildMirvBullet(self.position.x, 
                                          self.position.y,
                                          self.velocity.x *-1, 
                                          self.velocity.y *-1, self.speed)
        self.drawIt(screen)
            