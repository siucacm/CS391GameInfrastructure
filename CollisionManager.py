'''
Created on Feb 20, 2015

@author: SIU853541579
'''
from CollisionBox import *

class CollisionManager():
    '''
    CollisionManger
    This class will provide factories for building collision boxes
    It will also maintain all collisions in our game
    The entities will not run collisions, the manager will
    When a collision happens, the entity will be informed of the who/how 
        and be told to deal with it /sunglasses
        
    The collision manager will contain a list of all collisionBoxes in the game
    The collision manager should use a lot of static functions so we don't have to have an object for it
    
    '''
    
    #collision list
    collisionList = []
    
    @staticmethod
    def buildCollisionBox(x,y,width,height,owner):
        temp = CollisionBox(x,y,width,height, owner)
        CollisionManager.collisionList.append(temp)
        return temp
    
    @staticmethod
    def update():
        for currentBox in CollisionManager.collisionList:
            for other in CollisionManager.collisionList:
                #print currentBox.owner.type, other.owner.type
                if currentBox != other:
                    if(currentBox.checkBoxHit(other) == True):
                        currentBox.owner.onHit(other.owner, currentBox.getHitDirection(other))
                        other.owner.onHit(currentBox.owner, other.getHitDirection(currentBox))
                    CollisionManager.cleanUpDeadBoxes()
        
        
    @staticmethod
    def cleanUpDeadBoxes():
        i = len(CollisionManager.collisionList)-1
        while i >= 0:
            if(CollisionManager.collisionList[i].owner.isAlive == False):
                CollisionManager.collisionList.remove(CollisionManager.collisionList[i])
            i -= 1
    
    @staticmethod
    def test():
        print CollisionManager.collisionList;
    
    def __init__(self):
        '''
        Constructor
        '''
        