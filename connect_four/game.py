import pygame
from .window import Window
from .stone import Stone
from .constants import YELLOW, RED

class Game:
    def __init__(self,win):
        self.win = win
        self.window = Window()
        self.reset()

    def reset(self):
        self.turn = 'red'
        self.turn_stone = Stone(RED)
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
        self.possible_moves = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
        
        self.winner = 0

    def update(self):
        self.win.fill((0,0,20))
        self.window.draw(self.win,self.board)
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

    def make_move(self,col,board): 
        if -1 < col < 7:
            for i in range(len(board)):
                i = len(board)-1-i
                if board[i][col] == 0:
                    if self.turn == 'red':
                        board[i][col] = Stone(RED)    
                    elif self.turn == 'yellow':
                        board[i][col] = Stone(YELLOW)
                    break
        return board
    
    def get_possible_moves(self,board):
        possible_moves = []
        for col in range(len(board[0])):
            for row in range(len(board)-1,-1,-1):    
                if board[row][col] == 0:
                    possible_moves.append((col,row))
                    break
        return possible_moves
    
    def win_check(self, board):
        if self.turn == 'red':
            color = RED
        elif self.turn == 'yellow':
            color = YELLOW

        win = False
        #horizontaal
        posible_start_locs = [0,1,2,3]
        for row in board:
            for start_loc in posible_start_locs:
                if row[start_loc] != 0:
                    if row[start_loc].color == color:
                        if row[start_loc+1] != 0:
                            if row[start_loc+1].color == color:
                                if row[start_loc+2] != 0:
                                    if row[start_loc+2].color == color:
                                        if row[start_loc+3] != 0:
                                            if row[start_loc+3].color == color:
                                                win = True


        #verticaal
        posible_start_locs = [0,1,2]
        for col in range(len(board[0])):
            for start_loc in posible_start_locs:
                if board[start_loc][col] != 0:
                    if board[start_loc][col].color == color:
                        if board[start_loc+1][col] != 0:
                            if board[start_loc+1][col].color == color:
                                if board[start_loc+2][col] != 0:
                                    if board[start_loc+2][col].color == color:
                                        if board[start_loc+3][col] != 0:
                                            if board[start_loc+3][col].color == color:
                                                win = True


        #diagonaal (righttop leftbottom)
        posible_start_locs = [[3,4,5,6],[3,4,5,6],[3,4,5,6]]
        for row in range(len(posible_start_locs)):
            for col in posible_start_locs[row]:
                if board[row][col] != 0:
                    if board[row][col].color == color:
                        if board[row+1][col-1] != 0:
                            if board[row+1][col-1].color == color:
                                if board[row+2][col-2] != 0:
                                    if board[row+2][col-2].color == color:
                                        if board[row+3][col-3] != 0:
                                            if board[row+3][col-3].color == color:
                                                win = True


        #diagonaal (lefttop rightbottom)
        posible_start_locs = [[0,1,2,3],[0,1,2,3],[0,1,2,3]]
        for row in range(len(posible_start_locs)):
            for col in posible_start_locs[row]:
                if board[row][col] != 0:
                    if board[row][col].color == color:
                        if board[row+1][col+1] != 0:
                            if board[row+1][col+1].color == color:
                                if board[row+2][col+2] != 0:
                                    if board[row+2][col+2].color == color:
                                        if board[row+3][col+3] != 0:
                                            if board[row+3][col+3].color == color:
                                                win = True

        if win == True:
            print(self.turn,'heeft gewonnen')

        return win
        
