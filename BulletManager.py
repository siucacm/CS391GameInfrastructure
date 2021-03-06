'''
Created on Mar 6, 2015

@author: SIU853541579
'''
from baseBullet import *
from MirvBullet import *
class BulletManager():
    '''
    This is going to be a manager and factory class for bullets
    '''

    bulletList = []
    
    @staticmethod
    def buildBaseBullet(spawnX, spawnY, aimX, aimY, speed):
        #print "BulletManager.buildBaseBullet"
        temp = BaseBullet(spawnX, spawnY, aimX, aimY, speed)
        BulletManager.bulletList.append(temp)
        return temp
    
    @staticmethod
    def buildMirvBullet(spawnX, spawnY, aimX, aimY, speed):
        #print "BulletManager.buildBaseBullet"
        temp = MirvBullet(spawnX, spawnY, aimX, aimY, speed)
        BulletManager.bulletList.append(temp)
        return temp
    
    @staticmethod
    def update(screen, lowBound, upBound):
        for bullet in BulletManager.bulletList:
            if(bullet.isAlive == False):
                BulletManager.bulletList.remove(bullet)
            else:
                bullet.update(screen, lowBound, upBound)
    
    def __init__(self, params):
        '''
        Constructor
        '''
        