import sys
import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1500, 820))
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)
font = pygame.font.Font(None, 36)   # None uses default font, 36 is size, what is None for and 36 means size?
small_font = pygame.font.Font(None, 24)
size = 20
snake_img = pygame.image.load("111.png")
snake_img = pygame.transform.scale(snake_img,(size,size))
snake_dir = "RIGHT"
snake_xy = [[40, 0], [20, 0], [0, 0]]
clock = pygame.time.Clock()
snake_speed = 8
food_x = random.randint(0, 800//20 - 1) * size
food_y = random.randint(0, 600//20 - 1) * size
score = 0
playing = True

def restart_game():
    global size, snake_dir, snake_img, snake_xy, score, food_x, food_y, playing
    size = 20
    snake_img = pygame.image.load("111.png")
    snake_img = pygame.transform.scale(snake_img,(size,size))
    snake_dir = "RIGHT"
    snake_xy = [[40, 0], [20, 0], [0, 0]]
    food_x = random.randint(0, 1500//20 - 1) * size
    food_y = random.randint(0, 820//20 - 1) * size
    score = 0
    playing = True

def game_over():
    playing = False
    for snake_x, snake_y in snake_xy:
        screen.blit(snake_img, (snake_x, snake_y))
    Game_over = font.render(f"Game over, score: {score}", True, (255, 0, 0))
    quit = font.render("Press X on top right coner to quit", True, (255, 255, 255))
    restart = font.render("Press r to restart", True, (255, 255, 255))
    screen.blit(Game_over, (200, 280))
    screen.blit(quit, (200, 310))
    screen.blit(restart, (200, 340))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Press R to restart
                restart_game()
    pygame.display.update()
    

while True:
    if playing == True:
        screen.fill("black")

        for snake_x, snake_y in snake_xy:
            screen.blit(snake_img, (snake_x, snake_y))

        screen.blit(snake_img, (food_x, food_y))

        pygame.display.update()

        if snake_xy[0][0] == food_x and snake_xy[0][1] == food_y:   # snake eat the food
            snake_xy.insert(0, [food_x, food_y])  # Insert at beginning (head)
            food_x = random.randint(0, 800//20 - 1) * size
            food_y = random.randint(0, 600//20 - 1) * size
            screen.blit(snake_img, (food_x, food_y))
            score += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pass
                if event.key == pygame.K_UP:
                    if snake_dir != "DOWN":
                        snake_dir = "UP"
                elif event.key == pygame.K_DOWN:
                    if snake_dir != "UP":
                        snake_dir = "DOWN"
                elif event.key == pygame.K_LEFT:
                    if snake_dir != "RIGHT":
                        snake_dir = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    if snake_dir != "LEFT":
                        snake_dir = "RIGHT"
        
        # snake moving
        for i in range(len(snake_xy)-1, 0, -1):     # range(len(snake_xy)-1, 0意思是最后一节到0，第二个 -1是每次减1
            snake_xy[i][0] = snake_xy[i - 1][0]    # snake_xy[i][0] 意思是第i节蛇的x
            snake_xy[i][1] = snake_xy[i - 1][1]

        if snake_dir == "UP":
            snake_xy[0][1] -= size # 20
        elif snake_dir == "DOWN":
            snake_xy[0][1] += size # 20
        elif snake_dir == "LEFT":
            snake_xy[0][0] -= size # 20
        elif snake_dir == "RIGHT":
            snake_xy[0][0] += size # 20

        clock.tick(snake_speed)

        if snake_xy[0][0] < 0 or snake_xy[0][1] < 0 or snake_xy[0][0] >= 1500 or snake_xy[0][1] >= 820: # snake hit the wall
            playing = False
            
        for body in snake_xy[1:]:  # 1:的意思是从第二个开始到最后一个
            if snake_xy[0][0] == body[0] and snake_xy[0][1] == body[1]:
                playing = False
    else:
        game_over()