import pygame
import random
from pygame import Surface
from Bird import Bird
from Button import Button
from Pipe import Pipe
from config import (
    PIPE_FREQUENCY,
    S_WIDTH,
    S_HEIGHT,
    BG_GAME,
    GROUND_GAME,
    FPS,
    SURFACE,
    BIRD_INITIAL_X,
    PIPE_INITIAL_Y,
    PIPE_INITIAL_X,
    BUTTON_X,
    BUTTON_Y,
    PIPE_DIRECTION_UP,
    PIPE_DIRECTION_DOWN,
    GROUND_MOVING_SPEED,
    BIRD_INITIAL_X
)


class FlappyBirdGame:
    def __init__(self):
        self.ground_moving_speed = GROUND_MOVING_SPEED
        self.ground_moving = 0
        self.run_game = True
        self.flying = False
        self.game_over = False
        self.last_pipe = pygame.time.get_ticks() - PIPE_FREQUENCY

        self.bird_group = pygame.sprite.Group()
        self.flappy = Bird(
            BIRD_INITIAL_X,
            (S_HEIGHT / 2),
            self.get_flying_status,
            self.get_game_over_status,
            self.set_flying_status,
        )
        self.bird_group.add(self.flappy)

        self.pipe_group = pygame.sprite.Group()
        bottom_pipe = Pipe(PIPE_INITIAL_X, (S_HEIGHT / 2), PIPE_DIRECTION_DOWN)
        top_pipe = Pipe(PIPE_INITIAL_Y, (S_HEIGHT / 2), PIPE_DIRECTION_UP)

        self.pipe_group.add(bottom_pipe)
        self.pipe_group.add(top_pipe)

        self.btn = Button(BUTTON_X, BUTTON_Y)

    def get_flying_status(self) -> bool:
        return self.flying

    def get_game_over_status(self) -> bool:
        return self.game_over

    def set_flying_status(self, status: bool) -> None:
        self.flying = status

    def draw_background(self, surface: Surface):
        surface.blit(source=BG_GAME, dest=(0, 0))

    def draw_ground(self, surface: Surface):
        surface.blit(
            GROUND_GAME, (self.ground_moving, S_HEIGHT -
                          GROUND_GAME.get_height())
        )
        surface.blit(
            GROUND_GAME,
            (
                self.ground_moving + GROUND_GAME.get_width(),
                S_HEIGHT - GROUND_GAME.get_height(),
            ),
        )

    def reset_game(self):
        self.pipe_group.empty()
        self.flappy.rect.x = BIRD_INITIAL_X
        self.flappy.rect.y = S_HEIGHT / 2

    def run(self):
        clock = pygame.time.Clock()

        while self.run_game:
            self.handle_events()
            self.update_game()
            self.render()

            clock.tick(FPS)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False
            elif (
                event.type == pygame.MOUSEBUTTONUP
                and not self.flying
                and not self.game_over
            ):
                self.flying = True

    def update_game(self):
        if not self.game_over and self.flying:
            self.update_pipes()
            self.move_ground()

        self.bird_group.update()

        if self.flappy.rect.bottom >= S_HEIGHT - GROUND_GAME.get_height():
            self.game_over = True
            self.flying = False

        if (
            pygame.sprite.groupcollide(
                self.bird_group, self.pipe_group, False, False)
            or self.flappy.rect.top < 0
        ):
            self.game_over = True

    def update_pipes(self):
        time_now = pygame.time.get_ticks()
        if (time_now - self.last_pipe) > PIPE_FREQUENCY:
            # генерация случайной высоты трубы.
            pipe_height = random.randint(-100, 100)
            bottom_pipe = Pipe(S_WIDTH, (S_HEIGHT / 2) + pipe_height, 1)
            top_pipe = Pipe(S_WIDTH, (S_HEIGHT / 2) + pipe_height, -1)
            self.pipe_group.add(bottom_pipe)

            self.pipe_group.add(top_pipe)
            self.last_pipe = time_now

        self.pipe_group.update()

    def move_ground(self):
        self.ground_moving -= self.ground_moving_speed
        if abs(self.ground_moving) >= GROUND_GAME.get_width():
            self.ground_moving = 0

    def render(self):
        self.draw_background(SURFACE)
        self.draw_ground(SURFACE)
        self.bird_group.draw(SURFACE)
        self.pipe_group.draw(SURFACE)

        if self.game_over:
            if self.btn.draw():
                self.game_over = False
                self.reset_game()

        pygame.display.flip()


if __name__ == "__main__":
    game = FlappyBirdGame()

    try:
        game.run()
    finally:
        pygame.quit()
