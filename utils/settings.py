import pygame

pygame.init()
pygame.font.init()

# Colors
BLACK = (0, 0, 0)
GRAY = (228, 228, 228)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (131, 247, 236)

"""Default Settings"""
# Frames per second
FPS = 60

# Dimensions
WIDTH = 900
HEIGHT = 600

# Font getter
def get_font(size: int):
    return pygame.font.SysFont("monospace", size)


def get_font_bold(size: int):
    return pygame.font.SysFont("monospace b228", size)