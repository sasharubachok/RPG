from pygame import *

class Button:
    def __init__(self, window, screen_width, screen_height,onclick_function):
        self.window = window
        self.width = 100
        self.height = 50
        self.x = screen_width/2
        self.y = screen_height/2
        self.onclick_function=onclick_function
        font.init()
        self.font1 = font.Font(None, 20)
        self.rect = rect.Rect( self.x,  self.y,  self.width,  self.height)

    def reset(self): 
        draw.rect(self.window, (255,255,255),self.rect )
        self.window.blit(self.font1.render('Exit', True, (0,0,0)),(self.x,  self.y,))

    def click(self):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.colidepoint(event.pos): 
                self.onclick_function()
