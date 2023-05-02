import pygame

class Button:
    def __init__(self, x, y, width, height, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
        
        self.border = 2
        self.font = pygame.font.Font('freesansbold.ttf', 18)


    def check_if_clicked(self, pos):
        x_pos,y_pos = pos
        if x_pos > self.x and x_pos < self.x + self.width and y_pos > self.y and y_pos < self.y + self.height:
            return self.action
        else:
            return 0

    def draw(self, win):
        pygame.draw.rect(win,(128,128,128),(self.x,self.y,self.width, self.height))
        pygame.draw.rect(win,(200,200,200),(self.x+self.border,self.y+self.border,self.width-self.border*2, self.height-self.border*2))
        text = self.font.render(self.action, True,(0,0,0))
        textRect = text.get_rect()
        textRect.center = ((self.x)+(self.width)//2,(self.y)+(self.height)//2)
        win.blit(text, textRect)