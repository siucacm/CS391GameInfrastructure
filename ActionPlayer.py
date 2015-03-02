'''
Created on Feb 27, 2015

@author: SIU853541579
'''
from Player import *
from Vector2 import *
from CollisionManager import *
from Colors import *
import pygame

class ActionPlayer(Player):
    '''
    ActionPlayer is a top-down arena shooter player character
    It will move in simple up/down/left/right & diagonal patterns
    It will eventually shoot through vectors at the mouse 
    '''
    def __init__(self, x,y,width,height,vx,vy):
        Player.__init__(self,x,y,width,height,vx,vy)
        self.colBoxAnchorOffset = Vector2(0,0) #since we have no art, this can be 0,0
        self.collisionBox = CollisionManager.buildCollisionBox(self.position.x + self.colBoxAnchorOffset.x,
                                                              self.position.y + self.colBoxAnchorOffset.y,
                                                              width,height,
                                                              self)
        self.facing = Vector2(0,0)
        self.color = Color.cyan
    
    
    #input hooks
    def inputUpKeyAction(self):
        self.position.y -= self.velocity.y
        self.updateCollisionBox()
        
    def inputDownKeyAction(self):
        self.position.y += self.velocity.y
        self.updateCollisionBox()
        

    def inputRightKeyAction(self):
        self.position.x += self.velocity.x
        self.updateCollisionBox()
        
    def inputLeftKeyAction(self):
        self.position.x -= self.velocity.x
        self.updateCollisionBox()
    
    def inputAction1(self):
        pass
    #more to come
    
    def handleBoundHit(self, direction):
        #options:
        # - set up a flag preventing movement - basically turning off velocity in a direction
        # - set up a velocity backup variable and set velocity to 0?
        # - back the player up one velocity step
        if(direction[0] == -1):
            self.position.x += self.velocity.x
        elif(direction[0] == 1):
            self.position.x -= self.velocity.x
            
        if(direction[1] == -1):
            self.position.y += self.velocity.y
        elif(direction[1] == 1):
            self.position.y -= self.velocity.y
            
        self.updateCollisionBox()
    
    def drawIt(self,drawTarget):
        #using primitives for now ... sprites later
        pygame.draw.rect(drawTarget,self.color,self.toRect())
        self.collisionBox.debugDraw(drawTarget)
        
    
    def update(self, drawTarget, lowBound, upBound):
        #is our collisionmanger handling bound hits? ... should it?
        #print "Entered ActionPlayerUpdate"
        self.handleBoundHit(self.collisionBox.checkBoundHit(lowBound, upBound)) #derp ... 
        self.drawIt(drawTarget)
    