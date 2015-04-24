'''
Created on Apr 24, 2015

@author: SIU853541579
'''
from CollisionManager import *
from Entity import *
from ModEffect import *
import pygame


class PowerUp(Entity):

    def __init__(self, x, y, width, height, effect):
        Entity.__init__(self, x, y, width, height, 0, 0)
        self.colBoxAnchorOffset = Vector2(0,0) #since we have no art, this can be 0,0
        self.collisionBox = CollisionManager.buildCollisionBox(self.position.x + self.colBoxAnchorOffset.x,
                                                              self.position.y + self.colBoxAnchorOffset.y,
                                                              width,height,
                                                              self)
        self.modEffect = effect
        self.type = "powUp"
        self.color = Color.MediumSpringGreen
    
    def onHit(self, other, direction):
        self.isAlive = False
        self.modEffect.applyEffects(other)
        
    
    def drawIt(self, drawTarget):
        pygame.draw.rect(drawTarget,self.color,self.toRect())
        
    def update(self, drawTarget):
        self.drawIt(drawTarget)