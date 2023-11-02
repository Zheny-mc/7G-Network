FPS = 30
MINIMUM_SIDE = 500
BACKGROUND = (150, 90, 30)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
YELLOW = (255, 219, 139)
DIRTY_GREY = (128, 117, 63)
RED = (255, 0, 0)
IS_RUN = True
CELL_QTY_X = 3
CELL_QTY_Y = 5
PROCENT_CELL_BANNED = 30
MARGIN = 20

NUMS_BANNED_CELL = round(min(CELL_QTY_X, CELL_QTY_Y)**2 * PROCENT_CELL_BANNED / 100)
CELL_SIZE = int((MINIMUM_SIDE - MARGIN * 2) / max(CELL_QTY_X, CELL_QTY_Y))
WINDOW_SIZE = (CELL_SIZE * CELL_QTY_X + MARGIN * 2,
               CELL_SIZE * CELL_QTY_Y + MARGIN * 2)
