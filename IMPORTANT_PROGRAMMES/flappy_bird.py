import pygame
import random

pygame.init()
font = pygame.font.SysFont('Bauhaus 93', 60)

white = (255, 255, 255)

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

pygame.display.set_caption('FlappyBird')
screen = pygame.display.set_mode((screen_width, screen_height))

bg = pygame.image.load('img/bg.png')  # загружаю картинку заднего фона игры
ground_img = pygame.image.load('img/ground.png')  # загружаю землю

ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 200
pipe_frequence = 1500
last_pipe = pygame.time.get_ticks()
score = 0
pass_pipe = False
button_img = pygame.image.load('img/restart.png')


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_game():
    global score, game_over
    pipe_group.empty() # удаляет все спрайты группы
    flappy.rect.x = 100
    flappy.rect.y = screen_height // 2
    score = 0
    game_over = False

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 3 + 1):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]  # чтобы обращаться к центру птицы
        self.vel = 0
        self.clicked = False

    def update(self):

        if flying:
            self.vel += 0.5
            if self.vel > 8: self.vel = 8
            if self.rect.bottom < 768: self.rect.y += int(self.vel)

        if not game_over:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.vel = -10

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter += 1
            flappy_cooldown = 5

            if self.counter > flappy_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap/2)]  # можем обращаться к блокам по нижней и левой грани
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap/2)]  # можем обращаться к блокам по верхней и левой грани

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0: self.kill() # удаляем объект группы, который уже за экраном

class Button(): # кнопка рестарта игры
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        action = False # будет переменной попадания курсора на рестарт
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            action = True # смотрит попал ли курсор на кнопку
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


bird_group = pygame.sprite.Group()  # ДЛЯ СОЗДАНИЯ АНИМАЦИИ
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)  # добавляем птицу в группу

button = Button(screen_width // 2 - 50, screen_height // 2, button_img)

run = True
while run:
    clock.tick(fps)

    screen.blit(bg, (0, 0))  # подключаю задний фон игры
    bird_group.draw(screen)  # добавляем анимацию птички
    bird_group.update()
    pipe_group.draw(screen)

    screen.blit(ground_img, (ground_scroll, 768))  # подключаю задний фон игры

    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and \
             bird_group.sprites()[0].rect.right > pipe_group.sprites()[0].rect.right and not pass_pipe:
            pass_pipe = True
        if pass_pipe:
            score += 1
            pass_pipe = False

    draw_text(str(score), font, white, int(screen_width/2), 20)


    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True

    if flappy.rect.bottom > 768:
        game_over = True
        flying = False

    if not game_over:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequence:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
            top_pipe = Pipe(screen_width, int(screen_height / 2 + pipe_height), 1)
            pipe_group.add(btm_pipe)  # добавляем столбик в группу
            pipe_group.add(top_pipe)  # добавляем столбик в группу
            last_pipe = time_now

        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:  # количество покселй запаса картинки земли от общей ширины экрана
            ground_scroll = 0
        pipe_group.update()
    else:
        if button.draw():
            reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying:
            flying = True # пауза перед началом игры

    pygame.display.update()

pygame.quit()
