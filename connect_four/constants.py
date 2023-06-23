import pygame

WIDTH, HEIGHT = 760,420 #DO NOT CHANGE!
STONE_SIZE = 60 #DO NOT CHANGE!


RED = (160,10,10)
YELLOW = (140,140,10)

GLOW_IMAGE = pygame.image.load('ConnectFour/assets/glow.png')


# Game constants
SAVE_GAME = True

# AI constants
SEARCH_DEPTH = 6
ALPHA_BETA_PRUNING = True
VALUE_SYSTEM = "connected_pieces" # "possible_connect_fours" | "connected_pieces" | "random" | "combination"

# Player constants
PLAYER_NAME = 'Unknown'
PLAYER_AGE = 10

