import math 
from .board import Board
lookup_table = [[ 3 , 4 , 5  , 7  , 5  , 4 , 3 ],
                [ 4 , 6 , 8  , 10 , 8  , 6 , 4 ],
                [ 5 , 8 , 11 , 13 , 11 , 8 , 5 ],
                [ 5 , 8 , 11 , 13 , 11 , 8 , 5 ],
                [ 4 , 6 , 8  , 10 , 8  , 6 , 4 ],
                [ 3 , 4 , 5  , 7  , 5  , 4 , 3 ]]

points_for_win = 1000


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
        print(possible_moves)
        
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


def find_best_move2(original_board,turn):
    test_board = Board()
    test_board.board = original_board.board
    test_board.moves = original_board.moves
    bestScore = -math.inf
    bestMove = None
    for move in test_board.get_possible_moves():
        test_board.make_move(move[0],turn)
        if turn == 'red':
            turn = 'yellow'
            score = minimax2_red(test_board,False,2,0,turn)
        else:
            turn = 'red'
            score = minimax2_yellow(test_board,False,2,0,turn)
        test_board.cancel_move()
        print(f"Move: {move[0]} - Score: { score}")
        if (score > bestScore):
            bestScore = score
            bestMove = move
    
    
    print(bestMove[0],'\n')
    return bestMove[0]

def minimax2_red(test_board, max_turn, depth, current_depth, turn):
    
    if max_turn:
        if test_board.win_check(turn):
            return -points_for_win
        elif len(test_board.moves) == 42:
            return 0

        elif current_depth < depth:
            scores = []
            for move in test_board.get_possible_moves():
                test_board.make_move(move[0],turn)
                if turn == 'yellow':
                    turn = 'red'
                else:
                    turn = 'yellow'
                scores.append(minimax2_red(test_board,False,depth,current_depth + 1,turn))
                test_board.cancel_move()         
            
            return(max(scores))
        
        else:
            possible_connect_fours_yellow,possible_connect_fours_red = test_board.get_amound_of_possible_connect_fours()
            score = possible_connect_fours_red - possible_connect_fours_yellow
            return score
            
    else:
        if test_board.win_check(turn):
            print('hallo red')
            return points_for_win
        elif len(test_board.moves) == 42:
            return 0
        elif current_depth < depth:
            scores = []
            for move in test_board.get_possible_moves():
                test_board.make_move(move[0],turn)
                if turn == 'yellow':
                    turn = 'red'
                else:
                    turn = 'yellow'
                scores.append(minimax2_red(test_board,True,depth,current_depth + 1,turn))
                test_board.cancel_move()
            
            return(min(scores))
        
        else:
            possible_connect_fours_yellow,possible_connect_fours_red = test_board.get_amound_of_possible_connect_fours()

            score = possible_connect_fours_red - possible_connect_fours_yellow
            return score

def minimax2_yellow(test_board, max_turn, depth, current_depth, turn):
    
    if max_turn:
        if test_board.win_check('yellow'):
            return points_for_win
        elif test_board.win_check('red'):
            return -points_for_win
        elif len(test_board.moves) == 42:
            return 0
        elif current_depth < depth:
            scores = []
            for move in test_board.get_possible_moves():
                test_board.make_move(move[0],turn)
                if turn == 'yellow':
                    turn = 'red'
                else:
                    turn = 'yellow'
                scores.append(minimax2_yellow(test_board,False,depth,current_depth + 1,turn))
                test_board.cancel_move()          
            
            return(min(scores))
        
        else:
            possible_connect_fours_yellow,possible_connect_fours_red = test_board.get_amound_of_possible_connect_fours()
            score = possible_connect_fours_yellow - possible_connect_fours_red
            return score
            
    else:
        if test_board.win_check('yellow'):
            return points_for_win
        elif test_board.win_check('red'):
            return -points_for_win
        elif len(test_board.moves) == 42:
            return 0
        elif current_depth < depth:
            scores = []
            for move in test_board.get_possible_moves():
                test_board.make_move(move[0],turn)
                if turn == 'yellow':
                    turn = 'red'
                else:
                    turn = 'yellow'
                scores.append(minimax2_yellow(test_board,True,depth,current_depth + 1,turn))
                test_board.cancel_move()
            
            return(max(scores))
        
        else:
            possible_connect_fours_yellow,possible_connect_fours_red = test_board.get_amound_of_possible_connect_fours()

            score = possible_connect_fours_yellow - possible_connect_fours_red
            return score


