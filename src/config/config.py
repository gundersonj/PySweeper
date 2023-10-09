import os
import pygame as pg

from src.config.window import Window


class Config:
    def __init__(
        self,
        screen: pg.Surface,
        clock: pg.time.Clock,
        fps: int,
        window: Window,
    ) -> None:
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.window = window
        
    def tick(self) -> None:
        self.clock.tick(self.fps)