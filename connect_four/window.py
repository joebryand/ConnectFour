import pygame
from .constants import WIDTH,HEIGHT,STONE_SIZE,GLOW_IMAGE, SEARCH_DEPTH,PLAYER_NAME
from .UI import Button, Text

class Window:
    def __init__(self):
        self.board_rect = (90,0,490,420)
        self.side_bar_rect = [(0,0,self.board_rect[0]-4,HEIGHT),((self.board_rect[0]+self.board_rect[2]+4,0,WIDTH-(self.board_rect[0]+self.board_rect[2])-4,HEIGHT))]
        self.cel_width = self.board_rect[2]/7

        self.in_game_buttons = [Button(590,340,160,40,"RESET"),Button(590,20,160,40,"CANCEL MOVE"),Button(590,80,160,40,"HIGHLIGHT"),Button(590,140,160,40,"AI MOVE")]
        self.in_game_text = [Text(0,HEIGHT-75,90,20,(0,0,0),12,f'Player name:'),Text(0,HEIGHT-60,90,20,(0,0,0),12,f'{PLAYER_NAME}'),Text(0,HEIGHT-30,90,20,(0,0,0),12,f'AI level: {SEARCH_DEPTH}')]
        self.game_end_buttons = [Button(240,170,190,80,"NEW GAME")]

    def draw(self,win,board):
        self.draw_board(win)
        self.draw_side_bar(win)  
        self.draw_stones(win,board)
        for button in self.in_game_buttons: button.draw(win) 
        for text in self.in_game_text: text.draw(win) 

    def draw_board(self,win):
        pygame.draw.rect(win,(30,30,120),self.board_rect)
        for col in range(7):
            for row in range(6):
                pygame.draw.circle(win,(0,0,0),(self.board_rect[0]+self.cel_width/2+self.cel_width*col,self.board_rect[1]+self.cel_width/2+self.cel_width*row),STONE_SIZE//2)

    def draw_side_bar(self,win):
        pygame.draw.rect(win,(120,200,210),(self.side_bar_rect[0]))
        pygame.draw.rect(win,(120,200,210),(self.side_bar_rect[1]))
    
    def draw_stones(self,win,board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                content = board[row][col]
                if content != 0:
                    content.draw(win,(self.board_rect[0]+col*self.cel_width+self.cel_width/2,self.board_rect[1]+row*self.cel_width+self.cel_width/2))

    def draw_possible_moves(self,win,possible_moves):
        for cel in possible_moves:
            col,row = cel
            win.blit(GLOW_IMAGE,(self.board_rect[0]+col*self.cel_width,self.board_rect[1]+row*self.cel_width))

    def draw_game_end_screen(self,win):
        for button in self.game_end_buttons: button.draw(win) 