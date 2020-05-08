'''
  * @file    ball.py 
  * @author  Jesus CH
  * @version V1.0
  * @date    04-May-2020
  * @brief   Game Pong with OOP
'''

#Pygame modules and module constants
import pygame, random
from constants import Screen_Width, Screen_Height, Color_Ball

'''
Ball class 

Provides utility functions to creating, drawing, updating
and checking if two rectangles overlap
'''
class Ball:

    #Constructor of the ball object and its attributes.
    def __init__(self):
        self.pos_x = Screen_Width // 2
        self.pos_y = Screen_Height // 2
        self.speed_ball = 5 * random.choice((1,-1))
        self.vel_x = self.speed_ball * random.choice((1,-1))
        self.vel_y = self.speed_ball * random.choice((1,-1))
        self.radius = 10
    
    #Function to draw the ball on surface to the screen
    def draw(self, screen):
        pygame.draw.circle(screen, Color_Ball, (self.pos_x, self.pos_y), self.radius)

    #Function to get rectangular coordinates of the ball.
    def get_rect(self):
        return pygame.Rect(self.pos_x - self.radius, self.pos_y - self.radius, self.radius * 2, self.radius *2)

    #Function to update the behavior of the ball.
    def update(self, left_paddle, right_paddle, player1_score, player2_score):
        #Ball movements
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        #Conditions to setting field limits and bounce
        #Limit top and bounce
        if self.pos_y > Screen_Height - self.radius * 2:
            self.vel_y *= -1 
            
        #Limit right and reset the ball
        if self.pos_x > Screen_Width - self.radius * 2:
            player1_score[0] += 1
            self.__init__()

        #Limit Left reset the ball
        if self.pos_x <  self.radius * 2:
            player2_score[0] += 1
            self.__init__()
            
        #Limit bottom and bounce
        if self.pos_y < self.radius * 2:
            self.vel_y *= -1 
        
        #Conditions to check if two rectangles overlap and reverse the direction of the ball, in this case paddle and ball.
        if self.get_rect().colliderect(left_paddle.rect) or self.get_rect().colliderect(right_paddle.rect):
            self.vel_x *= -1
        