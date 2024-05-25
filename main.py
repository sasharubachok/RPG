from pygame import *
from random import randint
init() 
 
info = display.Info()
screen_width,screen_height = info.current_w, info.current_h
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


class Sprite(sprite.Sprite):
    def __init__(self, img_name='tree.png', x=200, y=200, width=350, height=350, speed=0):
        super().__init__()
        self.image = image.load(img_name)
        self.image = transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def random_respawn(self):
        self.rect.x = randint(0, screen_width-50)
        self.rect.y = randint(0, screen_height-50)

    def collide(self, obj):
        return self.rect.colliderect(obj.rect)

class Hero(Sprite):
    def __init__(self,screen_width,screen_height):
        self.height = 50
        self.width = 50
        self.x = screen_width / 2 -  self.width 
        self.y = screen_height / 2 - self.height
        super().__init__( 'hero.png', self.x,self.y,self.width,self.height,10)
        self.money = 0
        self.health = 100
        self.armor = 100
        self.speed = 2

    def move(self):
        keys = key.get_pressed()
        if keys[K_d]:
            if self.rect.x < screen_width-50:

                self.rect.x += self.speed 
        if keys[K_a]:
            if self.rect.x > 50:
                self.rect.x -= self.speed
        if keys[K_w]:
            if self.rect.y > 50:
                self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y < screen_height-50:

                self.rect.y += self.speed

class Enemy(Sprite):
    def __init__(self,x_start,x_end, y_start ,y_end):
        self.height = 70
        self.width = 70
        self.x = x_start
        self.y = y_start
        super().__init__( 'enemy.png', self.x,self.y,self.width,self.height,10)
        self.x_start = x_start
        self.x_end = x_end 
        self.y_start = y_start 
        self.y_end = y_end
        self.speed = 2
        self.direction ='left'

    def move(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.rect.x > self.x_end:
            self.direction = 'left'
        if self.rect.x < self.x_start:
            self.direction = 'right'
        



window = display.set_mode((screen_width,screen_height)) 
background = transform.scale(image.load("bg.jpg"),(screen_width,screen_height)) 
game = True 
pause = True
clock = time.Clock() 
hero = Hero(screen_width,screen_height)
def stop_game():
    global game
    game = False
def start_game():
    hero.rect.x = 500
    hero.rect.y = 500
    
    global pause
    pause = False
btn1 = Button(600, 500, stop_game, 'exit.png')
btn2 = Button(600, 450, start_game, 'start.png')

coins = []
for i in range(0, 10):
    coin = Sprite('coins.png',randint(0, screen_width-50), randint(0, screen_height-50), 50, 50,0 )
    coins.append(coin)

enemys = [] 
enemy1 = Enemy(10, 400, 100, 100)
enemys.append(enemy1)
enemy1 = Enemy(300, 600, 300, 300)
enemys.append(enemy1)


while game: 
    for e in event.get():
        if pause:
            btn1.click(e) 
            btn2.click(e) 
        if e.type == QUIT :
            game = False 
        if e.type == KEYDOWN:
            if e.key  == K_ESCAPE: 
                pause = not pause

    if pause:
        window.blit(background, (0,0))
        btn1.reset(window)
        btn2.reset(window)

        display.update()
        clock.tick(60)
        continue

    
    window.blit(background, (0,0))

    for c in coins:
        c.reset(window)
        if c.collide(hero):
            c.random_respawn()

    hero.reset(window)
    hero.move()
    for i in enemys:
        if i.collide(hero):
            pause = True

        i.reset(window)
        i.move()
    display.update()
    clock.tick(60)