import pygame
import time
import random
from pygame import mixer
x=pygame.init()

screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("JD GAMEZONE")
pygame.display.update()



white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
high_score=0

clock=pygame.time.Clock()
fps=30





font=pygame.font.SysFont(None,55)

def text_Screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def draw_snake(snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,white,[x,y,snake_size,snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_Screen("Welcome to Snakes Game",black,260,250)
        text_Screen("press spacebar to play",black,232,290)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
        clock.tick(60)


def game_loop():
    score=0
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=45
    snake_size=20
    MOVE_RIGHT=True
    MOVE_LEFT=False
    MOVE_UP=False
    MOVE_DOWN=False
    snake_list=[]
    snake_length=1

    x_velocity=0
    y_velocity=0

    x_food=random.randint(50,screen_height-50)
    y_food=random.randint(50,screen_height-50)
    while not exit_game:
        if game_over:
            global high_score
            high_score= max(score,high_score)
            gameWindow.fill(white)
            text_Screen("Game Over ! press enter to continue",red,100,200)
            text_Screen("high score is : "+str(high_score),red,100,230)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT and x_velocity==0:
                        x_velocity=10
                        y_velocity=0
                    if event.key==pygame.K_LEFT and x_velocity==0:
                        x_velocity=-10
                        y_velocity=0
                    if event.key==pygame.K_UP and y_velocity==0:
                        y_velocity=-10
                        x_velocity=0
                    if event.key==pygame.K_DOWN and y_velocity==0:
                        y_velocity=10
                        x_velocity=0

            snake_x+=x_velocity
            snake_y+=y_velocity
            snake_x%=900
            snake_y%=600
            if abs(snake_x-x_food)<=6 and abs(snake_y-y_food)<=6:
                x_food=random.randint(50,screen_height-50)
                y_food=random.randint(50,screen_height-50)
                score+=10
                snake_length+=2
                mixer.init()
                mixer.music.load("beep.mp3")
                mixer.music.play()

            gameWindow.fill(black)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if(len(snake_list)>snake_length):
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True

            text_Screen("Score : "+str(score),red,5,5)
            pygame.draw.rect(gameWindow,red,[x_food,y_food,snake_size,snake_size])
            draw_snake(snake_list,snake_size)


        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()
