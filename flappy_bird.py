import pygame
from datetime import datetime
import math
from datetime import date
import random

from pygame.constants import K_SPACE

# random.seed(datetime.now)

class Tower:
    def __init__(self,pos,height,reverse_height):
        self.position=pos
        self.height=height
        self.reverse_height=reverse_height

class Bird:
    def __init__(self,pos,height):
        self.position=pos
        self.height=height


pygame.init()

screen_width=1000
screen_height=700
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird")
pygame.display.update()
font=pygame.font.SysFont(None,30)



white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
high_score=0

clock=pygame.time.Clock()
fps=60


def text_Screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def game():
    startPos=800
    towers=[]
    towers.append(Tower(720,random.randint(40,300),random.randint(40,300)))
    lastTower=800
    B=Bird(485,345)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            if event.type==pygame.KEYDOWN:
                if event.key==K_SPACE:
                    B.height-=80
        gameWindow.fill(white)
        pygame.draw.circle(gameWindow,red,(B.position,B.height),20)
        B.height+=2
        cur_towers=[]
        for i in towers:
            if i.position+80>=0:
                cur_towers.append(i)
        for i in cur_towers:
            pygame.draw.rect(gameWindow,green,[i.position,700-i.height,80,i.height])
            pygame.draw.rect(gameWindow,green,[i.position,0,80,i.reverse_height])
            pygame.draw.rect(gameWindow,(0,100,0),[i.position-20,700-i.height,120,40])
            pygame.draw.rect(gameWindow,(0,100,0),[i.position-20,i.reverse_height-20,120,40])
            i.position-=2
        towers=cur_towers
        lastTower-=2
        if lastTower<=880:
            x=random.randint(80,130)
            towers.append(Tower(lastTower+x,random.randint(40,300),random.randint(40,300)))
            lastTower+=80+x

        
        
            
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

game()
