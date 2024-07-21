import random
import pygame

pygame.init()

font = pygame.font.SysFont('Bauhaus 93', 60)

clock = pygame.time.Clock()
fps = 60

screen_width = 1900
screen_high = 800

pygame.display.set_caption('Dinosaur')
screen = pygame.display.set_mode((screen_width, screen_high))

road_img = pygame.image.load('img/road.png')
road_scroll = 0
scroll_speed = 8
index = 0

but_img = pygame.image.load('img/rt.png')
but_img = pygame.transform.scale(but_img, (300, 300))


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'img/run{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
        self.top_move = False

    def jump(self):
        global jumping, score, cactus_pass

        if jumping:
            if self.vel < 35:
                self.vel += 1
                self.rect.y -= 7
            elif self.vel < 70:
                self.vel += 1
                self.rect.y += 7
            else:
                jumping = False
                self.vel = 0
                if len(cactus_group) > 0:
                    if dinosaur_group.sprites()[0].rect.left > cactus_group.sprites()[0].rect.left and \
                            dinosaur_group.sprites()[0].rect.right > cactus_group.sprites()[0].rect.right \
                            and not cactus_pass:
                        score += 1
                        cactus_pass = True
                    if cactus_pass:
                        cactus_pass = False
            return cactus_pass

    def update(self):

        if not game_over:
            self.counter += 1
            dinosaur_cooldown = 5
            if self.counter > dinosaur_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]


class Cactus(pygame.sprite.Sprite):
    index = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f'img/{num}.png')
            self.images.append(img)
        self.image = random.choice(self.images)
        counter = self.images.index(self.image)
        if counter in [0, 1, 2]:
            y = screen_high - 123
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x < 0: self.kill()


class Button():  # кнопка рестарта игры
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        action = False  # будет переменной попадания курсора на рестарт
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            action = True  # смотрит попал ли курсор на кнопку
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


def restart():
    global game_over, score
    game_over = False
    cactus_group.empty()
    dinosaur.rect.y = screen_high - 119
    score = 0


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


"""создаем группу для динозавра"""
dinosaur_group = pygame.sprite.Group()
dinosaur = Dinosaur(screen_width // 2, screen_high - 73)
dinosaur_group.add(dinosaur)

cactus_group = pygame.sprite.Group()

game_over = False
run = True
white = (255, 255, 255)
black = (0, 0, 0)
jumping = False
last_cactus = pygame.time.get_ticks()
cactus_pass = False
score = 0

button = Button(screen_width // 2, screen_high // 2, but_img)

while run:
    cactus_friquence = random.randint(1000, 3000)

    clock.tick(fps)

    screen.fill(white)

    dinosaur_group.draw(screen)
    dinosaur_group.update()

    cactus_group.draw(screen)

    pressed_keys = pygame.key.get_pressed()

    if pygame.sprite.groupcollide(dinosaur_group, cactus_group, False, False):
        screen.blit(road_img, (road_scroll, screen_high - 40))
        screen.blit(road_img, (road_scroll + 2350, screen_high - 40))
        game_over = True

    draw_text(str(score), font, black, screen_width // 2, screen_high // 4)

    if not game_over:
        road_scroll -= scroll_speed

        time_now = pygame.time.get_ticks()
        if time_now - last_cactus > cactus_friquence:
            cactus = Cactus(screen_width, screen_high - 99)
            cactus_group.add(cactus)
            last_cactus = time_now

        if abs(road_scroll) >= 2404:
            road_scroll += 2350
            screen.blit(road_img, (road_scroll, screen_high - 40))
            screen.blit(road_img, (road_scroll + 2350, screen_high - 40))
        else:
            screen.blit(road_img, (road_scroll + 2350, screen_high - 40))
            screen.blit(road_img, (road_scroll, screen_high - 40))

        cactus_group.update()

    else:
        if button.draw():
            restart()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True

    dinosaur.jump()

    pygame.display.update()
pygame.quit()
