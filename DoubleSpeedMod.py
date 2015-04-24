'''
Created on Apr 24, 2015

@author: SIU853541579
'''
from ModEffect import *
from Vector2 import *
import pygame

class DoubleSpeedMod(ModEffect):
    '''
    classdocs
    '''


    def __init__(self):
        self.target = 0
        self.isAlive = True
        self.prevVelocity = 0
        self.newVelocity = 0
        self.modVal = 2
        self.lifeSpan = 3000 #3 seconds
        self.timer = pygame.time.get_ticks()
    
    def applyEffects(self, target):
        #print "picked up"
        self.target = target
        target.addMod(self)
        self.prevVelocity = target.velocity
        self.newVelocity = Vector2(self.prevVelocity.x * self.modVal,
                                   self.prevVelocity.y * self.modVal)
        target.velocity = self.newVelocity
        self.timer = pygame.time.get_ticks()
        self.isAlive = True
        #print target.velocity.x, target.velocity.y
        
    
    def monitorLifeCycle(self):
        #print "2X Speed monitor"
        if(pygame.time.get_ticks() - self.timer >= self.lifeSpan):
            self.target.velocity = self.prevVelocity
            self.isAlive = False
            
            
             
        