import worldBuilder


PI = 3.14159265358979323

BLOCK_SIZE = 64
GRID_SIZE = 128
RENDER_DISTANCE = 128

GAME_WORLD = worldBuilder.build(GRID_SIZE)


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


SPEED_M = 0.002 * BLOCK_SIZE
SPEED_R = 0.0004