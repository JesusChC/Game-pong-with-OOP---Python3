'''
  * @file    main.py 
  * @author  Jesus Ch
  * @version V1.0
  * @date    04-May-2020
  * @brief   Game Pong with OOP
'''

#Pygame modules
import pygame                   
from pygame.locals import *

#Classes of objects and modules
from constants import *
from ball import Ball
from paddle import Paddle
from inputs import handle_input

#Variable to FPS
Tick_Rate = 30

#Variable to While control
done = False

#Initialize pygame, construtor screen and title screen
pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height)) 
pygame.display.set_caption("Pong -- OOP")

#Constructor of a textfont
game_font = pygame.font.Font("freesansbold.ttf", 25)

#Constructor of screen refresh
refresh = pygame.time.Clock()

#Constructor of objects like ball, right paddle and left paddle
ball = Ball()
left_paddle = Paddle()
right_paddle = Paddle()

#Create position on screen of right paddle
right_paddle.rect.x = Screen_Width - right_paddle.rect.width - 5

#Variables for scores
player1_score = [0]
player2_score = [0]

#Main function control
while not done:
    
    #FPS on screen
    refresh.tick(Tick_Rate)

    #Events control pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Set the color on surface to the screen
    screen.fill(Color_Screen)
    
    #Call the function of handle inputs that contains the keyboard control for paddles
    handle_input(left_paddle, right_paddle)

    #Draw the ball on surface to the screen and it shows us the behavior of the ball (ball.update(xxxx))
    ball.draw(screen)
    ball.update(left_paddle, right_paddle, player1_score, player2_score)
    
    #Draw the paddles on surface to the screen
    left_paddle.draw(screen)
    right_paddle.draw(screen)
    
    #Visual lines (field)
    pygame.draw.aaline(screen, White, (Screen_Width // 2, 0),(Screen_Width // 2, Screen_Height))
    pygame.draw.aaline(screen, White, (0, 0), (Screen_Width, 0))
    pygame.draw.aaline(screen, White, (0, 479), (Screen_Width, 479))
    
    #Constructor of score for player-1, player-2 and its visualization on the screen
    player1_text = game_font.render(f"{player1_score[0]}", False, White)
    screen.blit(player1_text, (Screen_Width // 2 - 50, 1))
    player2_text = game_font.render(f"{player2_score[0]}", False, White)
    screen.blit(player2_text, (Screen_Width // 2 + 50, 1))
    
    #Update the display surface to the screen
    pygame.display.flip()

#Uninitialize all pygame modules
pygame.quit()

