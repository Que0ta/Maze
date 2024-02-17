from pygame import *
'''Необхідні класи'''

mixer.init()
#клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
# головний герой та його керування
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y,wall_width, wall_height):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height)) # картинка стіни(вигляд)
        self.image.fill((color1,color2,color3))
        self.rect = self.image.get_rect()   # стіна має хітбокс
        self.rect.y  = wall_y
        self.rect.x = wall_x

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

'''надписи'''
font.init()
font = font.Font(None, 70)
win = font.render("YOU'VE WON!", True, (255,215, 0))
lose = font.render("YOU'VE LOST!", True, (180,0,0))

#стіни
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 450, 130, 10, 360)
w6 = Wall(154, 205, 50, 300, 20, 10, 350)
w7 = Wall(154, 205, 50, 390, 120, 130, 10)

finish = False 
#Ігрова сцена:
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
#Персонажі гри:
player = Player('hero.png', 5, win_height - 80, 4)
monster = GameSprite('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
game = True
clock = time.Clock()
FPS = 60

#музика
# звукові ефекти
finish = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
mixer.music.load('jungles.ogg')
mixer.music.play()
 
while game:
    for ev in event.get():
        if ev.type == QUIT:
            game = False
        # if ev.type == KEYDOWN:
        #     if ev.key == K_1:
        #         print('pressed <1>')
    if finish != True:
        window.blit(background,(0, 0))
        player.reset()
        monster.reset()

        player.update()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

    display.update()
    clock.tick(FPS)
