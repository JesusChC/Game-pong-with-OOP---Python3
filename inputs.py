'''
  * @file    inputs.py 
  * @author  Jesus CH
  * @version V1.0
  * @date    04-May-2020
  * @brief   Game Pong with OOP
'''

#Pygame modules
import pygame
from pygame.locals import *

'''
Inputs module

This is a function that allows the paddles to be controlled
by the keyboard.
'''
def handle_input(left_paddle, right_paddle):
    
    #Internally process pygame event handlers
    pygame.event.pump()
    #Constructor to get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    #Call the up and down movement functions to the left paddle if the key pressed is W and S
    if keys[K_w]:
        left_paddle.move_up()
    elif keys[K_s]:
        left_paddle.move_down()

    #Call the up and down movement functions to the right paddle if the key pressed is O and L
    if keys[K_o]:
        right_paddle.move_up()
    elif keys[K_l]:
        right_paddle.move_down()


