import math 
from .board import Board
lookup_table = [[3,4,5,7,5,4,3],
                [4,6,7,10,7,6,4],
                [5,7,12,13,12,7,5],
                [5,7,12,13,12,7,5],
                [4,6,7,10,7,6,4],
                [3,4,5,7,5,4,3]]

points_for_win = 9999


def minimax(original_board,turn):
    test_board = Board()
    test_board.board = original_board.board
    test_board.moves = original_board.moves
    possible_moves = test_board.get_possible_moves()
    print(possible_moves)


    move = find_best_move(possible_moves,1,turn,test_board)

    return move

def find_best_move(possible_moves,depth,turn,test_board):
    highest_score = -math.inf
    
    for r in possible_moves:
        test_board.make_move(r[0],turn)
        score = 0
        score += lookup_table[r[1]][r[0]]
        if test_board.win_check(turn):
            score += points_for_win
        print(score)
        if score > highest_score:
            best_move = r
            highest_score = score
        test_board.cancel_move()
            
    return best_move[0]
