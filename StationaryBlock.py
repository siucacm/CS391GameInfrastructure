'''
Created on Apr 24, 2015

@author: SIU853541579
'''
import pygame
from Entity import *
from Colors import *
from CollisionManager import *

class StationaryBlock(Entity):
    '''
    classdocs
    '''


    def __init__(self, x, y, width, height):
        '''
        Constructor
        '''
        Entity.__init__(self, x, y, width, height, 0, 0)
        self.colBoxAnchorOffset = Vector2(0,0) #since we have no art, this can be 0,0
        self.collisionBox = CollisionManager.buildCollisionBox(self.position.x + self.colBoxAnchorOffset.x,
                                                              self.position.y + self.colBoxAnchorOffset.y,
                                                              width,height,
                                                              self)
        self.type = "block"
        self.color = Color.yellow
        
    
    def onHit(self,other, direction):
        if direction[0] == -1:
            #self got hit on the left
            other.position.x = self.position.x - other.dimmensions.x
        
        elif direction[0] == 1:
            other.position.x = self.position.x + self.dimensions.x
        
        if direction[1] == -1:
            #self got hit on the left
            other.position.y = self.position.y - other.dimmensions.y
        
        elif direction[1] == 1:
            other.position.y = self.position.y + self.dimensions.y
        
    def drawIt(self, drawTarget):
        pygame.draw.rect(drawTarget,self.color,self.toRect())
        
    def update(self, drawTarget):
        self.drawIt(drawTarget)