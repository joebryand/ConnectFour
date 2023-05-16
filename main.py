import pygame
from connect_four.constants import WIDTH, HEIGHT
from connect_four.game import Game
from connect_four.minimax import find_best_move

pygame.init()

FPS = 200000

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Connect Four')

game = Game(WIN)

points = {"red" : 0, "yellow" : 0}

def main():
    run = True

    go = False
    startup = True
    position = 0
    positions = [[1,5],[3,3],[0,1],[2,3],[0,0],[3,4],[6,1],[6,5],[0,6],[5,0]]
    test_game = [0,0]
    first_AI =  ["possible_connect_fours", "connected_pieces", "random", "combination"]
    second_AI = ["possible_connect_fours", "connected_pieces", "random", "combination"]

    scores = [[],[],[],[]]

    clock = pygame.time.Clock()
    print(game.game_board.get_number_of_possible_connect_fours())
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            abs_pos = 0
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                abs_pos = pygame.mouse.get_pos()
                if game.gamestate == "dynamic":

                    if abs_pos[0] <= 90:
                        go = not go

                    elif abs_pos[0] >= 590:
                        for button in game.window.in_game_buttons: 
                            action = button.check_if_clicked(abs_pos)
                            if action != 0:
                                break

                        if action == "CANCEL MOVE":
                            if game.game_board.cancel_move():
                                game.change_turn()
                            game.possible_moves = game.get_possible_moves()

                        elif action == "AI MOVE":
                            if game.make_move(find_best_move(game.game_board,game.turn)):
                                if game.win_check():
                                    game.winner = game.turn
                                game.change_turn()
                                game.possible_moves = game.get_possible_moves()

                        elif action == "RESET":
                            game.reset()

                        elif action == "HIGHLIGHT":
                            game.enable_show_possible_moves = not game.enable_show_possible_moves

                    col = int((abs_pos[0]-game.window.board_rect[0]) // 70)
                    if -1 < col < 7:
                        if game.make_move(col):
                            if game.win_check():
                                game.winner = game.turn
                            game.change_turn()
                            game.possible_moves = game.get_possible_moves()

                elif game.gamestate == "static":
                    for button in game.window.game_end_buttons: 
                        action = button.check_if_clicked(abs_pos)
                        if action != 0:
                            break

                    if action == "NEW GAME":
                        game.reset()
                
        if go and game.gamestate == "dynamic":
            if game.turn == "yellow":
                if game.make_move(find_best_move(game.game_board,game.turn,first_AI[test_game[0]])):
                    if game.win_check():
                        game.winner = game.turn
                    game.change_turn()
                    game.possible_moves = game.get_possible_moves()
            
            elif game.turn == "red":
                if game.make_move(find_best_move(game.game_board,game.turn,second_AI[test_game[1]])):
                    if game.win_check():
                        game.winner = game.turn
                    game.change_turn()
                    game.possible_moves = game.get_possible_moves()
        
        if startup:
            for move in positions[position]:
                game.make_move(move)
                game.change_turn()
            game.possible_moves = game.get_possible_moves()
            startup = False

        winner = game.update()
        if game.gamestate == "dynamic":
            if winner == 'yellow':
                points["yellow"] += 1
                print(points)
                #game.gamestate = "static"

                if position < len(positions)-1:
                    startup = True
                    position += 1
                    game.reset()
                
                else:
                    startup = True
                    position = 0
                    scores[test_game[1]].append((points["red"],points["yellow"]))
                    points["red"] = 0
                    points["yellow"] = 0
                    if test_game[0] < 3:
                        test_game[0] += 1
                        game.reset()
                    elif test_game[1] < 3:
                        test_game[1] += 1
                        test_game[0] = 0
                        game.reset()
                    else:
                        game.gamestate = "static"
                    print(scores)
                
            elif winner == 'red':
                points["red"] += 1
                print(points)
                #game.gamestate = "static"

                if position < len(positions)-1:
                    startup = True
                    position += 1
                    game.reset()

                else:
                    startup = True
                    position = 0
                    scores[test_game[1]].append((points["red"],points["yellow"]))
                    points["red"] = 0
                    points["yellow"] = 0
                    if test_game[0] < 3:
                        test_game[0] += 1
                        game.reset()
                    elif test_game[1] < 3:
                        test_game[1] += 1
                        test_game[0] = 0
                        game.reset()
                    else:
                        game.gamestate = "static"
                    print(scores)
            
            elif len(game.game_board.moves) == 42:
                print(points)
                #game.gamestate = "static"

                if position < len(positions)-1:
                    startup = True
                    position += 1
                    game.reset()

                else:
                    startup = True
                    position = 0
                    scores[test_game[1]].append((points["red"],points["yellow"]))
                    points["red"] = 0
                    points["yellow"] = 0
                    if test_game[0] < 3:
                        test_game[0] += 1
                        game.reset()
                    elif test_game[1] < 3:
                        test_game[1] += 1
                        test_game[0] = 0
                        game.reset()
                    else:
                        game.gamestate = "static"
                    print(scores)
                    
        

    pygame.quit()

main()


#[[(2, 2), (1, 3), (1, 3), (3, 1)], [(1, 3), (1, 3), (0, 4), (3, 1)], [(1, 3), (0, 3), (2, 2), (2, 2)], [(1, 3), (1, 3), (0, 4), (1, 3)]]
#[[(2, 2), (1, 3), (0, 3), (3, 1)], [(1, 3), (1, 3), (1, 3), (3, 1)], [(1, 3), (1, 2), (1, 2), (3, 1)], [(2, 2), (1, 3), (0, 4), (1, 3)]]

#(red, yellow)


# depth 0
#[[(1, 3),  (4, 6),  (6, 4), (1, 9)], 
# [(1, 9),  (1, 9),  (1, 9), (1, 9)], 
# [(0, 10), (0, 10), (2, 8), (0, 10)], 
# [(6, 3),  (2, 8),  (9, 1), (0, 10)]]

# depth 1
#[[(2, 8), (2, 8), (7, 3),  (1, 9)], 
# [(2, 8), (2, 8), (5, 4),  (0, 10)], 
# [(1, 9), (1, 8), (6, 3),  (0, 10)], 
# [(7, 3), (8, 2), (10, 0), (5, 4)]]

# depth 2
#[[(2, 6), (6, 4), (7, 3), (0, 7)], 
# [(4, 6), (0, 9), (7, 3), (0, 10)], 
# [(1, 9), (2, 8), (8, 2), (1, 9)], 
# [(3, 6), (6, 3), (8, 2), (3, 7)]]

# depth 3
#[[(3, 7), (3, 7),  (5, 4),  (1, 9)], 
# [(3, 7), (3, 7),  (5, 5),  (1, 9)], 
# [(2, 8), (3, 6),  (5, 4),  (0, 9)], 
# [(9, 1), (10, 0), (10, 0), (2, 7)]]

# depth 4
#[[(2, 4),  (9, 1),  (10, 0), (5, 5)], 
# [(0, 10), (4, 6),  (2, 5),  (1, 9)], 
# [(1, 9),  (2, 7),  (6, 4),  (2, 8)], 
# [(4, 3),  (10, 0), (9, 1),  (4, 6)]]

# depth 5
#[[(6, 3),  (7, 2),  (7, 3), (5, 5)], 
# [(6, 3),  (7, 2),  (7, 1), (6, 4)], 
# [(1, 8),  (4, 3),  (4, 5), (1, 9)], 
# [(10, 0), (10, 0), (9, 1), (1, 4)]]