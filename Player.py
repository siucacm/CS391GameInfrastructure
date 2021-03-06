'''
Created on Feb 23, 2015

@author: SIU853541579
'''
from Entity import *

class Player(Entity):
    
    def __init__(self, x,y,width,height,vx,vy):
        '''
        Constructor
        '''
        Entity.__init__(self, x, y, width, height, vx, vy)
        self.type = "player"
        self.activeMods = []
        #I am an entity, so I have things like a collision box and offset, etc
        #however, I'm still an abstract so, I don't set those things yet
    
    #input hooks
    def inputUpKeyAction(self):
        pass
    def inputDownKeyAction(self):
        pass
    def inputRightKeyAction(self):
        pass
    def inputLeftKeyAction(self):
        pass
    
    def inputAction1(self):
        pass
    #more to come
    def addMod(self, effect):
        self.activeMods.append(effect)
        
    def monitorMods(self):
        i = len(self.activeMods)-1
        while i >= 0:
            self.activeMods[i].monitorLifeCycle()
            if self.activeMods[i].isAlive == False:
                self.activeMods.remove(self.activeMods[i])
            i-=1
            
    def handleBoundHit(self, direction):
        pass
    
    def update(self, drawTarget, lowBound, upBound):
        pass
    