import pygame
import random
from time import sleep
import os

pygame.init()

screenWidth = 900
screenHeight = 600
white = (166, 173, 200)
grey = (49, 50, 68)
red = (243, 139, 168)
base = (24, 24, 37)
violet = (203, 166, 247)
exitGame = False

gameWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('SB Snake')
pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont("Noto Sans", 35)


def text_screen(text, colour, x, y, font=font):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, (x, y))


def plot_snake(gameWindow, color, snk_list, size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, size, size])


def welcome():
    global exitGame
    while not exitGame:
        gameWindow.fill(base)
        text_screen('Welcome To Snake', violet, 280, 250)
        text_screen('Press Spacebar to Play!', red, 250, 300)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                exitGame = True
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
        clock.tick(30)


def game_loop():
    global exitGame
    if not os.path.exists('highscore.txt'):
        with open('highscore.txt', 'w') as f:
            f.write('0')
    with open('highscore.txt', 'r') as f:
        highscore = f.read()
    xkeys = True
    ykeys = True
    game_over = False
    snakex = 45
    snakey = 100
    snake_size = 20
    fps = 55
    vel_x = 0
    vel_y = 0
    foodx = random.randint(0, screenWidth-200)
    foody = random.randint(0, screenHeight-200)
    food_size = 9
    score = 0
    snk_list = []
    snk_len = 1
    while not exitGame:
        if game_over:
            sleep(0.5)
            gameWindow.fill(base)
            text_screen('GAME OVER', red,  320, 220)
            text_screen('Press enter to play again', violet, 230, 280)
            text_screen('Score: '+str(score), white, 340, 360)
            with open('highscore.txt', 'w') as fw:
                fw.write(str(highscore))
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    exitGame = True
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_RETURN:
                        game_loop()
        else:
            gameWindow.fill(base)
            text_screen(str(score), grey, screenWidth/2 + 10 - len(str(score))*150, -50, font=pygame.font.SysFont("Noto Sans", 500))
            text_screen('Highscore: ' + str(highscore), white, screenWidth/2-70, screenHeight-50, font=pygame.font.SysFont("Noto Sans", 20))
            pygame.draw.circle(gameWindow, red, (foodx+food_size/2, foody+food_size/2), food_size, width=5)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    exitGame = True

                if ev.type == pygame.KEYDOWN:

                    if ev.key == pygame.K_RIGHT:
                        if xkeys:
                            if len(snk_list) > 2:
                                b = snk_list[2][1]
                                if abs(snakey-b) < 20:
                                    while abs(snakey-b) < 20:
                                        snakex += vel_x
                                        snakey += vel_y
                                        pygame.display.update()
                                        clock.tick(fps)
                                    vel_y = 0
                                    vel_x = 5
                                    xkeys = False
                                    ykeys = True
                                else:
                                    vel_y = 0
                                    vel_x = 5
                                    xkeys = False
                                    ykeys = True
                            else:
                                vel_y = 0
                                vel_x = 5
                                xkeys = False
                                ykeys = True
                    if ev.key == pygame.K_LEFT:
                        if xkeys:
                            if len(snk_list) > 2:
                                b = snk_list[2][1]
                                if abs(snakey-b) < 20:
                                    while abs(snakey-b) < 20:
                                        snakex += vel_x
                                        snakey += vel_y
                                        pygame.display.update()
                                        clock.tick(fps)
                                    vel_y = 0
                                    vel_x = -5
                                    xkeys = False
                                    ykeys = True
                                else:
                                    vel_y = 0
                                    vel_x = -5
                                    xkeys = False
                                    ykeys = True
                            else:
                                vel_y = 0
                                vel_x = -5
                                xkeys = False
                                ykeys = True
                    if ev.key == pygame.K_UP:
                        if ykeys:
                            if len(snk_list) > 2:
                                b = snk_list[2][0]
                                if abs(snakex-b) < 20:
                                    while abs(snakex-b) < 20:
                                        snakex += vel_x
                                        snakey += vel_y
                                        pygame.display.update()
                                        clock.tick(fps)
                                    vel_x = 0
                                    vel_y = -5
                                    xkeys = True
                                    ykeys = False
                                else:
                                    vel_x = 0
                                    vel_y = -5
                                    xkeys = True
                                    ykeys = False
                            else:
                                vel_x = 0
                                vel_y = -5
                                xkeys = True
                                ykeys = False

                    if ev.key == pygame.K_DOWN:
                        if ykeys:
                            if len(snk_list) > 2:
                                b = snk_list[2][0]
                                if abs(snakex-b) < 20:
                                    while abs(snakex-b) < 20:
                                        snakex += vel_x
                                        snakey += vel_y
                                        pygame.display.update()
                                        clock.tick(fps)
                                    vel_x = 0
                                    vel_y = 5
                                    xkeys = True
                                    ykeys = False
                                else:
                                    vel_x = 0
                                    vel_y = 5
                                    xkeys = True
                                    ykeys = False
                            else:
                                vel_x = 0
                                vel_y = 5
                                xkeys = True
                                ykeys = False

            snakex += vel_x
            snakey += vel_y
            if abs(snakex-foodx) < 15.5 and abs(snakey-foody) < 15.5:
                foodx = random.randint(0, 800)
                foody = random.randint(0, 500)
                score += 1
                snk_len += 4
                if int(score) > int(highscore):
                    highscore = score
            head = []
            head.append(snakex)
            head.append(snakey)
            snk_list.append(head)
            plot_snake(
                gameWindow, violet, snk_list, snake_size)
            if len(snk_list) > snk_len:
                del snk_list[0]
            if snakex < 0:
                snakex = screenWidth
            if snakex > screenWidth:
                snakex = 0
            if snakey < 0:
                snakey = screenHeight
            if snakey > screenHeight:
                snakey = 0
            if head in snk_list[:-1]:
                sleep(1)
                game_over = True

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
