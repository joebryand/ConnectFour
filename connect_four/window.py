import pygame
from .constants import WIDTH,HEIGHT,STONE_SIZE,RED,YELLOW,GLOW

class Window:
    def __init__(self):
        self.board_rect = (100,0,490,420)
        self.side_bar_rect = [(0,0,self.board_rect[0]-4,HEIGHT),((self.board_rect[0]+self.board_rect[2]+4,0,WIDTH-(self.board_rect[0]+self.board_rect[2])-4,HEIGHT))]
        self.cel_width = self.board_rect[2]/7

    def draw(self,win,board):
        self.draw_board(win)
        self.draw_side_bar(win)  
        self.draw_stones(win,board)      

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
            win.blit(GLOW,(self.board_rect[0]+col*self.cel_width,self.board_rect[1]+row*self.cel_width))