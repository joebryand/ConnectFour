import math 
from .board import Board
lookup_table = [[ 3 , 4 , 5  , 7  , 5  , 4 , 3 ],
                [ 4 , 6 , 8  , 10 , 8  , 6 , 4 ],
                [ 5 , 8 , 11 , 13 , 11 , 8 , 5 ],
                [ 5 , 8 , 11 , 13 , 11 , 8 , 5 ],
                [ 4 , 6 , 8  , 10 , 8  , 6 , 4 ],
                [ 3 , 4 , 5  , 7  , 5  , 4 , 3 ]]

points_for_win = 9999


def minimax(original_board,turn):
    test_board = Board()
    test_board.board = original_board.board
    test_board.moves = original_board.moves

    move = find_best_move(1,turn,test_board)

    return move

def find_best_move(depth,turn,test_board):
    highest_score = -math.inf
    for layer in range(depth):
        possible_moves = test_board.get_possible_moves()
        for i in possible_moves:
            test_board.make_move(i[0],turn)
            score = 0
            score += lookup_table[i[1]][i[0]]
            if test_board.win_check(turn):
                score += points_for_win
            print(score)
            if score > highest_score:
                best_move = i
                highest_score = score
            test_board.cancel_move()
            
    return best_move[0]
