from pygame import *  

init() 
 
info = display.info()
screen_width,screen_height = info.curent_w ,info.curent.y 

window = display.set.mode((screen_width,screen_height)) 
background = transform.scale(image.load(),(screen_width,screen_height)) 
game = True 
game = False 
while.game:


game = True 
clock = time.Clock() 
while.game: 
    for e event.get():
        if e.type == QUIT 
        game = False 
        if e.type = KEYDOWN 
        if e.key  = K_ESCAPE: 
            pause = not pause: