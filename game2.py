import pgzrun
import random

HEIGHT = 500
WIDTH = 800

class Hero(Actor):
    def move(self):
        if keyboard.left:
            self.x -= 10
            self.angle = 10
        elif keyboard.right:
            self.x += 10
            self.angle = -10
        elif keyboard.up:
            self.y -= 10
        elif keyboard.down:
            self.y += 10     
        else :
            self.angle = 0       

    def warp(self):
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y > HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = HEIGHT                        

class Ship(Actor):
    def track (self , player , speed=1):
        if player.x > self.x :
            self.x += speed 
        elif player.x < self.x :
            self.x -= speed
        if player.y > self.y:
            self.y += speed
        elif player.y < self.y :
            self.y -= speed



p = Hero('ironman',(100, 100))
b = Rect((300, 100), (32,32)) # position size
s = Ship('ship', (1000,1000))
e = Ship('alien',(300,500))

def draw():
    screen.fill('black')
    p.draw()
    p.warp()
    s.draw()
    e.draw()
    screen.draw.filled_rect(b, 'red')
    
def update():
    p.move()
    s.track(p,4)
    e.track(p,3)

pgzrun.go()