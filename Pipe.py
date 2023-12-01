import pygame
from config import PIPE_DIRECTION_DOWN, PIPE_DIRECTION_UP, PIPE_GAP


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, pos: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/pipe.png")
        self.rect = self.image.get_rect()

        if pos == PIPE_DIRECTION_DOWN:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - PIPE_GAP / 2]
        if pos == PIPE_DIRECTION_UP:
            self.rect.topleft = [x, y + PIPE_GAP / 2]

    def update(self):
        """pipe speed and removal"""
        self.rect.x -= 4
        if self.rect.right < 50:
            self.kill()
