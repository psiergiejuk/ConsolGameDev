#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Dev Game
GameView module


This file definid UI and handle it
"""

import sys
import urwid

__author__ = "Paweł Siergiejuk"
__date__ = "20/03/2018"
__time__ = "23:22:27"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"

class GameModes:
    WELCOME = 0
    EXIT = 1
    DEAD = 2

class GameView():
    """
        (MVC) Class that handle GUI

    """
    palette = [
        ('titlebar', 'dark red,bold', ''),
        ('option button', 'dark green,bold', ''),
        ('quit button', 'dark red', ''),
        ('getting quote', 'dark blue', ''),
        ('headers', 'white,bold', ''),
        ('change ', 'dark green', ''),
        ('change negative', 'dark red', '')]

    def __init__(self, controller):
        self.in_exit_mode = False
        self.controller = controller
        self.layout = None
        self.build_screen()

    def confirm_exit(self):
        self.controller.game.pause()
        self.in_exit_mode = True

    def build_screen(self):
        mode = self.controller.get_game_mode()
        if mode == GameModes.WELCOME:
            text = urwid.Text(u' Dev Game ' + __version__)
            header = urwid.AttrMap(text, 'titlebar')
            div = urwid.Divider()
            info = urwid.Text(u'Press F12 to Exit')
            header = urwid.AttrMap(text, 'titlebar')
            pile = urwid.Pile([header, div, info])
            self.layout = urwid.Filler(pile, valign='top')
        if mode == GameModes.EXIT:
            text = urwid.Text(u'Do you realy want to exit? y/n')
            header = urwid.AttrMap(text, 'titlebar')
            self.layout = urwid.Filler(header, valign='top')
            

    def refresh_view(self):
        return
        header_text = urwid.Text(u' Dev Game v0.1')
        header = urwid.AttrMap(header_text, 'titlebar')

        if not self.in_exit_mode:
            # Create the menu
            menu = urwid.Text([
                u'Press (', ('option button', u'P'), u') to open Property. ',
                u'Press (', ('quit button', u'Esc+Enter'), u') to exit.'
            ])
        else:
            menu = urwid.Text(['quit button', u"Do you really want to quit??? Y/N"])
            print(0)

        # Create the quotes box
        quote_text = urwid.Text(u'Press (S) to start the game!')
        quote_filler = urwid.Filler(quote_text, valign='top', top=1, bottom=1)
        v_padding = urwid.Padding(quote_filler, left=1, right=1)
        quote_box = urwid.LineBox(v_padding)

        # Assemble the widgets
        self.layout = urwid.Frame(header=header, body=quote_box, footer=menu)


if __name__ == "__main__":
    print("No UnitTest at this moment :(")


