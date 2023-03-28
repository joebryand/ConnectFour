import pygame
from .constants import STONE_SIZE

class Stone:
    def __init__(self,color):
        self.color = color
        self.border_color = tuple((abs(x-50)+x-50)/2 for x in self.color)
        self.highlight_color = tuple((abs(x+30)+x+30)/2 for x in self.color)
        self.border_width = 12
        self.radius = STONE_SIZE//2

    def change_color(self,color):
        self.color = color
        self.border_color = tuple((abs(x-50)+x-50)/2 for x in self.color)
        self.highlight_color = tuple((abs(x+30)+x+30)/2 for x in self.color)
        self.border_width = 12

    def draw(self,win,center):
        
        pygame.draw.circle(win,self.border_color,center,self.radius)
        pygame.draw.circle(win,self.highlight_color,center,self.radius-3)
        pygame.draw.circle(win,self.border_color,center,self.radius-self.border_width+2)
        pygame.draw.circle(win,self.color,center,self.radius-self.border_width)