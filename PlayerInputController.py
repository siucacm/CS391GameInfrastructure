'''
Created on Feb 25, 2015

@author: SIU853541579
'''
from Player import *

class PlayerInputController():
    '''
    This class is an inbetween for handling and calling input events in a player
    This class allows us to easily change key bindings
    '''

    #constructor sets up initial bindings for keys
    def __init__(self, up, down, left, right, act1, player):
        self.upKey = up
        self.downKey = down
        self.leftKey = left
        self.rightKey = right
        self.actionKey1 = act1
        
        self.owningPlayer = player
    
    def update(self, keyboard):
        if(keyboard[self.upKey] == True):
            self.owningPlayer.inputUpKeyAction()
        #else:
            #self.owningPlayer.inputUpKeyRelease()
        if(keyboard[self.downKey] == True):
            self.owningPlayer.inputDownKeyAction()
        
        if(keyboard[self.rightKey] == True):
            self.owningPlayer.inputRightKeyAction()
        
        if(keyboard[self.leftKey] == True):
            self.owningPlayer.inputLeftKeyAction()
        
        if(keyboard[self.actionKey1] == True):
            self.owningPlayer.inputAction1()
        else:
            self.owningPlayer.releaseAction1()
            
            
            
            
        