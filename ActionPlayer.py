'''
Created on Feb 27, 2015

@author: SIU853541579
'''
from Player import *
from Vector2 import *
from CollisionManager import *
from Colors import *
from MachineGun import *
import pygame
import math

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
        self.equipedGun = MachineGun(Vector2(self.position.x + self.dimensions.x/2,
                                             self.position.y + self.dimensions.y/2),
                                     Vector2(1,1))
        self.facing = Vector2(0,0)
        self.gunOrigin = Vector2(0,0)
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
        #print "actionplayer.actionkey1"
        self.calculateGunOrigin()
        
        self.equipedGun.update(self.gunOrigin,self.facing, True)
        self.equipedGun.shoot()
    #more to come
    
    #in our action game, we want to aim at the mouse
    #so we need the mouse location
    def calculateAimingVector(self):
        mousePos = Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        midPoint = Vector2(self.position.x + self.dimensions.x/2, 
                           self.position.y + self.dimensions.y/2)
        
        vector = Vector2(mousePos.x - midPoint.x, mousePos.y - midPoint.y)
        if(vector.x != 0 or vector.y != 0):
            size = math.sqrt(vector.x**2 + vector.y**2)
            self.facing.x = vector.x/size
            self.facing.y = vector.y/size
            
    def calculateGunOrigin(self):
        self.calculateAimingVector() #update aiming vector
        midPoint = Vector2(self.position.x + self.dimensions.x/2, 
                           self.position.y + self.dimensions.y/2)
        self.gunOrigin.x = midPoint.x + (self.facing.x * 75)
        self.gunOrigin.y = midPoint.y + (self.facing.y * 75)
    
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
        pygame.draw.circle(drawTarget, (255,255,0), 
                           (int(self.gunOrigin.x), int(self.gunOrigin.y)),
                           5)
        self.collisionBox.debugDraw(drawTarget)
        
    
    def update(self, drawTarget, lowBound, upBound):
        #is our collisionmanger handling bound hits? ... should it?
        #print "Entered ActionPlayerUpdate"
        self.handleBoundHit(self.collisionBox.checkBoundHit(lowBound, upBound)) #derp ... 
        self.drawIt(drawTarget)
        
    