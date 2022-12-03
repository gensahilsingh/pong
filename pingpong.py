import pygame
import sys
from time import sleep
import os
import tkinter

pygame.init()

icon=pygame.image.load("background.png")
background=pygame.image.load("background.png")
clock=pygame.time.Clock()
width=800
height=600
green=(0, 110, 0)
screen=pygame.display.set_mode((width, height))
color1=(0, 0, 0)
color2=(255,255,255)
X_speed=10
Y_speed=10
ball=pygame.Rect(width/2, height/2, 30, 30)
player1=pygame.Rect(width-20, height/2-70, 10, 140)
player2=pygame.Rect(width-790, height/2-70, 10, 140)
level_rect=pygame.Rect(width/2-7, height-64, 30, 30)
font = pygame.font.SysFont('Comic Sans Ms', 20)
textX= width-20
testY= height/2-70
player1score=0
player2score=0
font_color=(0,0,0)
font_obj=pygame.font.Font("freesansbold.ttf",25)
playerspeed=0
player2speed=0
fps=30
speed=0
#button_level=tkinter.Button()

def player_movement():
    player1.y+=playerspeed
    player2.y+=player2speed
    if player1.top <= 0:
       player1.top=0
    if player1.bottom >= height:
        player1.bottom=height
    if player2.top <= 0:
       player2.top=0
    if player2.bottom >= height:
        player2.bottom=height

def function_ball():
    global text_obj
    global X_speed, Y_speed
    global player1score, player2score
    ball.x+=X_speed
    ball.y+=Y_speed
    if ball.bottom >= height or ball.top <= 0:
        Y_speed*=-1
    if ball.right >= width:
        player2score+=1
        ball.x=width/2
        ball.y=height/2
        sleep(0.5)
    if ball.left <= 0:
        player1score+=1
        ball.x=width/2
        ball.y=height/2
        sleep(0.5)
    if pygame.Rect.colliderect(ball, player1) == True:
        X_speed*=-1
        Y_speed*=-1
        player1score+=1
        #text_obj=font_obj.render((player1score, player2score), True, font_color)
        print(player1score)
        print(player2score)
        os.system('clear')
    if pygame.Rect.colliderect(ball, player2) == True:
        X_speed*=-1
        Y_speed*=-1
        player2score+=1
        #pygame.display.set_caption((player2score))
        #text_obj=font_obj.render((player1score, player2score), True, font_color)
        print(player2score)
        print(player1score)
        os.system('clear')


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                playerspeed-=10
            if event.key==pygame.K_DOWN:
                playerspeed+=10
            if event.key==pygame.K_w:
                player2speed-=10
            if event.key==pygame.K_s:
                player2speed+=10
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                playerspeed+=10
            if event.key==pygame.K_DOWN:
                playerspeed-=10
            if event.key==pygame.K_w:
                player2speed+=10
            if event.key==pygame.K_s:
                player2speed-=10
        if player1score==30:
            pygame.quit()
        if player2score==30:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_l:
                if speed<4:
                    fps*=2
                    speed+=1
            if event.key==pygame.K_d:
                if speed>-4:
                    fps/=2
                    speed-=1
                #clock.tick(fps)
            #if event.==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()        

    function_ball()
    player_movement()
    screen.fill((color2))
    screen.blit(background, (0, 0))
    text_obj=font_obj.render(f"{player1score}", True, font_color)
    text_obj2=font_obj.render(f"{player2score}", True, font_color)
    level_text_obj=font_obj.render(f"{speed}", True, color2)
    screen.blit(text_obj, (width-60, 20))
    screen.blit(text_obj2, (60, 20))
    pygame.draw.rect(screen, color1, level_rect)
    screen.blit(level_text_obj, (width/2, height-60))
    pygame.draw.ellipse(screen, green, ball)
    pygame.draw.rect(screen, color2, player1)
    pygame.draw.rect(screen, color2, player2)
    pygame.display.flip()
    clock.tick(fps)