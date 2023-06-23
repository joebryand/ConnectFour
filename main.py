import pygame
from connect_four.constants import WIDTH, HEIGHT, PLAYER_NAME, PLAYER_AGE, SAVE_GAME, SEARCH_DEPTH
from connect_four.game import Game
from connect_four.minimax import find_best_move
from saved_data.statistics import Statistics

pygame.init()

FPS = 30

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Connect Four')

game = Game(WIN)

points = {"red" : 0, "yellow" : 0}

stats = Statistics(PLAYER_NAME, PLAYER_AGE)


def game_end_check(): # Function for checking if the game should end. 
    if game.winner == 'yellow':
        points["yellow"] += 1
        print(points)
        game.gamestate = "game_over"
        return True

    elif game.winner == 'red':
        points["red"] += 1
        print(points)
        game.gamestate = "game_over"
        return True

    
    elif len(game.game_board.moves) == 42:
        print(points)
        game.gamestate = "game_over"
        return True

    return False

def button_check(abs_pos): # Function for checking if the mouse position is on any in game button, and performing the action of that button. 
    for button in game.window.in_game_buttons: 
        action = button.check_if_clicked(abs_pos)
        if action != 0:
            break

    if action == "CANCEL MOVE": # if button "CANCEL MOVE" is clicked the last 2 moves get deleted so that it is the players turn again. 
        if game.game_board.cancel_move():
            game.change_turn()
        if game.game_board.cancel_move():
            game.change_turn()
        game.possible_moves = game.get_possible_moves()

    elif action == "AI MOVE": # if button "AI MOVE" is clicked the AI makes the best move using minimax algorithm
        if game.make_move(find_best_move(game.game_board,game.turn)):
            if game.win_check():
                game.winner = game.turn
            game.change_turn()
            game.possible_moves = game.get_possible_moves()

    elif action == "RESET": # if button "RESET" is clicked the game object is reset 
        game.reset()

    elif action == "HIGHLIGHT": # if button "HIGHLIGHT" is clicked the highlighted possible moves get turned on or off
        game.enable_show_possible_moves = not game.enable_show_possible_moves


def main(): # main program for handeling UI
    run = True # as long as run is True the application is running
    clock = pygame.time.Clock() # needed for checking FPS
    while run: # loop of the application
        clock.tick(FPS)

        
        if game.turn == 'red': #If AI's turn
            if game.make_move(find_best_move(game.game_board,game.turn)): # make move using Minimax to find best move
                if game.win_check():
                    game.winner = game.turn 
                game.change_turn()
                game.possible_moves = game.get_possible_moves()

        for event in pygame.event.get(): # pygames event loop to get all input of the window
            abs_pos = 0
            if event.type == pygame.QUIT: # makes the red X button in the top right of the window work
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: # if any button on the mouse gets clicked the position of the mouse is saved and used for UI
                abs_pos = pygame.mouse.get_pos()
                
                if game.gamestate == "in_game": # if the game is still ongoing
                    if game.turn == 'yellow': # if players turn
                        if abs_pos[0] >= 590: #position of the click is somewhere right from the game board.
                            button_check(abs_pos) # check if clicked on any button
                        
                        elif abs_pos[0] > 90: #position of 'click' somewhere on the game board.
                            col = int((abs_pos[0]-game.window.board_rect[0]) // 70) # calculate the colomn which is clicked.
                            if game.make_move(col): # try to make the move with the calculated column
                                if game.win_check(): # check for win after played move
                                    game.winner = game.turn 
                                game.change_turn() # changes the turn to other player
                                game.possible_moves = game.get_possible_moves() # find new possible moves

                elif game.gamestate == "game_over": # if the game has finished
                    for button in game.window.game_end_buttons:  #check if clicked on any button
                        action = button.check_if_clicked(abs_pos)
                        if action != 0: # if not clicked on any buttons: break
                            break

                    if action == "NEW GAME": #if clicked on 'NEW GAME' button  
                        game.reset() # reset game

        game.update() #update game every loop

        if game.gamestate == "in_game": # if the game is still ongoing
            if game_end_check(): # check if the game should end
                if SAVE_GAME: # if the game finishes save the position if SAVE_GAME is True
                    new_game_moves = []                 
                    for move in game.game_board.moves:   
                        new_game_moves.append(move[1])  
                    with open("ConnectFour\saved_data\saved_games.txt", "a") as saved_games:
                        saved_games.write(f"{PLAYER_NAME},{PLAYER_AGE},{SEARCH_DEPTH},{'draw' if game.winner == 0 else game.winner},{new_game_moves}\n")
                    
    pygame.quit() # if run is not true anymore close the game window.

main()