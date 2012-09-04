#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Jump
# Authored by Joshua Seaver and Bimal Sadhwani with a big big nod to Natalie Rusk who did the original code in Logo.
# Version .22 added mouse cursor, alpha overlay on whole screen...partially done
# Josh added sound integration---annoying???
# This is the version with a wooden board and a restart button in the lower left and text about marbles left and moves left
# Note too that olpcgames and eventwrap are not enabled...7
# Finally, it would be a good idea to clean out all of the commented out functions that are not being used.'''
# added code for alpha freezing screen: to add - the moves left code and then check if no moves left bring up the screen.

import os
import sys
import gtk
import pygame
import random
from pygame.locals import *
import levelBase


BROWN_COLOR = (88, 47, 27)
doneTest = 0
global myMatrix

myMatrix = [[2,2,1,1,1,2,2],
            [2,2,1,1,1,2,2],
            [1,1,1,1,1,1,1],
            [1,1,1,0,1,1,1],
            [1,1,1,1,1,1,1],
            [2,2,1,1,1,2,2],
            [2,2,1,1,1,2,2]]
global myMatrix_colors
myMatrix_colors=[[0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0]]
                 #[0,0,0,0,0,0,0],
                 #[0,0,0,0,0,0,0]]     

myMatrixGridSize = len(myMatrix[0])
marblesLeft = 0
movesLeft = 0
_font = 'VeraSe.ttf'
color=(0,0,0)
#color=(255,255,255)
play_var=0
button1=None
helpoff=None
count=0
marbleColor=0
special_x=0 
special_y=0
next_marble=0

def load_image(name, colorkey=None):
    
    fullname = os.path.join('data', name)
    
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    image.set_colorkey((255,255,255))
    return image, image.get_rect()

def load_sound(name):
    
    """loads a sound file (.ogg) in memory"""
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound

class board(levelBase.Level):
    
    def __init__(self):
        self.RESERVED = 0
        self.EMPTY = 1
        self.MARBLE = 2
    
    def getLayout(self):
        return [[0,0,2,2,2,0,0],\
                [0,2,2,2,2,2,0],\
                [2,2,2,2,2,2,2],\
                [2,2,2,2,2,2,2],\
                [2,2,2,2,2,2,2],\
                [0,2,2,2,2,2,0],\
                [0,0,2,2,2,0,0]]
    

#need to somehow load in random marble images from data folder

class Marble(pygame.sprite.Sprite):
        
    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self)
        marbleColor = random.random()
        marbleColor = marbleColor * 10
        marbleColor = int(marbleColor)
        if marbleColor > 23:
            marbleColor = 23 
        pngLoad = str(marbleColor)
        pngLoad = pngLoad + '.png'
        self.image, self.rect = load_image(pngLoad,-1)
                
        if rect != None:
            self.rect = rect

class simple_button(pygame.sprite.Sprite):

    def __init__(self,x,y,pic,sound):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(pic)
        self.status = self.down = self.up = 0
        self.ypos = self.rect.top = y
        self.xpos = self.rect.left = x
        self.pressSound = load_sound('newboard.ogg')
        
    def press(self):        
        self.status = 1
        self.pressSound.play()
        
    def unpress(self):        
        self.status = 0
                
    def update(self):
        if self.down:
            self.press()
            self.down = 0            
            self.screen.blit(self.background,(0,0))
        elif self.up:
            self.unpress()
            self.up = 0
                        
    def is_focused(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

class SolitaireMain:
    def __init__(self, width=1200,height=825):
        self.width = width
        self.height = height
        

    def load_things(self):
        self.screen = pygame.display.get_surface()
        if (self.screen == None):
            self.screen = pygame.display.set_mode((self.width, self.height))

        self.font = pygame.font.Font(None, 50)
        a=pygame.image.load("data/0.png").convert()                
        a.set_colorkey(color)                        
        b=pygame.image.load("data/1.png").convert()                
        b.set_colorkey(color)
        c=pygame.image.load("data/2.png").convert()                
        c.set_colorkey(color)
        d=pygame.image.load("data/3.png").convert()
        d.set_colorkey(color)
        e=pygame.image.load("data/4.png").convert()
        e.set_colorkey(color)
        f=pygame.image.load("data/5.png").convert()
        f.set_colorkey(color)
        g=pygame.image.load("data/6.png").convert()
        g.set_colorkey(color)
        h=pygame.image.load("data/7.png").convert()                
        h.set_colorkey(color)
        i=pygame.image.load("data/8.png").convert()
        i.set_colorkey(color)
        j=pygame.image.load("data/9.png").convert()
        j.set_colorkey(color)
        k=pygame.image.load("data/10.png").convert()
        k.set_colorkey(color)
        l=pygame.image.load("data/11.png").convert()
        l.set_colorkey(color)
        m=pygame.image.load("data/12.png").convert()
        m.set_colorkey(color)
        n=pygame.image.load("data/13.png").convert()
        n.set_colorkey(color)
        o=pygame.image.load("data/14.png").convert()
        o.set_colorkey(color)
        p=pygame.image.load("data/15.png").convert()
        p.set_colorkey(color)
        q=pygame.image.load("data/16.png").convert()
        q.set_colorkey(color)
        r=pygame.image.load("data/17.png").convert()
        r.set_colorkey(color)
        s=pygame.image.load("data/18.png").convert()
        s.set_colorkey(color)
        t=pygame.image.load("data/19.png").convert()
        t.set_colorkey(color)
        u=pygame.image.load("data/20.png").convert()
        u.set_colorkey(color)
        v=pygame.image.load("data/21.png").convert()
        v.set_colorkey(color)
        w=pygame.image.load("data/22.png").convert()
        w.set_colorkey(color)
        x=pygame.image.load("data/23.png").convert()
        x.set_colorkey(color)
        y=pygame.image.load("data/24.png").convert()
        y.set_colorkey(color)        
        bl=pygame.image.load("data/blank.png")
        z=pygame.image.load("data/25.png")
        
        
        self.marble_images=[]
        self.marble_images.append(a)
        self.marble_images.append(b)
        self.marble_images.append(c)
        self.marble_images.append(d)
        self.marble_images.append(e)
        self.marble_images.append(f)
        self.marble_images.append(g)
        self.marble_images.append(h)
        self.marble_images.append(i)
        self.marble_images.append(j)
        self.marble_images.append(k)
        self.marble_images.append(l)
        self.marble_images.append(m)
        self.marble_images.append(n)
        self.marble_images.append(o)
        self.marble_images.append(p)
        self.marble_images.append(q)
        self.marble_images.append(r)
        self.marble_images.append(s)
        self.marble_images.append(t)
        self.marble_images.append(u)
        self.marble_images.append(v)
        self.marble_images.append(w)
        self.marble_images.append(x)
        self.marble_images.append(y)      
        self.marble_images.append(bl)#number25
        self.marble_images.append(z)        
        
        #special marbles
        a=pygame.image.load("data/S08.png").convert()
        b=pygame.image.load("data/S21.png").convert()
        c=pygame.image.load("data/S03.png").convert()
        d=pygame.image.load("data/S04.png").convert()
        e=pygame.image.load("data/S05.png").convert()
        f=pygame.image.load("data/S06.png").convert()
        g=pygame.image.load("data/S07.png").convert()
        h=pygame.image.load("data/S08.png").convert()
        i=pygame.image.load("data/S09.png").convert()
        j=pygame.image.load("data/S10.png").convert()
        k=pygame.image.load("data/S11.png").convert()
        l=pygame.image.load("data/S12.png").convert()
        m=pygame.image.load("data/S13.png").convert()
        n=pygame.image.load("data/S14.png").convert()
        o=pygame.image.load("data/S15.png").convert()
        p=pygame.image.load("data/S16.png").convert()
        q=pygame.image.load("data/S17.png").convert()
        r=pygame.image.load("data/S18.png").convert()
        s=pygame.image.load("data/S19.png").convert()
        t=pygame.image.load("data/S20.png").convert()
        u=pygame.image.load("data/S21.png").convert()
        v=pygame.image.load("data/S22.png").convert()
        w=pygame.image.load("data/S23.png").convert()
        x=pygame.image.load("data/S24.png").convert()
        y=pygame.image.load("data/S25.png").convert()
        z=pygame.image.load("data/S26.png").convert()
        aa=pygame.image.load("data/S27.png").convert()
        ab=pygame.image.load("data/S28.png").convert()
        ac=pygame.image.load("data/S29.png").convert()
        ad=pygame.image.load("data/S30.png").convert()
        ae=pygame.image.load("data/S31.png").convert()
        af=pygame.image.load("data/S32.png").convert()
        ag=pygame.image.load("data/S33.png").convert()
        ah=pygame.image.load("data/S34.png").convert()
        ai=pygame.image.load("data/S35.png").convert()
        aj=pygame.image.load("data/S36.png").convert()                
        
        self.special_marbles=[]
        self.special_marbles.append(a)
        self.special_marbles.append(b)
        self.special_marbles.append(c)
        self.special_marbles.append(d)
        self.special_marbles.append(e)
        self.special_marbles.append(f)
        self.special_marbles.append(g)
        self.special_marbles.append(h)
        self.special_marbles.append(i)
        self.special_marbles.append(j)
        self.special_marbles.append(k)
        self.special_marbles.append(l)
        self.special_marbles.append(m)
        self.special_marbles.append(n)
        self.special_marbles.append(o)
        self.special_marbles.append(p)
        self.special_marbles.append(q)
        self.special_marbles.append(r)
        self.special_marbles.append(s)
        self.special_marbles.append(t)
        self.special_marbles.append(u)
        self.special_marbles.append(v)
        self.special_marbles.append(w)
        self.special_marbles.append(x)
        self.special_marbles.append(y)
        self.special_marbles.append(z)        
        self.special_marbles.append(aa)
        self.special_marbles.append(ab)
        self.special_marbles.append(ac)
        self.special_marbles.append(ad)
        self.special_marbles.append(ae)        
        self.special_marbles.append(af) #no 31
        self.special_marbles.append(bl) #no 32
        self.special_marbles.append(ag)        
        self.special_marbles.append(ah)
        self.special_marbles.append(ai)
        self.special_marbles.append(aj)
        
        #call reset funnction
        self.reset()
        self.helpscreen = pygame.image.load("data/Instructions.png")
        self.flags=[]
        self.flags.append(pygame.image.load("data/Flag01.png").convert())
        self.flags.append(pygame.image.load("data/Flag02.png").convert())        
        self.flags.append(pygame.image.load("data/Flag03.png").convert())
        self.flags.append(pygame.image.load("data/Flag04.png").convert())
        self.flags.append(pygame.image.load("data/Flag05.png").convert())
        self.flags.append(pygame.image.load("data/Flag06.png").convert())
        self.flags.append(pygame.image.load("data/Flag07.png").convert())
        
        
        self.level_sounds=[]
        self.level_sounds.append(load_sound('0.ogg'))
        self.level_sounds.append(load_sound('1.ogg'))
        self.level_sounds.append(load_sound('2.ogg'))
        self.level_sounds.append(load_sound('3.ogg'))
        self.level_sounds.append(load_sound('4.ogg'))
        self.level_sounds.append(load_sound('5.ogg'))
        self.level_sounds.append(load_sound('6.ogg'))
        self.level_sounds.append(load_sound('7.ogg'))
        
    def reset(self):    
        global marbleColor
        #intialisation of Number for the first time ..keep a balnk png.
        self.updated_text=32
        self.updated_moves=4
        self.Number=25# 26  #25
        self.pressed=False
        self.selected= False
        self.initial_x=0
        self.initial_y=0
        
        self.final_x=0
        self.final_y=0
        self.OutofRange=True
        
        self.clickedOnce=False
        self.attached=False
        self.picked=False
        marbleColor=0
    def reset_board(self):
        
        global myMatrix
        myMatrix=[[2,2,1,1,1,2,2],
                  [2,2,1,1,1,2,2],
                  [1,1,1,1,1,1,1],
                  [1,1,1,0,1,1,1],
                  [1,1,1,1,1,1,1],
                  [2,2,1,1,1,2,2],
                  [2,2,1,1,1,2,2]]        
        
        global myMatrix_colors
        myMatrix_colors=[[0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0]]
        
        
    def checkValidMovement(self):     
        global marbleColor
        temp=pygame.mouse.get_pos()
        #print temp
        x=temp[0]    
        y=temp[1]
        x=x-300
        
        x/=90
        y-=120
        
        y/=90
        
        if(x>=0 and x<=6 and y>=0 and y<=6):
        
            if(myMatrix[y][x]==0):
                self.final_x=y
                self.final_y=x
            else:
                self.OutofRange=True
                self.final_x=0
                self.final_y=0
           
        
        if(self.initial_x ==0 and self.initial_y ==0):
            self.OutofRange=False
            
        w=self.initial_x
        x=self.initial_y
        self.wInput=self.initial_x
        self.xInput=self.initial_y
        
        y=self.final_x
        z=self.final_y
        
        self.yInput=self.final_x
        self.zInput=self.final_y
        neighborState = 99
        neighborStateRow = 99
        neighborStateColumn = 99
        validJump = 99
        self.matrixPosStart=myMatrix[w][x]
        self.matrixPosEnd=myMatrix[y][z]
        
        if w == y:
            if x > z:
                neighborStateRow = w
                neighborStateColumn = x - 1
                neighborState = myMatrix[neighborStateRow][neighborStateColumn]
                if (self.xInput - self.zInput) > 2:
                    validJump = 0
                else: 
                    validJump = 1
            elif x<z:
                neighborStateRow = w
                neighborStateColumn = x + 1
                neighborState = myMatrix[neighborStateRow][neighborStateColumn]
                if (self.zInput - self.xInput) > 2:
                    validJump = 0
                else: 
                    validJump = 1
        elif x==z:

            if w > y:
                neighborStateRow = w - 1
                neighborStateColumn = x
                neighborState = myMatrix[neighborStateRow][neighborStateColumn]
                if (self.wInput - self.yInput) > 2:
                    validJump = 0
                else: 
                    validJump = 1
            elif w<y:
                neighborStateRow = w + 1
                neighborStateColumn = x
                neighborState = myMatrix[neighborStateRow][neighborStateColumn]
                if (self.yInput - self.wInput) > 2:
                    validJump = 0
                else:                    
                    validJump = 1
                    
        if(validJump==99 and self.initial_x>0 and self.initial_y>0):
            self.OutofRange=True
            
        if self.matrixPosStart != 2 and self.matrixPosEnd == 0 and neighborState == 1 and validJump == 1:
            myMatrix[w][x] = 0
            myMatrix[neighborStateRow][neighborStateColumn] = 0
            myMatrix[y][z] = 1
            myMatrix_colors[y][z]=myMatrix_colors[w][x]
            #test playing sound here
            moveSound = load_sound('drop.ogg')
            moveSound.play()
            
        else:             
             if(self.OutofRange==True):
                 myMatrix[w][x]=1

        self.screen.blit(self.background,(0,0))
        row=106
        for k in range(7):  
            start=292         
            for i in range(7):
                self.pngNumber=myMatrix_colors[k][i]
                      
                if(myMatrix[k][i]==1): 
                    if self.pngNumber==marbleColor:                        
                        self.screen.blit(self.marble_images[self.pngNumber],(start,row))
                    else:
        
                        self.pngNumber-=100
                        self.screen.blit(self.special_marbles[self.pngNumber],(start,row))                       
        
                start+=90                        
            row+=90        
        
        #reseting the values back
        self.OutofRange=True 
        self.initial_x=0
        self.initial_y=0      
        self.update_moves()
        self.display()
        
    def changePosition(self):
        global marbleColor,special_x,special_y
        self.x=pygame.mouse.get_pos()
        x=self.x[0]    
        y=self.x[1]
        x=(x/90)-(300/90) 
        y=(y/90)-(120/90)
        #self.Number=0
        
        #print "marble  color is :",marbleColor
        if(x>=0 and x<7 and y>=0 and y<7):
            if self.pressed==False and myMatrix[y][x]==1:
                myMatrix[y][x]=0
                self.Number=myMatrix_colors[y][x]
         
                if self.Number>=100:
                    special_x=y
                    special_y=x
         
                self.initial_x=y
                self.initial_y=x
        
        self.selected=True
        self.pressed=True 
        if self.Number==marbleColor:
            self.marble_rect=self.marble_images[self.Number].get_rect()
        elif self.Number==25:
            self.marble_rect=self.marble_images[self.Number].get_rect()
        else:
            self.marble_rect=self.special_marbles[self.Number-100].get_rect()
            
        self.marble_rect.center=pygame.mouse.get_pos()
        self.screen.blit(self.background,(0,0))
        
        
        row=106        
        for k in range(7):
            start=292           
            for i in range(7):
                self.pngNumber=myMatrix_colors[k][i]
                                    
                if(myMatrix[k][i]==1):
        
                    if self.pngNumber==marbleColor:                        
                        self.screen.blit(self.marble_images[self.pngNumber],(start,row))
                    
                    else:
                        self.pngNumber-=100
        
                        self.screen.blit(self.special_marbles[self.pngNumber],(start,row))
                start+=90                        
            row+=90
        

        if self.Number==marbleColor:
            self.screen.blit(self.marble_images[self.Number],self.marble_rect)
        elif self.Number==25:
            self.screen.blit(self.marble_images[self.Number],self.marble_rect)
        else:

            self.screen.blit(self.special_marbles[self.Number-100],self.marble_rect)
        
    def moving(self):
        row=90
        self.screen.blit(self.background,self.marble_rect,self.marble_rect)       
       
        self.marble_rect.center=pygame.mouse.get_pos()
        self.screen.blit(self.marble_images[self.Number],self.marble_rect)
    def noMoreMoves(self):
        global button1
        rollover_once=0
        run=1
        self.alphasurface = pygame.Surface((1280,825))
        self.alphasurface.convert()
        self.alphasurfacerect = pygame.Rect(0,0,1280,825)
        self.alphasurface.fill((100,100,100))
        self.alphasurface.set_alpha(200)
        self.screen.blit(self.background, (0,0))
        row=106
        for k in range(7):  
            start=292         
            for i in range(7):
                self.pngNumber=myMatrix_colors[k][i]
                if(myMatrix[k][i]==1):   
                    if self.pngNumber==marbleColor:                        
                        self.screen.blit(self.marble_images[self.pngNumber],(start,row))
                    else:
                        self.pngNumber-=100
                        self.screen.blit(self.special_marbles[self.pngNumber],(start,row))                                
                start+=90                        
            row+=90     
        
        self.display()
        self.screen.blit(self.alphasurface,self.alphasurfacerect)
        
        while run:
            for event in pygame.event.get():
                
                if event.type == QUIT or (event.type == KEYDOWN and 
                                          event.key in [K_ESCAPE]):sys.exit()                                           
                
                
                elif event.type == MOUSEBUTTONDOWN:
                    if button1.is_focused():
                        button1.press()                    
                elif event.type == MOUSEBUTTONUP:
                    if button1.status == 1:
                        button1.unpress()
                        self.play_var = 1
                        run = 0                    
                
                if self.play_var==1:
                    self.play_var=0
                    self.reset()
                    self.reset_board()
                    self.SuperLooper()
                    
            if (button1.rect.collidepoint(pygame.mouse.get_pos()) and rollover_once==0):
                rollover_once=1     
                self.allsprites.remove(button1)
                button1 = simple_button(31,614,'NewBoardOn.png',None)
                self.allsprites=pygame.sprite.RenderPlain(button1)
                self.allsprites.draw(self.screen)
            elif not (button1.rect.collidepoint(pygame.mouse.get_pos())):
                rollover_once=0
                button1 = simple_button(31,614,'NewBoard.png',None)
                self.allsprites=pygame.sprite.RenderPlain(button1)
                self.allsprites.draw(self.screen)
            pygame.display.update()
 
    def SuperLooper(self):
        
        global button1,helpoff,marbleColor,next_marble,count
        rollover_once=0
        run=1

        pygame.init()

        self.load_things()

        self.background = pygame.image.load("data/Background2.png")
        self.play_var=0
        self.help_var=0
        self.play_sound=False
        self.pickedSound=0
        pygame.mouse.set_cursor((32, 32), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 31, 255, 255, 224, 31, 255, 255, 248, 31, 255, 255, 248, 31, 255, 255, 248, 31, 255, 255, 248, 31, 255, 255, 248, 31, 255, 255, 240, 31, 252, 0, 0, 31, 254, 0, 0, 31, 255, 0, 0, 31, 255, 128, 0, 31, 255, 192, 0, 31, 191, 224, 0, 31, 159, 240, 0, 31, 143, 248, 0, 31, 135, 252, 0, 31, 131, 254, 0, 31, 129, 255, 0, 31, 128, 255, 128, 31, 128, 127, 192, 31, 128, 63, 224, 31, 128, 31, 240, 31, 128, 15, 248, 31, 128, 7, 248, 31, 128, 3, 248, 31, 128, 1, 248, 15, 0, 0, 248, 0, 0, 0, 96, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 127, 255, 255, 248, 127, 255, 255, 252, 127, 255, 255, 254, 127, 255, 255, 254, 127, 255, 255, 254, 127, 255, 255, 254, 127, 255, 255, 254, 127, 255, 255, 252, 127, 255, 255, 252, 127, 255, 255, 240, 127, 255, 192, 0, 127, 255, 224, 0, 127, 255, 240, 0, 127, 255, 248, 0, 127, 255, 252, 0, 127, 255, 254, 0, 127, 255, 255, 0, 127, 255, 255, 128, 127, 239, 255, 192, 127, 231, 255, 224, 127, 227, 255, 240, 127, 225, 255, 248, 127, 224, 255, 252, 127, 224, 127, 254, 127, 224, 63, 254, 127, 224, 31, 254, 127, 192, 15, 254, 127, 192, 7, 254, 63, 128, 3, 252, 15, 0, 1, 248, 0, 0, 0, 0))
        group=[]
        empty=()
        self.displaying_arrow=False
        self.screen.blit(self.background, (0,0))
        
        button1 = simple_button(31,614,'NewBoard.png',None)
        self.allsprites=pygame.sprite.RenderPlain(button1)
        self.allsprites.empty()
        self.allsprites.draw(self.screen)
        helpoff=simple_button(970,614,'HelpOff.png',None)
        self.allspritess=pygame.sprite.RenderPlain(helpoff)
        self.LoadSprites()
        self.marble_rect=self.marble_images[self.Number].get_rect()
        self.marble_rect.center=pygame.mouse.get_pos()
        
        #onscreen text
        marble_text = self.font.render(str(self.updated_text), 1, BROWN_COLOR)
        marble_textpos = marble_text.get_rect(topleft=(1000,50))
        #self.screen.blit(marble_text, marble_textpos)
        
        self.screen.blit(self.special_marbles[next_marble-1],(1067,45))
        
        self.rollover_images=[]
        self.rollover_images.append(pygame.image.load("data/Arrow1.png"))
        self.rollover_images.append(pygame.image.load("data/Arrow2.png"))
        self.rollover_images.append(pygame.image.load("data/Arrow3.png"))
        self.rollover_images.append(pygame.image.load("data/Arrow4.png"))
        pygame.display.update()
        
        while run:
            #condition for checking for mouse arrows
            if(self.updated_text==32):
                if (self.displaying_arrow==False and pygame.mouse.get_pos()[0]>=550 and pygame.mouse.get_pos()[0]<=625
                    and pygame.mouse.get_pos()[1]>=550 and pygame.mouse.get_pos()[1]<=625):                                
                    self.screen.blit(self.rollover_images[3],(520,380))            
                    self.displaying_arrow=True
                    
                if (self.displaying_arrow==False and pygame.mouse.get_pos()[0]>=550 and pygame.mouse.get_pos()[0]<=625
                    and pygame.mouse.get_pos()[1]>=175 and pygame.mouse.get_pos()[1]<=275):
                    self.screen.blit(self.rollover_images[2],(550,200))
                    self.displaying_arrow=True
                    
                if (self.displaying_arrow==False and pygame.mouse.get_pos()[0]>=400 and pygame.mouse.get_pos()[0]<=450
                    and pygame.mouse.get_pos()[1]>=375 and pygame.mouse.get_pos()[1]<=425):
                    self.screen.blit(self.rollover_images[1],(400,350))
                    self.displaying_arrow=True
                    
                if (self.displaying_arrow==False and pygame.mouse.get_pos()[0]>=700 and pygame.mouse.get_pos()[0]<=800
                    and pygame.mouse.get_pos()[1]>=375 and pygame.mouse.get_pos()[1]<=450):
                    self.screen.blit(self.rollover_images[0],(550,350))
                    self.displaying_arrow=True
                    
                
            if (button1.rect.collidepoint(pygame.mouse.get_pos()) and rollover_once==0):
                rollover_once=1                                
                self.allsprites.remove(button1)
                button1 = simple_button(31,614,'NewBoardOn.png',None)
                self.allsprites=pygame.sprite.RenderPlain(button1)
                self.allsprites.draw(self.screen)
           
            elif not (button1.rect.collidepoint(pygame.mouse.get_pos())):             
                rollover_once=0
                self.allsprites.empty()
                button1 = simple_button(31,614,'NewBoard.png',None)
                self.allsprites=pygame.sprite.RenderPlain(button1)
                self.allsprites.draw(self.screen)
  
            if (helpoff.rect.collidepoint(pygame.mouse.get_pos()) and rollover_onces==0):
                rollover_onces=1
                self.allspritess.remove(button1)
                helpoff = simple_button(970,614,'HelpOn.png',None)
                self.allspritess=pygame.sprite.RenderPlain(helpoff)
                self.allspritess.draw(self.screen)
           
            elif not (helpoff.rect.collidepoint(pygame.mouse.get_pos())):             
                
                rollover_onces=0                
                helpoff = simple_button(970,614,'HelpOff.png',None)
                self.allspritess=pygame.sprite.RenderPlain(helpoff)
                self.allspritess.draw(self.screen)
            temp_pos=pygame.mouse.get_pressed()
            if temp_pos[0]==0 and self.selected==True and self.pressed==True:
                self.pressed=False
                self.selected=False
                self.checkValidMovement()
                self.Number=25#26    25
                self.picked=False
                self.displaying_arrow=False
                '''Change the cursor to an arrow'''
                pygame.mouse.set_cursor((32, 32), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 31, 255, 255, 224, 31, 255, 255, 248, 31, 255, 255, 248, 31, 255, 255, 248, 31, 255, 255, 248, 31, 255, 255, 248, 31, 255, 255, 240, 31, 252, 0, 0, 31, 254, 0, 0, 31, 255, 0, 0, 31, 255, 128, 0, 31, 255, 192, 0, 31, 191, 224, 0, 31, 159, 240, 0, 31, 143, 248, 0, 31, 135, 252, 0, 31, 131, 254, 0, 31, 129, 255, 0, 31, 128, 255, 128, 31, 128, 127, 192, 31, 128, 63, 224, 31, 128, 31, 240, 31, 128, 15, 248, 31, 128, 7, 248, 31, 128, 3, 248, 31, 128, 1, 248, 15, 0, 0, 248, 0, 0, 0, 96, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 127, 255, 255, 248, 127, 255, 255, 252, 127, 255, 255, 254, 127, 255, 255, 254, 127, 255, 255, 254, 127, 255, 255, 254, 127, 255, 255, 254, 127, 255, 255, 252, 127, 255, 255, 252, 127, 255, 255, 240, 127, 255, 192, 0, 127, 255, 224, 0, 127, 255, 240, 0, 127, 255, 248, 0, 127, 255, 252, 0, 127, 255, 254, 0, 127, 255, 255, 0, 127, 255, 255, 128, 127, 239, 255, 192, 127, 231, 255, 224, 127, 227, 255, 240, 127, 225, 255, 248, 127, 224, 255, 252, 127, 224, 127, 254, 127, 224, 63, 254, 127, 224, 31, 254, 127, 192, 15, 254, 127, 192, 7, 254, 63, 128, 3, 252, 15, 0, 1, 248, 0, 0, 0, 0))
                self.pickedSound=0
                
            if temp_pos[0]==1 : #and self.picked==False:
                '''Change the cursor to an X'''
                pygame.mouse.set_cursor((32, 32), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 0, 16, 62, 0, 0, 120, 63, 0, 0, 252, 63, 128, 1, 252, 31, 192, 3, 248, 15, 224, 7, 240, 7, 240, 15, 224, 3, 248, 31, 192, 1, 252, 63, 128, 0, 254, 127, 0, 0, 127, 254, 0, 0, 63, 252, 0, 0, 31, 248, 0, 0, 15, 240, 0, 0, 15, 240, 0, 0, 31, 248, 0, 0, 63, 252, 0, 0, 127, 254, 0, 0, 254, 127, 0, 1, 252, 63, 128, 3, 248, 31, 192, 7, 240, 15, 224, 15, 224, 7, 240, 31, 192, 3, 248, 63, 128, 1, 252, 63, 0, 0, 252, 30, 0, 0, 124, 8, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0), (28, 0, 0, 16, 62, 0, 0, 124, 127, 0, 0, 254, 255, 128, 1, 254, 255, 192, 3, 255, 255, 224, 7, 254, 127, 240, 15, 254, 63, 248, 31, 252, 31, 252, 63, 248, 15, 254, 127, 240, 7, 255, 255, 224, 3, 255, 255, 192, 1, 255, 255, 128, 0, 255, 255, 0, 0, 127, 254, 0, 0, 63, 252, 0, 0, 63, 252, 0, 0, 127, 254, 0, 0, 255, 255, 0, 1, 255, 255, 128, 3, 255, 255, 192, 7, 255, 255, 224, 15, 254, 127, 240, 31, 252, 63, 248, 63, 248, 31, 252, 127, 240, 15, 254, 127, 224, 7, 255, 255, 192, 3, 255, 127, 128, 1, 255, 127, 0, 0, 254, 62, 0, 0, 124, 8, 0, 0, 56))                                                                                  
                self.picked=True
                pickedSound = load_sound('pop1.ogg')
                if self.pickedSound == 0:
                    pickedSound.play()
                    self.pickedSound=1
                self.changePosition()
                self.display()

            while gtk.events_pending():
                gtk.main_iteration()
                
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and 
                                          event.key in [K_ESCAPE]):sys.exit()                                           
                
                
                elif event.type == MOUSEBUTTONDOWN:
                    if button1.is_focused():
                        button1.press()
                    elif helpoff.is_focused():                        
                        helpoff.press()                    
                elif event.type == MOUSEBUTTONUP:
                    if button1.status == 1:
                        button1.unpress()
                        self.play_var = 1
                        run=0
                    elif helpoff.status == 1:
                        helpoff.unpress()
                        self.help_var = 1
                        #run=0                                
                
                if self.play_var==1:
                    self.play_var=0
                    self.reset()
                    self.reset_board()
                    self.SuperLooper()
                if self.help_var==1:
                    self.help_var=0
                    self.help_screen()
                    
            pygame.display.update()
            
            if self.updated_text==28 and self.play_sound==False and count==0:
                self.level_sounds[0].play()
                count+=1
                self.play_sound=True
            elif self.updated_text==24 and self.play_sound==False and count==1:
                self.level_sounds[1].play()
                self.play_sound=False
                count+=1
            elif self.updated_text==20 and self.play_sound==False and count==2:
                self.level_sounds[2].play()
                self.play_sound=True
                count+=1
            elif self.updated_text==16 and self.play_sound==False and count==3:
                self.level_sounds[3].play()
                self.play_sound=True
                count+=1
            elif self.updated_text==12 and self.play_sound==False and count==4:
                self.level_sounds[4].play()
                self.play_sound=True
                count+=1
            elif self.updated_text==8 and self.play_sound==False and count==5:
                self.level_sounds[5].play()
                self.play_sound=True
                count+=1
            elif self.updated_text==4 and self.play_sound==False and count==6:
                self.level_sounds[6].play()
                self.play_sound=True
                count+=1
                
            if self.updated_moves==0:
                if self.updated_text==1:
                    self.level_sounds[7].play()
                    f = open("marble.txt","r")                     
                    number=f.readline()                     
                    f.close()
                    number=int(number)
                    if number>=0:
                        p=open("marble.txt","w")
                        number+=1
                        number=str(number)
                        p.write(number)
                        p.close()                       
                run=0                
                self.noMoreMoves()
                
    def help_screen(self):
        
        run=True
        self.alphasurface = pygame.Surface((1280,825))
        self.alphasurface.convert()
        self.alphasurfacerect = pygame.Rect(0,0,1280,825)
        self.alphasurface.fill((100,100,100))
        self.alphasurface.set_alpha(200)
        self.screen.blit(self.alphasurface,self.alphasurfacerect)            
        self.screen.blit(self.helpscreen,(0,0))
        pygame.display.update()
        while run:
            while gtk.events_pending():
                gtk.main_iteration()

            for event in pygame.event.get():
                
                if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                    run =0
            
        
    def update_moves(self):        
        marblesLeft = 0
        movesLeft = 0
        i = 0
        while i < myMatrixGridSize: # should eventually be length of rows
            j = 0
            while j < myMatrixGridSize: # should eventually be length of columns
                m = myMatrix[i][j]
                if m == 1: # there is a marble in the slot
                    marblesLeft = marblesLeft + 1
                    boundsCheck = i - 1
                    if boundsCheck >= 0:
                        mn = myMatrix[i -1][j]
                        if mn == 0: # no move directly above
                            pass
                        else:
                            pass
                        boundsCheck = i - 2
                        if boundsCheck >= 0:
                            mn = myMatrix[i - 2][j]
                            mn2 = myMatrix[i - 1][j]
                            if mn == 0 and mn2 == 1:
                                #print "There is a move above."
                                movesLeft = movesLeft + 1 
                            else:
                                pass
                    else: # there is a move above, but is the slot above that empty
                        pass
                    boundsCheck = i + 1
                    if boundsCheck < myMatrixGridSize: # needs to be drawn from the number of rows eventually
                        mn = myMatrix[i + 1][j]
                        if mn == 0: # no move directly below
                            pass
                        else:
                            pass
                        boundsCheck = i + 2
                        if boundsCheck < myMatrixGridSize:
                            mn = myMatrix[i + 2][j]
                            mn2 = myMatrix[i + 1][j]
                            if mn == 0 and mn2 == 1:
                                movesLeft = movesLeft + 1 
                            else:
                                pass
                    else: # there is a move below, but is the slot below that empty
                        pass
                    boundsCheck = j - 1
                    if boundsCheck >= 0: # needs to be drawn from the number of rows eventually
                        mn = myMatrix[i][j - 1]
                        if mn == 0: # no move directly to the left
                            pass
                        else:
                            pass
                        boundsCheck = j - 2
                        if boundsCheck >= 0:
                            mn = myMatrix[i][j - 2]
                            mn2 = myMatrix[i][j - 1]
                            if mn == 0 and mn2 == 1:
                                movesLeft = movesLeft + 1 
                            else:
                                pass
                    else: # there is a move below, but is the slot below that empty
                        pass
                    #check right
                    boundsCheck = j + 1
                    if boundsCheck < myMatrixGridSize: # needs to be drawn from the number of rows eventually
                        mn = myMatrix[i][j + 1]
                        if mn == 0: # no move directly to the right
                            pass
                        else:
                            pass
                        boundsCheck = j + 2
                        if boundsCheck < myMatrixGridSize:
                            mn = myMatrix[i][j + 2]
                            mn2 = myMatrix[i][j + 1]
                            if mn == 0 and mn2 == 1:
                                movesLeft = movesLeft + 1 
                            else:
                                pass
                    else: # there is a move below, but is the slot below that empty
                        pass
                else: # There is no marble in the slot
                    pass
    
                        
                j = j + 1
            i = i + 1
        
        self.updated_text=marblesLeft
        
        self.updated_moves= movesLeft
        return

    def display(self):
        global button1,helpoff,next_marble
        marble_text = self.font.render(str(self.updated_text), 1, BROWN_COLOR)
        marble_textpos = marble_text.get_rect(topleft=(1000,50))
        #self.screen.blit(marble_text, marble_textpos)
        #flag conditions
        if(self.updated_text<=28 and self.updated_text>24):# and count==0):
            self.screen.blit(self.flags[0],(1038,110))
                        
        elif(self.updated_text<=24 and self.updated_text>20):# and count==2):
            self.screen.blit(self.flags[1], (1038,110))
            self.play_sound=False
        elif(self.updated_text<=20 and self.updated_text>16):
            self.screen.blit(self.flags[2], (1038,110))
            self.play_sound=False
        elif(self.updated_text<=16 and self.updated_text>12):
            self.screen.blit(self.flags[3],(1038,110))
            self.play_sound=False
        elif(self.updated_text<=12 and self.updated_text>8):
            self.screen.blit(self.flags[4],(1038,110))
            self.play_sound=False
        elif(self.updated_text<=8 and self.updated_text>4):
            self.screen.blit(self.flags[5],(1038,110))
            self.play_sound=False
        elif(self.updated_text<=4 and self.updated_text>1):
            self.screen.blit(self.flags[6], (1038,110))
            self.play_sound=False           
        
        self.screen.blit(self.special_marbles[next_marble-1],(1067,45)) 
        self.allsprites.draw(self.screen)
        if self.updated_moves>0:
            self.allspritess.draw(self.screen)
        
    def LoadSprites(self):
        global marbleColor,next_marble
        """Create the Marbles group"""         
        n=7        
        row=106 #120        
        
        marbleColor = random.randrange(0,23)
        f = open("marble.txt","r")
        number=f.readline()
        f.close()
        number=int(number)
        if number>32:
            number=32
            
        next_marble=number+1
        j=0
        start=292
        row=106
        if number>0:                     
            while j !=(number):
                pngNumber=j
                xtemp = random.randrange(0,7)
                ytemp = random.randrange(0,7)
                print pngNumber,xtemp,ytemp
                    
                if(myMatrix[xtemp][ytemp]==1):
                    myMatrix_colors[xtemp][ytemp]=pngNumber+100
                    self.screen.blit(self.special_marbles[pngNumber],(start+(ytemp*90),row+(xtemp*90)))
                    myMatrix[xtemp][ytemp]=3
                    j+=1
        
        row=106           
        #function for generating the dots using matrix method
        for k in range(7):  
            start=292
            for i in range(7):     
                if(myMatrix[k][i]==1):
                    pngNumber=marbleColor                            
                    myMatrix_colors[k][i]=pngNumber
                    self.screen.blit(self.marble_images[pngNumber],(start,row))
                start+=90
            row+=90
            
        
        for k in range(7):        
            for i in range(7):     
                if(myMatrix[k][i]==3):
                    myMatrix[k][i]=1
        
        
        
def main():
    MainWindow = SolitaireMain()    
    MainWindow.SuperLooper()
       
if __name__=="__main__":
    main()
