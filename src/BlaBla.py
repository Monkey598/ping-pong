import pygame
from time import time
from random import randint
pygame.init()

lvl_number_player = 1
live_number_player = 5

speed_ball_x = 10
speed_ball_y = 8
racket_x = 200
racket_y = 299

no_game = False
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

class Area():
   def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
   def color(self, new_color):
       self.fill_color = new_color
   def fill(self):
       pygame.draw.rect(mw, self.fill_color, self.rect)
   def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Pin(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self, shift_x=0, shift_y=0):
        mw.blit(self.image, (self.rect.x, self.rect.y))

ball = Pin('image/планета.png', 160, 200, 50, 50)
derevashka = Pin('image/платформа.png', racket_x, racket_y, 100, 30)

start_x = 5
start_y = 5
count = 9
monsters = []
livs = []

z = 10
for o in range(5):
    lives = Pin('image/сердца.png', z, 420, 50, 50)
    livs.append(lives)
    z+=55
    

for i in range(3):
    y = start_y + (55 * i)
    x = start_x + (27.5 * i)
    for j in range (count):
        d = Pin('image/гавнюки.png', x, y, 50, 50)
        monsters.append(d)
        x = x + 55
    count = count - 1

    
while not no_game:
    for i in livs:
        i.fill()
        i.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            no_game = True
    
    ball.fill()
    derevashka.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            no_game == True
    for n in monsters:
        n.draw()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and derevashka.rect.x < 425 or keys[pygame.K_RIGHT] and derevashka.rect.x < 425:
        derevashka.rect.x += 10
    if keys[pygame.K_a] and derevashka.rect.x > 0 or keys[pygame.K_LEFT] and derevashka.rect.x > 0:
        derevashka.rect.x -= 10

    if ball.rect.y <= 400:
        if ball.colliderect(derevashka.rect):
            speed_ball_y *= -1
        elif ball.rect.x + speed_ball_x >= 475 or ball.rect.x + speed_ball_x <= 0:
            speed_ball_x = -speed_ball_x
        elif ball.rect.y + speed_ball_y <= 0:
            speed_ball_y = -speed_ball_y
        ball.rect.x += speed_ball_x
        ball.rect.y += speed_ball_y
    else:
        if live_number_player <= 1:
            livs[0].fill()
            no_game = True
        else:
            livs[live_number_player -1].fill()
            livs.remove(livs[live_number_player -1])
            live_number_player -= 1
            ball.rect.x = derevashka.rect.x
            ball.rect.y = 200
    
    if lvl_number_player == 10:
        no_game = True

    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            m.fill()
            monsters.remove(m)
            
            speed_ball_y *= -1
    if len(monsters) == 0:
        ball.rect.x, ball.rect.y = 160, 200
        i = 0
        j = 0
        count = 9
        for i in range(3):
            y = start_y + (55 * i)
            x = start_x + (27.5 * i)
            for j in range (count):
                d = Pin('image/гавнюки.png', x, y, 50, 50)
                monsters.append(d)
                x = x + 55
            count = count - 1
        lvl_number_player += 1
        live_number_player = 5

    derevashka.draw()
    ball.draw()

    pygame.display.update()

    clock.tick(30)  