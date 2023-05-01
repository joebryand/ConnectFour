import pygame
from .stone import Stone
from .constants import YELLOW, RED

class Board:
    def __init__(self):
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
        self.moves = []

    def cancel_move(self):
        try:
            last_move = self.moves.pop(len(self.moves)-1)
            #print("cancel:",last_move)
            self.board[last_move[0]][last_move[1]] = 0
            return True
        
        except:
            print("Warning! Could not cancel last move")
            return False
        
    def make_move(self,col,turn): 
        if -1 < col < 7:
            for i in range(len(self.board)):
                i = len(self.board)-1-i
                if self.board[i][col] == 0:
                    self.moves.append((i,col))
                    if turn == 'red':
                        self.board[i][col] = Stone(RED)    
                    elif turn == 'yellow':
                        self.board[i][col] = Stone(YELLOW)
                    break
                
    def get_possible_moves(self):
        possible_moves = []
        for col in range(len(self.board[0])):
            for row in range(len(self.board)-1,-1,-1):    
                if self.board[row][col] == 0:
                    possible_moves.append((col,row))
                    break
        return possible_moves
    
    def win_check(self,turn):
        if turn == 'red':
            color = RED
        elif turn == 'yellow':
            color = YELLOW

        win = False
        #horizontaal
        possible_start_locs = [0,1,2,3]
        for row in self.board:
            for start_loc in possible_start_locs:
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
        possible_start_locs = [0,1,2]
        for col in range(len(self.board[0])):
            for start_loc in possible_start_locs:
                if self.board[start_loc][col] != 0:
                    if self.board[start_loc][col].color == color:
                        if self.board[start_loc+1][col] != 0:
                            if self.board[start_loc+1][col].color == color:
                                if self.board[start_loc+2][col] != 0:
                                    if self.board[start_loc+2][col].color == color:
                                        if self.board[start_loc+3][col] != 0:
                                            if self.board[start_loc+3][col].color == color:
                                                win = True


        #diagonaal (righttop leftbottom)
        possible_start_locs = [[3,4,5,6],[3,4,5,6],[3,4,5,6]]
        for row in range(len(possible_start_locs)):
            for col in possible_start_locs[row]:
                if self.board[row][col] != 0:
                    if self.board[row][col].color == color:
                        if self.board[row+1][col-1] != 0:
                            if self.board[row+1][col-1].color == color:
                                if self.board[row+2][col-2] != 0:
                                    if self.board[row+2][col-2].color == color:
                                        if self.board[row+3][col-3] != 0:
                                            if self.board[row+3][col-3].color == color:
                                                win = True


        #diagonaal (lefttop rightbottom)
        possible_start_locs = [[0,1,2,3],[0,1,2,3],[0,1,2,3]]
        for row in range(len(possible_start_locs)):
            for col in possible_start_locs[row]:
                if self.board[row][col] != 0:
                    if self.board[row][col].color == color:
                        if self.board[row+1][col+1] != 0:
                            if self.board[row+1][col+1].color == color:
                                if self.board[row+2][col+2] != 0:
                                    if self.board[row+2][col+2].color == color:
                                        if self.board[row+3][col+3] != 0:
                                            if self.board[row+3][col+3].color == color:
                                                win = True

        if win == True:
            pass
            #print(turn,'heeft gewonnen')

        return win
    
    def get_amound_of_possible_connect_fours(self):
 
        colors = [YELLOW,RED]

        possible_connect_fours = [0,0]
        
        for i,color in enumerate(colors):
            #horizontal
            possible_start_locs = [0,1,2,3]
            for row in self.board:
                for start_loc in possible_start_locs:
                    if row[start_loc] == 0 or row[start_loc].color == color:
                        if row[start_loc+1] == 0 or row[start_loc+1].color == color:
                            if row[start_loc+2] == 0 or row[start_loc+2].color == color:
                                if row[start_loc+3] == 0 or row[start_loc+3].color == color:
                                    possible_connect_fours[i] += 1

            #vertical
            possible_start_locs = [0,1,2]
            for col in range(len(self.board[0])):
                for start_loc in possible_start_locs:
                    if self.board[start_loc][col] == 0 or self.board[start_loc][col].color == color:
                        if self.board[start_loc+1][col] == 0 or self.board[start_loc+1][col].color == color:
                            if self.board[start_loc+2][col] == 0 or self.board[start_loc+2][col].color == color:
                                if self.board[start_loc+3][col] == 0 or self.board[start_loc+3][col].color == color:
                                    possible_connect_fours[i] += 1

            #diagonal (righttop leftbottom)
            possible_start_locs = [[3,4,5,6],[3,4,5,6],[3,4,5,6]]
            for row in range(len(possible_start_locs)):
                for col in possible_start_locs[row]:
                    if self.board[row][col] == 0 or self.board[row][col].color == color:
                        if self.board[row+1][col-1] == 0 or self.board[row+1][col-1].color == color:
                            if self.board[row+2][col-2] == 0 or self.board[row+2][col-2].color == color:
                                if self.board[row+3][col-3] == 0 or self.board[row+3][col-3].color == color:
                                    possible_connect_fours[i] += 1

            #diagonal (lefttop rightbottom)
            possible_start_locs = [[0,1,2,3],[0,1,2,3],[0,1,2,3]]
            for row in range(len(possible_start_locs)):
                for col in possible_start_locs[row]:
                    if self.board[row][col] == 0 or self.board[row][col].color == color:
                        if self.board[row+1][col+1] == 0 or self.board[row+1][col+1].color == color:
                            if self.board[row+2][col+2] == 0 or self.board[row+2][col+2].color == color:
                                if self.board[row+3][col+3] == 0 or self.board[row+3][col+3].color == color:
                                    possible_connect_fours[i] += 1

        #print(possible_connect_fours)
        return possible_connect_fours  # amound of possible connect fours [yellow,red]
        