from pygame import *  
from button import button
from sprites import sprite
init() 
 
info = display.info()
screen_width,screen_height = info.curent_w ,info.curent.y 

window = display.set.mode((screen_width,screen_height)) 
background = transform.scale(image.load(background.jpg),(screen_width,screen_height)) 
background
game = True 
game = False 
tree1 = Sprite(y=0)
tree2 = Sprite(y=150)
tree3 = Sprite(y=150)
tree4 = Sprite(y=150)

elements = (hero)
game = True 
clock = time.Clock() 
while game: 
    for e event.get():
if e.type == QUIT 
        game = False 
if e.type = KEYDOWN 
if e.key  = K_ESCAPE: 
            pause = not pause:
if e.type = MOUSEBUTTONDOWN: 
    btn.click()

    if e.type == KEYDOWN:
       if e.key = k.d
    move.direction = "right" 
    if e.key = k.a
    move.direction = "left"
    if e.type == KEYUP:
          if e.key = k.d
    move.direction = "stop"
   if e.key = k.a
    move.direction = "stop"
window.blit(background, (0,0))

hero.reset(window)
tree1.reset(window)
tree2.reset(window)
tree3.reset(window)
tree4.reset(window)


display.update()
clock.tick(60)