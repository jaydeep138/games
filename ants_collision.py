import pygame
from datetime import datetime
import math
from datetime import date
import random

class Ant:
    def __init__(self,a,b,c,color,height):
        self.velocity=a
        self.position=b
        self.direction=c
        self.color=color
        self.height=height
    
    def reverse_direction(self):
        self.direction*=-1

pygame.init()

screen_width=800
screen_height=700
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Collision")
pygame.display.update()
font=pygame.font.SysFont(None,30)



white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
high_score=0

clock=pygame.time.Clock()
fps=30


def text_Screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def game():
    main_list=[]
    height=10
    for i in range(33):    
        all_ant_list=[]
        red_intial=1
        for i in range(7):
            all_ant_list.append(Ant(2,red_intial,1,"r",height))
            red_intial+=50
        black_intial=799
        for i in range(7):
            all_ant_list.append(Ant(2,black_intial,-1,"b",height))
            black_intial-=50
        main_list.append(all_ant_list)
        height+=20

    flg=1
    cnt=0
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print(flg)
                    flg^=1
        if flg:
            gameWindow.fill((132,222,2))
            for ants in main_list:
                for i in ants:
                    if i.color=="r":
                        pygame.draw.circle(gameWindow,(int(255*(i.height/800)),int(255*(i.height/800)),int(255*(i.height/800))),(i.position,i.height),5)
                    else:
                        pygame.draw.circle(gameWindow,(int(255*(i.height/800)),int(255*(i.height/800)),int(255*(i.height/800))),(i.position,i.height),5)
                    if i.position<=0 or i.position>=800:
                        i.reverse_direction()
                    i.position+=(i.velocity*i.direction)
                for i in range(len(ants)):
                    for j in range(i+1,len(ants)):
                        if i!=j:
                            if ants[i].direction != ants[j].direction:
                                if abs(ants[i].position-ants[j].position)<=10:
                                    ants[i].direction*=-1
                                    ants[j].direction*=-1
                                    cnt+=1
                                if abs(ants[i].position-ants[j].position)<=11:
                                    pygame.draw.circle(gameWindow,black,((ants[i].position+ants[j].position)/2,ants[i].height),10,2)
        # text_Screen(str(cnt),black,350,20)
            
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

game()
