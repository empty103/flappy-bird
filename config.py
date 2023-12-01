from pygame import image, transform, display

S_WIDTH, S_HEIGHT = 1024, 768

BG_GAME = image.load("./images/bg.png")
GROUND_GAME = image.load("./images/ground.png")
BG_GAME = transform.scale(BG_GAME, (S_WIDTH, S_HEIGHT))

GROUND_GAME = transform.scale(GROUND_GAME, (S_WIDTH, GROUND_GAME.get_height()))
PIPE_GAP = 200
PIPE_FREQUENCY = 2000
FPS = 60

BIRD_INITIAL_X = 200
PIPE_INITIAL_X = -2000
PIPE_INITIAL_Y = -2000
BUTTON_X = S_WIDTH // 2 - 70
BUTTON_Y = S_HEIGHT // 2

PIPE_DIRECTION_UP = -1
PIPE_DIRECTION_DOWN = 1
GROUND_MOVING_SPEED = 5

BIRD_INITIAL_X = 100

SURFACE = display.set_mode(size=(S_WIDTH, S_HEIGHT))
