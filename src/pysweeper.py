import asyncio
import sys
import pygame as pg

from .config import Config, Window


class Pysweeper:
    def __init__(self):
        pg.init()
        window = Window(800, 600, "Pysweeper")
        pg.display.set_caption(window.title)
        screen = pg.display.set_mode((window.width, window.height))
        
        self.config = Config(
            screen=screen,
            clock=pg.time.Clock(),
            fps=30,
            window=window,
        )

    def check_quit_event(self, event):
        if event.type == pg.QUIT:
            self.quit()

    