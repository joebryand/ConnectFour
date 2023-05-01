import math 
from .board import Board
lookup_table = [[ 3 , 4 , 5  , 7  , 5  , 4 , 3 ],
                [ 4 , 6 , 8  , 10 , 8  , 6 , 4 ],
                [ 5 , 8 , 11 , 13 , 11 , 8 , 5 ],
                [ 5 , 8 , 11 , 13 , 11 , 8 , 5 ],
                [ 4 , 6 , 8  , 10 , 8  , 6 , 4 ],
                [ 3 , 4 , 5  , 7  , 5  , 4 , 3 ]]

points_for_win = 1000

def find_best_move(original_board,turn):
    test_board = Board()
    test_board.board = original_board.board
    test_board.moves = original_board.moves
    bestScore = -math.inf
    bestMove = None
    for move in test_board.get_possible_moves():
        test_board.make_move(move[0],turn)

        score = minimax(test_board,False,0,0,turn)

        test_board.cancel_move()
        print(f"Move: {move[0]} - Score: {score}")
        if (score > bestScore):
            bestScore = score
            bestMove = move
    
    print(bestMove[0],'\n')
    return bestMove[0]

def minimax(test_board, max_turn, depth, current_depth, turn):
    
    if max_turn:
        if test_board.win_check(turn):
            return -points_for_win
        elif len(test_board.moves) == 42:
            return 0

        elif current_depth < depth:
            scores = []
            if turn == 'yellow':
                turn = 'red'
            else:
                turn = 'yellow'
            for move in test_board.get_possible_moves():
                
                test_board.make_move(move[0],turn)
                scores.append(minimax(test_board,False,depth,current_depth + 1,turn))
                test_board.cancel_move()
            
            return(max(scores))
        
        else:
            possible_connect_fours_yellow,possible_connect_fours_red = test_board.get_amound_of_possible_connect_fours()
            if turn == "red":
                score = possible_connect_fours_yellow - possible_connect_fours_red
            elif turn == "yellow":
                score = possible_connect_fours_red - possible_connect_fours_yellow
            return score
            
    else:
        if test_board.win_check(turn):
            return points_for_win
        elif len(test_board.moves) == 42:
            return 0
        elif current_depth < depth:
            scores = []
            if turn == 'yellow':
                turn = 'red'
            else:
                turn = 'yellow'
            for move in test_board.get_possible_moves(): 
                test_board.make_move(move[0],turn)
                scores.append(minimax(test_board,True,depth,current_depth + 1,turn))
                test_board.cancel_move()
            
            return(min(scores))
        
        else:
            possible_connect_fours_yellow,possible_connect_fours_red = test_board.get_amound_of_possible_connect_fours()
            if turn == "red":
                score = possible_connect_fours_red - possible_connect_fours_yellow
            elif turn == "yellow":
                score = possible_connect_fours_yellow - possible_connect_fours_red
            return score
