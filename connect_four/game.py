import pygame
from .window import Window
from .board import Board
from .stone import Stone
from .constants import YELLOW, RED

class Game:
    def __init__(self,win):
        self.win = win
        self.window = Window()
        self.reset()

    def reset(self):
        self.turn = 'yellow'
        self.turn_stone = Stone(YELLOW)
        self.game_board = Board()
        self.possible_moves = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
        self.winner = 0

    def update(self):
        self.win.fill((0,0,20))
        self.window.draw(self.win,self.game_board.board)
        self.turn_stone.draw(self.win,(50,40))
        self.window.draw_possible_moves(self.win,self.possible_moves)
        pygame.display.update()
        return self.winner
    
    def change_turn(self):
        if self.turn == 'red':
            self.turn = 'yellow'
            self.turn_stone.change_color(YELLOW)
        elif self.turn == 'yellow':
            self.turn = 'red'
            self.turn_stone.change_color(RED)

    def make_move(self,col):
        self.game_board.make_move(col,self.turn)

    def get_possible_moves(self):
        return self.game_board.get_possible_moves()

    def win_check(self):
        return self.game_board.win_check(self.turn)
