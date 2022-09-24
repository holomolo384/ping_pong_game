from pygame import *

class GameSprite(sprite.Sprite):
def __init__(self, player_image, player_x, player_y, player_speed, width, height):
	super().__init__()
	self. image = transform.scale(image.load(player_image,(width, heigh)
	self.speed = player_speed
	self.rect = self.image.get_rect()										 
	self.rect.x = player_x
	self.rect.y = player_y
def reset(self):
	def update_r(self):
		keys = key.get_pressed()
		if keys[K_UP] and self.rect.y > 5:
			self.rect.y -= self.speed								 
		if keys[K_DOWN] and self.rect.y < 420:									 
			self.rect.y += self.speed											 
	def update_l(self):
		keys = key.get_pressed()
		if keys{
											
                                                 
				
									 

#картинки 
											 
ball_img = "ball.png"
left_racket = "left_racket.png"
right_racket = "right_racket.png"

#ширина і висота
width = 600
height = 500

#головне вікно
background = (100, 255, 100)
window = display.set_mode((width, height))
window.fill(background)

#годинник для оновлення екрану
clock = time.CLock()
#кількість кадрів в секунду
FPS = 60
#прапорці для стану гри
game = True
finish = False

#ігровий цикл
while game:
    #перевірка подій
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)

