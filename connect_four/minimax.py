# In this python file the AI is written. for the AI is the minimax algorithm used. To write this code Yiğit PIRILDAK his blog was used: 
# https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f

# The minimax algorithm consist of two functions
#   -   The first function (find_best_move) is used to call te AI in the main python script. here everyting needed for the algorithm is 
#       collected and the first loop of the algorithm is called. Whitin the function the other function is called. The function returns 
#       the column of the best move.
#   -   The second function (minimax) is the main part of the algoritm. It consist of a max_turn and a not max_turn which means who's 
#       turn it is. if the AI is at turn, max_turn is True because we want to maximise the result. if the opponent is at turn, max_turn 
#       is False because we want to minimize the result. each consist of the same three parts further explained in the code.

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
    # getting all thing ready for the algorithm
    test_board = Board()
    test_board.board = original_board.board
    test_board.moves = original_board.moves
    bestScore = -math.inf
    bestMove = None

    # start first loop of the algorithm
    for move in test_board.get_possible_moves():
        test_board.make_move(move[0],turn)

        score = minimax(test_board,False,3,turn)

        test_board.cancel_move()
        print(f"Move: {move[0]} - Score: {score}")
        if (score > bestScore):
            bestScore = score
            bestMove = move

    # print and return the best move fount by the algorithm
    print(bestMove[0],'\n')
    return bestMove[0]

def minimax(test_board, max_turn, current_depth, turn):
    
    if max_turn:
        # check for game ending positions (win, lose or draw), because the last move is made by the opponent it could only have lost or drew on this move, so we dont look for a win.
        if test_board.win_check(turn):
            return -points_for_win
        elif len(test_board.moves) == 42:
            return 0
        
        # if the max dept is not reached yet we go to the next dept. for the next dept we change the turn. 
        elif current_depth != 0:
            scores = []
            if turn == 'yellow':
                turn = 'red'
            else:
                turn = 'yellow'
            for move in test_board.get_possible_moves():
                
                test_board.make_move(move[0],turn)
                scores.append(minimax(test_board,False,current_depth - 1,turn))
                test_board.cancel_move()
            
            return(max(scores))
        
         # if there is no game ending position and the max dept has been reached, the position will be given a value and returned to the previous dept.
        else:
            possible_connect_fours_yellow,possible_connect_fours_red = test_board.get_amound_of_possible_connect_fours()
            if turn == "red":
                score = possible_connect_fours_yellow - possible_connect_fours_red
            elif turn == "yellow":
                score = possible_connect_fours_red - possible_connect_fours_yellow
            return score
            
    else:
        # check for game ending positions (win, lose or draw), because the last move is made by the AI it could only have won or drew on this move, so we dont look for a lose. 
        if test_board.win_check(turn):
            return points_for_win
        elif len(test_board.moves) == 42:
            return 0
        
        # if the max dept is not reached yet we go to the next dept. for the next dept we change the turn. 
        elif current_depth != 0:
            scores = []
            if turn == 'yellow':
                turn = 'red'
            else:
                turn = 'yellow'
            for move in test_board.get_possible_moves(): 
                test_board.make_move(move[0],turn)
                scores.append(minimax(test_board,True,current_depth - 1,turn))
                test_board.cancel_move()
            
            return(min(scores))
        
        # if there is no game ending position and the max dept has been reached, the position will be given a value and returned to the previous dept.
        else:
            possible_connect_fours_yellow,possible_connect_fours_red = test_board.get_amound_of_possible_connect_fours()
            if turn == "red":
                score = possible_connect_fours_red - possible_connect_fours_yellow
            elif turn == "yellow":
                score = possible_connect_fours_yellow - possible_connect_fours_red
            return score
