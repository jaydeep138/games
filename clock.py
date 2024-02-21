import pygame
from datetime import datetime
import math
from datetime import date
pygame.init()

screen_width=400
screen_height=400
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("UNIVERSAL CLOCK")
pygame.display.update()
font=pygame.font.SysFont(None,30)



white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
high_score=0

clock=pygame.time.Clock()
fps=60



def coordinates_convert(radius,theta):
    x=math.sin((math.pi/180)*theta)*radius
    y=math.cos((math.pi/180)*theta)*radius
    return x+200,-y+200

def text_Screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def game():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        gameWindow.fill(white)
        pygame.draw.circle(gameWindow,(204,255,204),(200,200),200)
        pygame.draw.circle(gameWindow,black,(200,200),200,4)
        
        clock.tick(fps)

        cur_time=datetime.now()
        sec=cur_time.second
        minute=cur_time.minute
        hour=cur_time.hour



        
        #second hand
        pygame.draw.line(gameWindow,red,[200,200],coordinates_convert(170,sec*(360/60)),4)
        
        #minute hand
        pygame.draw.line(gameWindow,(0,255,0),[200,200],coordinates_convert(150,minute*(360/60)+sec/60),4)

        #hour hand
        pygame.draw.line(gameWindow,(0,0,255),[200,200],coordinates_convert(100,hour*(360/12)+(minute/60)+(sec/3600)),4)
    
        for i in range(1,13):
            text_Screen(str(i),black,coordinates_convert(180,i*30)[0]-5,coordinates_convert(180,i*30)[1]-10)
        minute_string = "0" + str(minute) if minute< 10 else str(minute)
        hours_string = "0" + str(hour) if hour < 10 else str(hour)
        text_Screen(hours_string + " : " + minute_string + " " +str(datetime.today().strftime("%p")),black,160,250)
        text_Screen(str(date.today()),black,160,280)

        pygame.display.update()
    pygame.quit()
    quit()

game()
