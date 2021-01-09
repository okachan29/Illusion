import sys
import pygame
import math
from pygame.locals import QUIT, Rect, MOUSEBUTTONDOWN, MOUSEBUTTONUP
pygame.init()
sysfont=pygame.font.SysFont(None,30)
SURFACE=pygame.display.set_mode((800,600))
FPSCLOCK = pygame.time.Clock()

class Circle:
    def __init__(self,color,position,radius,theta,phase):
        self.color=color
        self.pos=position
        self.currentPos=position
        self.radius=radius
        self.currentRadius=radius
        self.theta=theta
        self.phase=phase
    def movement(self):
        self.currentRadius=self.radius+math.floor(self.radius*math.sin(framecount/15+self.phase))+15
        self.currentPos=(math.floor(self.pos[0]+self.currentRadius*1.5*math.sin(math.radians(self.theta))),math.floor(self.pos[1]+self.currentRadius*1.5*math.cos(math.radians(self.theta))))
    def draw(self):
        pygame.draw.circle(SURFACE,self.color,self.currentPos,self.currentRadius,0)

def main():
    global framecount
    framecount=0
    mousepressed=False
    white=(255,255,255)
    black=(0,0,0)
    c1=Circle(white,(250,300),30,None,0)
    c2=Circle(white,(550,300),30,None,0)
    c1Arround=[]
    c2Arround=[]
    for theta in range(6):
        theta=theta*60
        c1Arround.append(Circle(white,(math.floor(c1.pos[0]+25*math.sin(math.radians(theta))),math.floor(c1.pos[1]+25*math.cos(math.radians(theta)))),20,theta,0))
        c2Arround.append(Circle(white,(math.floor(c2.pos[0]+25*math.sin(math.radians(theta))),math.floor(c2.pos[1]+25*math.cos(math.radians(theta)))),20,theta,math.pi))
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:  
                pygame.quit()
                sys.exit()
            if  event.type==MOUSEBUTTONDOWN:
                mousepressed=True
            if event.type==MOUSEBUTTONUP:
                mousepressed=False
        if not mousepressed:
            framecount+=1
            SURFACE.fill((0,0,0))
            c1.draw()
            c2.draw()
            for j in range(6):
                c1Arround[j].movement()
                c2Arround[j].movement()
                c1Arround[j].draw()
                c2Arround[j].draw()
            SURFACE.blit(sysfont.render("Press mouse to stop the movement.",True,white,black),(230,580))
            pygame.display.update()
            FPSCLOCK.tick(10)
if __name__=='__main__':
    main()
        

