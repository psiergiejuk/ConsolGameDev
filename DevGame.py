#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Dev Game

Cool consol game

This is main file of the game
"""

import sys
import urwid

from GameView import GameView
from GameModel import GameModel

__author__ = "Paweł Siergiejuk"
__date__ = "20/03/2018"
__time__ = "23:23:07"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class GameController():
    """
        (MVC) Class that control model and view

    """
    
    def __init__(self):
        self.game = GameModel()
        self.view = GameView(self)
        self.main_loop = None

    def handle_input(self, key):
        if key == 'f12':
            self.confirm_exit()
        else:
            pass

    def confirm_exit(self):
        self.game.exit_request()
        if self.view.confirm_exit():
            raise urwid.ExitMainLoop()

    def refresh(self, _loop, _data):
        self.view.refresh_view()
        self.main_loop.draw_screen()
        self.main_loop.set_alarm_in(1, self.refresh)

    def get_game_mode(self):
        return self.game.get_game_mode()

    def main(self):


        self.main_loop = urwid.MainLoop(self.view.layout, self.view.palette, unhandled_input=self.handle_input)
        self.main_loop.set_alarm_in(0, self.refresh)
        self.main_loop.run()


if __name__ == "__main__":
    game = GameController()
    game.main()


