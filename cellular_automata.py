import pygame

pygame.init()

screen_width=700
screen_height=800
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("CELLULAR AUTOMATA")
pygame.display.update()
font=pygame.font.SysFont(None,30)

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
button_color = pygame.Color("dodgerblue2")
hover_color = pygame.Color("deepskyblue")

rule_input = ""
input_rect = pygame.Rect(10, 710, 140, 32)
button_rect = pygame.Rect(160, 710, 80, 32)

clock=pygame.time.Clock()
fps=30

grid = [[0 for i in range(50)]]
grid[0][len(grid[0])//2] = 1

rule_number = 0


def update_grid():
    global rule_number
    binary_rule_number = bin(rule_number)[2:]
    binary_rule_number = binary_rule_number.zfill(8)
    print(binary_rule_number)
    last_row = grid[-1]
    new_row = [0]*len(last_row)
    for i in range(1, len(last_row)-1):
        current_pattern=str(last_row[i-1])+str(last_row[i])+str(last_row[i+1])
        current_pattern_index=int(current_pattern,2)
        new_row[i]=int(binary_rule_number[7-current_pattern_index])
    grid.append(new_row)

def reset_grid():
    global grid
    grid=[[0 for i in range(50)]]
    grid[0][len(grid[0])//2]=1

def game():
    global grid, rule_number, rule_input
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    try:
                        rule_number = int(rule_input)
                        print(rule_number)
                        reset_grid()
                        rule_input = ""
                    except ValueError:
                        rule_input = ""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        rule_number = int(rule_input)
                        reset_grid()
                        rule_input = ""
                    except ValueError:
                        rule_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    rule_input = rule_input[:-1]
                else:
                    rule_input += event.unicode
            
        gameWindow.fill(white)
        square_width = 700 / len(grid[0])
        # draw grid lines
        for i in range(len(grid[0])):
            pygame.draw.line(gameWindow,black,(0,i*square_width),(screen_width,i*square_width))
            pygame.draw.line(gameWindow,black,(i*square_width,0),(i*square_width,700))
        
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i]==1:
                    pygame.draw.rect(gameWindow,black,(i*square_width,j*square_width,square_width,square_width))
        
        if len(grid) < 700/square_width:
            update_grid()
            
        # Draw input field and button
        pygame.draw.rect(gameWindow, (255, 150, 150), input_rect)
        pygame.draw.rect(gameWindow, button_color, button_rect)

        input_text = font.render(rule_input, True, white)
        gameWindow.blit(input_text, (input_rect.x + 5, input_rect.y + 5))

        button_text = font.render("Update", True, white)
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(gameWindow, hover_color, button_rect)
        else:
            pygame.draw.rect(gameWindow, button_color, button_rect)

        gameWindow.blit(button_text, (button_rect.x + 10, button_rect.y + 5))



        clock.tick(fps)
        pygame.display.update()
    quit()
    
game()