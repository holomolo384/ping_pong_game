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
		if keys[K_w] and self.rect.y > 5:
			self.rect.y -= self.speed
		if keys[k_a] and self.rect.y < 420:
			self.rect.y += self.speed
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
		
ball = GameSprite("ball.png", 200,200,4,50,50)
racket1 = Player("left_racket", 30,200,4,50,150)
racket2 = Player("right_racket", 520, 200, 4, 50,150)
#прапорці для стану гри
game = True
finish = False

speed_y = 3
speed_x = 3

font.init()
font = font.Font(None, 35)
win2 = font.render("Player Right WIN!", True, (180,0,0))
win1 = font.render("Player Left WIN!", True, (180,0,0))											 
#ігровий цикл
while game:
    #перевірка подій
    for e in event.get():
        if e.type == QUIT:
            game = False
	if finish != True:
		window.fill(background)
		racket1.update_l()
		racket2.update_r()
		ball.rect.x += speed_x
		ball.rect.y += speed_y
		if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
			speed_x *= -1
			speed_y *= - 1
		if ball.rect.y < 0 or ball.rect.y > 450:
			speed_y *= -1
		if ball.rect.x < 0:
			finish = True
			window.blit(win2, (200,200)) #win right
			game = True
		if ball.rect.x > 600:
			finish = True
			window.blit(win1, (200,200)) #win left
			game = True
		racket1.reset()
		racket2.reset()
		ball.reset()
    display.update()
    clock.tick(FPS)

