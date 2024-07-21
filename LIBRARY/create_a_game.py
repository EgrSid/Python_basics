import pygame
import sys  # обращение к системе(железо); os - опрерационная система

pygame.init()  # запускаем библиотеку
pygame.font.init()  # инициализация шрифтов в PyGame

pygame.display.set_caption('PinBall')  # поменяли название окна


pygame.mixer.music.load('st.mp3') # подлючаем музыку на фон
pygame.mixer.music.play(-1) # чтобы музыка играла бесконечно


screen_width, screen_height = 800, 600  # ширина и высота экрана в пикселях
block_width, block_height = 150, 20  # ширина и высота блока в пикселях
circle_radius = 5  # радиус шарика в пикселх
posX_block = screen_width // 2 - block_width // 2  # начальная позиция по х для блока
posX_circle = screen_width // 2  # начальная позиция по х шарика
posY_circle = screen_height - block_height - circle_radius  # начальная позиция по У для шарика

circle_right = True  # направление шарика нвправо
circle_top = True  # направление шарика вверх

speed = 4  # скорость [пикселей/кадр]
score = 0

screen = pygame.display.set_mode((screen_width, screen_height))  # создаем окно
clock = pygame.time.Clock()  # берем компонент часов
font = pygame.font.SysFont('microsottaile', 50)

colors = {'BLACK': (0, 0, 0), 'WHITE': (255, 255, 255),
          'RED': (255, 0, 0), 'GREEN': (0, 200, 64), 'BLUE': (0, 0, 255),
          'YELLOW': (225, 225, 0)}  # палитра RGB

while True:
    clock.tick(60)  # назначаем FPS
    screen.fill(colors['BLACK'])  # красим экран в черный цвет
    text = font.render('SCORE: ' + str(score), True, colors['WHITE'], colors['BLACK']) # создали текст
    text2 = font.render('ВЫ ПРОИГРАЛИ', True, colors['RED'], colors['BLACK'])
    screen.blit(text, (0, 0))

    pressed_keys = pygame.key.get_pressed()  # отслеживание нажатия клавиш


    if pressed_keys[pygame.K_LEFT] and posX_block > 0:
        posX_block -= speed
    if pressed_keys[pygame.K_RIGHT] and posX_block + block_width < screen_width:
        posX_block += speed

    if posY_circle - circle_radius <= 0:  # движение шарика вверх
        circle_top = False

    if posX_circle - circle_radius <= 0:  # движение шарика влево-вправо
        circle_right = True
    elif posX_circle + circle_radius >= screen_width:
        circle_right = False

    if circle_right:  # меняем положене шарика по х
        posX_circle = posX_circle + speed
    else:
        posX_circle = posX_circle - speed

    if circle_top:  # меняем положене шарика по у
        posY_circle -= speed
    else:
        posY_circle += speed

    if posX_block <= posX_circle <= posX_block + block_width and \
            screen_height - block_height <= posY_circle + circle_radius <= screen_height:
        circle_top = True
        score += 1
    elif posY_circle + circle_radius > screen_height:
        pygame.mixer.music.pause()
        screen.blit(text2, (screen_width // 2 - len('ВЫ ПРОИГРАЛИ') // 2 * 25, screen_height // 2))
        pygame.display.update()
        pygame.mixer.music.load('game_over.mp3')
        pygame.mixer.music.play(loops=1) # запуск музыки только 1 раз
        pygame.time.wait(11 * 100)
        pygame.quit(), sys.exit()

    for event in pygame.event.get():  # выход из игры(закрытие приложения)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, colors['BLUE'],
                     (posX_block, screen_height - block_height, block_width, block_height))  # рисуем блок
    pygame.draw.circle(screen, colors['YELLOW'],
                       (posX_circle, posY_circle), circle_radius)

    pygame.display.update()  # обновляем экран