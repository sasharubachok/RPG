from pygame import *

class Button:
    def __init__(self,x,y, onclick_function, img_name):
        self.width = 100
        self.height = 50
        self.onclick_function = onclick_function

        self.image = image.load(img_name)
        self.image = transform.scale(self.image, ( self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, window): 
        window.blit(self.image, (self.rect.x, self.rect.y))
   
    def click(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.onclick_function()

