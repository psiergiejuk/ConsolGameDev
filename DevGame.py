#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Dev Game

Cool consol game

This is main file of the game
"""

import sys
import urwid

__author__ = "Paweł Siergiejuk"
__date__ = "03/03/2018"
__time__ = "21:32:09"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class GameModel():
    """
        (MVC) Class that handle model

    """
    
    def __init__(self):
        pass

class GameView(urwid.WidgetWrap):
    """
        (MVC) Class that handle GUI

    """
    def __init__(self):
        pass

class GameController():
    """
        (MVC) Class that control model and view

    """
    
    def __init__(self):
        pass

    def main(self):
        palette = [
            ('titlebar', 'dark red,bold', ''),
            ('option button', 'dark green,bold', ''),
            ('quit button', 'dark red', ''),
            ('getting quote', 'dark blue', ''),
            ('headers', 'white,bold', ''),
            ('change ', 'dark green', ''),
            ('change negative', 'dark red', '')]

        header_text = urwid.Text(u' Dev Game v0.1')
        header = urwid.AttrMap(header_text, 'titlebar')

        # Create the menu
        menu = urwid.Text([
            u'Press (', ('option button', u'P'), u') to open Property. ',
            u'Press (', ('quit button', u'Q'), u') to quit.'
        ])

        # Create the quotes box
        quote_text = urwid.Text(u'Press (S) to start the game!')
        quote_filler = urwid.Filler(quote_text, valign='top', top=1, bottom=1)
        v_padding = urwid.Padding(quote_filler, left=1, right=1)
        quote_box = urwid.LineBox(v_padding)

        # Assemble the widgets
        layout = urwid.Frame(header=header, body=quote_box, footer=menu)
        def handle_input(key):
            if key == 'R' or key == 'r':
                refresh(main_loop, '')

            if key == 'Q' or key == 'q':
                raise urwid.ExitMainLoop()

        def refresh(_loop, _data):
            print("refresh")

        main_loop = urwid.MainLoop(layout, palette, unhandled_input=handle_input)
        main_loop.set_alarm_in(0, refresh)
        main_loop.run()


if __name__ == "__main__":
    game = GameController()
    game.main()


