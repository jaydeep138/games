import pygame
import time
import random
from pygame import mixer
screen_width=1000
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("JD GAMEZONE")
pygame.display.update()
x=pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)


clock=pygame.time.Clock()
fps=30
zeroimg=pygame.image.load('zero.jpg')
crossimg=pygame.image.load('cross.jpg')
zeroc=pygame.image.load('zeroc.png')
crossc=pygame.image.load('crossc.png')
font=pygame.font.SysFont(None,55)
gameWindow.fill(white)

box_pos_list=[[0,0],[200,0],[400,0],[0,200],[200,200],[400,200],[0,400],[200,400],[400,400]]

def draw_zero(box):
    x=box_pos_list[box-1][0]+5
    y=box_pos_list[box-1][1]+5
    gameWindow.blit(zeroimg,(x,y))


def draw_cross(box):
    x=box_pos_list[box-1][0]+5
    y=box_pos_list[box-1][1]+5
    gameWindow.blit(crossimg,(x,y))

def text_Screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
    


def get_box(x,y):
    x=x//200
    y=y//200

    if x==0 and y==0:
        return 1
    if y==0 and x==1:
        return 2
    if y==0 and x==2:
        return 3
    if y==1 and x==0:
        return 4
    if y==1 and x==1:
        return 5
    if y==1 and x==2:
        return 6    
    if y==2 and x==0:
        return 7
    if y==2 and x==1:
        return 8
    if y==2 and x==2:
        return 9

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_Screen("Welcome to TIC-TAC-TOE Game",black,260,250)
        text_Screen("press spacebar to play",black,260,290)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
        clock.tick(60)

def game_loop():
    exit_game=False
    img_list=[0 for i in range(10)]
    cursor_zero=True
    game_over=False
    player1=False
    player2=False
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            
            if player1:
                text_Screen("!!  Player1 WINS  !!",red,200,300)
                time.sleep(2)
            if player2:
                time.sleep(2)
                text_Screen("!!  Player2 WINS  !!",red,200,300)

            text_Screen("press enter to continue",red,200,350)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            gameWindow.fill(white)
            coord=pygame.mouse.get_pos()
            x=coord[0]
            y=coord[1]
            
            pygame.draw.line(gameWindow,black,[200,0],[200,600])
            pygame.draw.line(gameWindow,black,[400,0],[400,600])
            pygame.draw.line(gameWindow,black,[0,200],[600,200])
            pygame.draw.line(gameWindow,black,[0,400],[600,400])
            pygame.draw.rect(gameWindow,red,[0,0,600,600],5)
            pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.MOUSEBUTTONDOWN:
                    box=get_box(x,y)
                    if cursor_zero and img_list[box]==0:
                        img_list[box]=1
                        cursor_zero^=1
                    elif (not cursor_zero) and img_list[box]==0:
                        img_list[box]=2
                        cursor_zero^=1
                    # print(get_box(x,y))
                    
            zero_count=0
            for i in range(1,10):
                if img_list[i]==1:
                    draw_zero(i)
                if img_list[i]==2:
                    draw_cross(i)
                if img_list[i]==0:
                    zero_count+=1
                
            if (img_list[1]==img_list[2] and img_list[2]==img_list[3] and img_list[1]):
                pygame.draw.line(gameWindow,red,[0,100],[600,100],width=5)
                if img_list[1]==1:
                    player1=True
                    print("player 1 wins")
                if img_list[1]==2:
                    player2=True
                    print("player 2 wins")
                game_over=True
            if (img_list[4]==img_list[5] and img_list[5]==img_list[6] and img_list[4]):
                pygame.draw.line(gameWindow,red,[0,300],[600,300],width=5)
                if img_list[4]==1:
                    player1=True
                    print("player 1 wins")
                if img_list[4]==2:
                    player2=True
                    print("player 2 wins")
                game_over=True
            if (img_list[7]==img_list[8] and img_list[8]==img_list[9] and img_list[7]):
                pygame.draw.line(gameWindow,red,[0,500],[600,500],width=5)
                if img_list[7]==1:
                    player1=True
                    print("player 1 wins")
                if img_list[7]==2:
                    player2=True
                    print("player 2 wins")
                game_over=True
            if (img_list[1]==img_list[4] and img_list[4]==img_list[7] and img_list[1]):
                pygame.draw.line(gameWindow,red,[100,0],[100,600],width=5)
                if img_list[1]==1:
                    player1=True
                    print("player 1 wins")
                if img_list[1]==2:
                    player2=True
                    print("player 2 wins")
                game_over=True
            if (img_list[2]==img_list[5] and img_list[5]==img_list[8] and img_list[2]):
                pygame.draw.line(gameWindow,red,[300,0],[300,600],width=5)
                if img_list[2]==1:
                    player1=True
                    print("player 1 wins")
                if img_list[2]==2:
                    player2=True
                    print("player 2 wins")
                game_over=True
            if (img_list[3]==img_list[6] and img_list[6]==img_list[9] and img_list[3]):
                pygame.draw.line(gameWindow,red,[500,0],[500,600],width=5)
                if img_list[3]==1:
                    player1=True
                    print("player 1 wins")
                if img_list[3]==2:
                    player2=True
                    print("player 2 wins")
                game_over=True
            if (img_list[1]==img_list[5] and img_list[5]==img_list[9] and img_list[1]):
                pygame.draw.line(gameWindow,red,[0,0],[600,600],width=5)
                if img_list[1]==1:
                    player1=True
                    print("player 1 wins")
                if img_list[1]==2:
                    player2=True
                    print("player 2 wins")
                game_over=True
            if (img_list[3]==img_list[5] and img_list[5]==img_list[7] and img_list[3]):
                pygame.draw.line(gameWindow,red,[600,0],[0,600],width=5)
                if img_list[3]==1:
                    player1=True
                    print("player 1 wins")
                if img_list[3]==2:
                    player2=True
                    print("player 2 wins")
                game_over=True

            if zero_count==0 and (not game_over):
                text_Screen("draw game",red,200,200)
                welcome()
            if(cursor_zero):
                gameWindow.blit(zeroc,(x-25,y-25))
                
            else:
                gameWindow.blit(crossc,(x-25,y-25))
                
            
        pygame.display.update()
        # gameWindow.fill(black)
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()