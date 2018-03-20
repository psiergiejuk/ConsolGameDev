#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Dev Game
GameModel module


This file create GameModel and handle it
"""

import sys

__author__ = "Paweł Siergiejuk"
__date__ = "20/03/2018"
__time__ = "23:23:11"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class GameModes:
    WELCOME = 0
    EXIT = 1
    DEAD = 2

class GameModel():
    """
        (MVC) Class that handle model

    """
    
    def __init__(self):
        self.game_mode = GameModes.WELCOME

    def pause(self):
        pass

    def exit_request(self):
        self.game_mode = GameModes.EXIT    

    def get_game_mode(self):
        return self.game_mode


if __name__ == "__main__":
    print("No UnitTest at this moment :(")


