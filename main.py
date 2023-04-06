import pygame
from connect_four.constants import WIDTH, HEIGHT
from connect_four.game import Game
from connect_four.minimax import minimax

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Connect Four')

game = Game(WIN)

points = [0,0]

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            abs_pos = 0
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                abs_pos = pygame.mouse.get_pos()
                col = int((abs_pos[0]-game.window.board_rect[0]) // 70)
                if abs_pos[0] <= 100:
                    game.board = game.make_move(minimax(game))
                    if game.win_check():
                        game.winner = game.turn
                    game.change_turn()
                    game.possible_moves = game.get_possible_moves()
                if -1 < col < 7:
                    game.board = game.make_move(col)
                    if game.win_check():
                        game.winner = game.turn
                    game.change_turn()
                    game.possible_moves = game.get_possible_moves()
        
        

        WIN.fill((0,0,10))
        winner = game.update()

        if winner == 'red':
            points[0] += 1
            print(points)
            game.reset()
        elif winner == 'yellow':
            points[1] += 1
            print(points)
            game.reset()

    pygame.quit()

main()