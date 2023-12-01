import pygame

from config import GROUND_GAME, S_HEIGHT


class Bird(pygame.sprite.Sprite):
    def __init__(
        self, x: int, y: int, get_flying: bool, get_game_over: bool, set_flying: None
    ):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0

        self.get_flying = get_flying
        self.get_game_over = get_game_over
        self.set_flying = set_flying

        for number in range(1, 4):
            img = pygame.image.load(f"./images/bird__pos{number}.png")
            self.images.append(img)

        self.image = pygame.image.load("./images/bird__pos1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.clicked = False

    def update(self) -> None:
        """updates the picture for the effect of bird flight"""
        if self.get_flying():
            self.update_flight()

        if not self.get_game_over():
            self.update_game()
        else:
            self.update_game_over()

    def update_flight(self) -> None:
        """Update bird's position during flight"""
        self.velocity += 0.5

        if self.velocity > 8:
            self.velocity = 8

        if self.rect.bottom < S_HEIGHT - GROUND_GAME.get_height():
            self.rect.y += int(self.velocity)

        self.update_click()

    def update_game(self) -> None:
        """Update bird's state during the game"""
        if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            self.clicked = True
            self.velocity = -10

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

        self.image = self.images[self.index]
        self.image = pygame.transform.rotate(
            self.images[self.index], self.velocity)

    def update_game_over(self) -> None:
        """Update bird's state after the game is over"""
        self.image = pygame.transform.rotate(self.images[self.index], -90)

    def update_click(self) -> None:
        """Handle click event during flight"""
        if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            self.clicked = True
            self.velocity = -10
