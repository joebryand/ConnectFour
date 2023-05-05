import pygame
from connect_four.constants import WIDTH, HEIGHT
from connect_four.game import Game
from connect_four.minimax import find_best_move

pygame.init()

FPS = 30

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Connect Four')

game = Game(WIN)

points = {"red" : 0, "yellow" : 0}

def main():
    run = True
    clock = pygame.time.Clock()
    print(game.game_board.get_amound_of_possible_connect_fours())
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
                        if game.make_move(find_best_move(game.game_board,game.turn)):
                            if game.win_check():
                                game.winner = game.turn
                            game.change_turn()
                            game.possible_moves = game.get_possible_moves()

                    elif abs_pos[0] >= 590:
                        for button in game.window.in_game_buttons: 
                            action = button.check_if_clicked(abs_pos)
                            if action != 0:
                                break
                        #print(action)

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
                    print(action)

                    if action == "NEW GAME":
                        game.reset()


        winner = game.update()
        if game.gamestate == "dynamic":
            if winner == 'yellow':
                points["yellow"] += 1
                print(points)
                game.gamestate = "static"
            elif winner == 'red':
                points["red"] += 1
                print(points)
                game.gamestate = "static"
            
            elif len(game.game_board.moves) == 42:
                print(points)
                game.gamestate = "static"
        

    pygame.quit()

main()