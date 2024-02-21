import pygame
import random
import math

pygame.init()


screen_width=800
screen_height=700
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Outer Path")
pygame.display.update()
font=pygame.font.SysFont(None,30)

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

clock=pygame.time.Clock()
fps=60

positions = []
for i in range(15):
    positions.append((random.randint(100,screen_width - 50),random.randint(100,screen_height - 50)))


# display the positions
while 1:
    gameWindow.fill(black)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    for pos in positions:
        pygame.draw.circle(gameWindow,red,pos,10)
    visited = [False for i in range(15)]
    curIndex = 0
    minHeight = math.inf
    for i in range(15):
        if positions[i][1] < minHeight:
            minHeight = positions[i][1]
            curIndex = i
        
    while not all(visited):
        visited[curIndex] = True
        minimun = math.inf
        for j in range(15):
            if curIndex != j:
                if not visited[j]:
                    distance = math.sqrt((positions[curIndex][0] - positions[j][0])**2 + (positions[curIndex][1] - positions[j][1])**2)
                    pygame.draw.line(gameWindow,white,positions[curIndex],positions[j],2)
                    pygame.display.update()
                    pygame.time.delay(100)
                    pygame.draw.line(gameWindow,black,positions[curIndex],positions[j],2)
                    pygame.display.update()
                    pygame.time.delay(100)
                    if distance < minimun:
                        minimun = distance
                        index = j
        
        pygame.draw.line(gameWindow,white,positions[curIndex],positions[index],2)
        curIndex = index
        
        
    pygame.display.update()
    clock.tick(fps)