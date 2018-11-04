

# game options/settings

TITLE = "Skybound"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'Times New Roman'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# World properties

GRAVITY = 0.75
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
MOB_LAYER = 2
POW_LAYER = 1
PLATFORM_LAYER = 1
CLOUD_LAYER = 0

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
JUMP_ACC = -20

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4,),
                 (WIDTH / 2 - 50, HEIGHT / 2),
                 (WIDTH / 2 - 50, HEIGHT / 4)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (30, 144, 255)
GOLD = (212, 175, 55)
