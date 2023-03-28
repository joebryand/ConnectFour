import math 
from .stone import Stone
from .constants import YELLOW, RED
lookup_table = [[3,4,5,7,5,4,3],
                [4,6,7,10,7,6,4],
                [5,7,12,13,12,7,5],
                [5,7,12,13,12,7,5],
                [4,6,7,10,7,6,4],
                [3,4,5,7,5,4,3]]

points_for_win = 9999


def minimax(game):
    start_board = game.board.copy()
    possible_moves = game.get_possible_moves(start_board)
    print(possible_moves)


    move = find_best_move(possible_moves,1,game,start_board)

    return move

def get_temp_board(col,board,turn): 
    if -1 < col < 7:
        for i in range(len(board)):
            i = len(board)-1-i
            if board[i][col] == 0:
                if turn == 'red':
                    board[i][col] = Stone(RED)    
                elif turn == 'yellow':
                    board[i][col] = Stone(YELLOW)
                break
    return board


def find_best_move(possible_moves,depth,game,start_board):
    highest_score = -math.inf
    
    for r in possible_moves:
        #temp_board = get_temp_board(r[0],start_board,game.turn)
        score = 0
        score += lookup_table[r[1]][r[0]]
        #if game.win_check(temp_board):
        #    score += points_for_win
        print(score)
        if score > highest_score:
            best_move = r
            highest_score = score
            
    return best_move[0]
