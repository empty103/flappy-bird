import pygame
from config import SURFACE


class Button:
    def __init__(self, x: int, y: int):
        self.image = pygame.image.load("./images/restart.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self) -> bool:
        action = False
        pos_btn = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_btn):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        SURFACE.blit(self.image, (self.rect.x, self.rect.y))
        return action
