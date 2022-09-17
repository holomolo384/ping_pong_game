from pygame import *

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

