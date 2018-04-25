#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Dev Game

Cool consol game

This is main file of the game
"""

import pygame
import sys
import os


__author__ = "Paweł Siergiejuk"
__date__ = "25/04/2018"
__time__ = "22:54:42"
__version__ = "v0.2"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class MapModel():
    """Model responsible for handling all item 
        related to map"""
    
    resolution = (500,500)

    def __init__(self):
        self.map = [[None] * self.resolution[0]] * self.resolution[1]

    def get(self):
        return self.DATA


class GameModel():
    """Top level of model of the game """
    

    def __init__(self):
        self.map = MapModel()


    def start_game(self):
        pass

    def exit_game(self):
        pass

    def get_game_map(self):
        pass

class GameState():
    """Object that store information about current 
        Game state"""
    
    INTRO = 0
    GAME = 1
    EXITING = 9

    def __init__(self):
        self.state = self.INTRO

    def start_game(self):
        self.state = self.GAME

    def stop_game(self):
        self.state = self.EXITING

    def get(self):
        return self.state


class DevGame():
    """Main Controller of Dev Game"""
    ICON = os.path.join("res", "logo32x32.png")
    WELCOME_IMAGE = os.path.join("res", "welcomeScreen.png")
    VERSION = __version__
    FPS = 20.0
    FONT_SIZE = 32

    def __init__(self):
        pygame.display.set_icon(pygame.image.load(self.ICON))
        pygame.display.set_caption("Dev Game " + self.VERSION)
        self.bg_image = pygame.image.load(self.WELCOME_IMAGE)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,600))
        self.running = False
        self.font = pygame.font.SysFont("Courier", self.FONT_SIZE)
        self.state = GameState()
        pygame.display.toggle_fullscreen()

    def start(self):
        self.running = True

        while self.running:
            #read event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
            #limit frame rate to given value
            self.clock.tick(self.FPS)
            
            #timing 
            self.tick()

            #draw the screen
            self.screen.blit(self.bg_image, (0, 0))
            self.draw()
            pygame.display.flip()
            
    def render_multiline_text(self, text, color, x, y):
        for i, l in enumerate(text.splitlines()):
            self.screen.blit(self.font.render(l, 1, color), (x, y + self.FONT_SIZE*i))

    def tick(self):
        pass

    def draw(self):
        #self.render_multiline_text("Welcome to Dev Game\nIf you want to learn Python click ENTER!", (200, 200,200), 100, 100)
        pass


     
if __name__=="__main__":
    pygame.init()
    game = DevGame()
    game.start()

