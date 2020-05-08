'''
  * @file    paddle.py 
  * @author  Jesus Ch
  * @version V1.0
  * @date    04-May-2020
  * @brief   Game Pong with OOP
'''

#Pygame modules and module constants
import pygame
from constants import Screen_Width, Screen_Height, Color_Paddle, Paddle_Width, Paddle_Height

'''
Paddles class 

Provides utility functions to creating, drawing, moving and 
movements limted of the paddles
'''
class Paddle:
    
    #Constructor of paddle object, storing rectangular coordinates and movement speed.
    def __init__(self):
        self.rect = pygame.Rect(5, Screen_Height // 2 - Paddle_Height // 2, Paddle_Width, Paddle_Height)
        self.Speed = 10

    #Function to draw the paddles on surface to the screen
    def draw(self, screen):
        pygame.draw.rect(screen, Color_Paddle, self.rect)

    #Function to move paddle Up
    def move_up(self):
        self.rect.y -= self.Speed
        self.limit_screen()
    
    #Function to move paddle Down
    def move_down(self):
        self.rect.y += self.Speed
        self.limit_screen()

    #Function to limit movement of the paddles on the screen
    def limit_screen(self):
        self.rect.y = min(self.rect.y, Screen_Height - self.rect.height)
        self.rect.y = max(0, self.rect.y)

