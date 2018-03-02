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
__time__ = "00:21:33"
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
    palette = [
        ('body',         'black',      'light gray', 'standout'),
        ('header',       'white',      'dark red',   'bold'),
        ('screen edge',  'light blue', 'dark cyan'),
        ('main shadow',  'dark gray',  'black'),
        ('line',         'black',      'light gray', 'standout'),
        ('bg background','light gray', 'black'),
        ('bg 1',         'black',      'dark blue', 'standout'),
        ('bg 1 smooth',  'dark blue',  'black'),
        ('bg 2',         'black',      'dark cyan', 'standout'),
        ('bg 2 smooth',  'dark cyan',  'black'),
        ('button normal','light gray', 'dark blue', 'standout'),
        ('button select','white',      'dark green'),
        ('line',         'black',      'light gray', 'standout'),
        ('pg normal',    'white',      'black', 'standout'),
        ('pg complete',  'white',      'dark magenta'),
        ('pg smooth',     'dark magenta','black')
        ]
    
    def __init__(self, controller):
        self.controller = controller
        urwid.WidgetWrap.__init__(self, self.main_window())

    def main_window(self):
        w = urwid.BarGraph(['bg background','bg 1','bg 2'], satt=None)
        return w

    def update_graph(self, force_update=False):
        pass

class GameController():
    """
        (MVC) Class that control model and view

    """
    
    def __init__(self):
        self.view = GameView(self)
        self.model = GameModel()
        self.loop = None

    def main(self):
        self.loop = urwid.MainLoop(self.view, self.view.palette)
        self.loop.run()


if __name__ == "__main__":
    def exit_on_q(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    palette = [
        ('banner', 'black', 'light gray'),
        ('streak', 'black', 'dark red'),
        ('bg', 'black', 'dark blue'),]

    txt = urwid.Text(('banner', u" Welcome in Dev Game"), align='center')
    map1 = urwid.AttrMap(txt, 'streak')
    fill = urwid.Filler(map1)
    map2 = urwid.AttrMap(fill, 'bg')
    loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
    loop.run()
    #game = GameController()
    #game.main()


