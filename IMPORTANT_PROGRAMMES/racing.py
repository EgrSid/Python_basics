import sys
import pygame

pygame.init()
pygame.font.init()

pygame.display.set_caption('Racing')

pygame.mixer.music.load('cybersdf-night-rider.mp3')
pygame.mixer.music.play(-1)

speed_for_blocks = 3

screen_width, screen_high = 1000, 600

"""параметры препятствий"""
block_width, block_high = 320, 60
posX_block1 = 0
posX_block2 = screen_width - block_width
posX_block3 = screen_width // 2 + block_width // 2
posX_block4 = screen_width // 2 - block_width

posY_block1 = 0
posY_block2 = 0
posY_block3 = 0
posY_block4 = 0
posY_block = 0


class Car:
    """параметры корпуса gмашинки"""
    car_width, car_high = 30, 100
    posX_car = screen_width // 2 - car_width // 2
    posY_car = screen_high // 1.5

    """параметры колес машинки"""
    wheel_width, wheel_high = 7, 30
    posX_wheel1 = posX_car + car_width
    posX_wheel2 = posX_car + car_width
    posX_wheel3 = posX_car - wheel_width
    posX_wheel4 = posX_car - wheel_width

    posY_wheel1 = posY_car
    posY_wheel2 = posY_car + car_high - wheel_high
    posY_wheel3 = posY_car + car_high - wheel_high
    posY_wheel4 = posY_car

    """ параметры кабины машины"""
    cabin_width, cabin_high = 10, 40
    posX_cabin = posX_car + car_width // 2 - cabin_width // 2
    posY_cabin = posY_car + car_high // 2

    """скорость машинки"""
    speed = 5

    def draw(self):
        """рисую машинку"""
        pygame.draw.rect(screen, colors['YELLOW'],
                         (self.posX_car, self.posY_car, self.car_width, self.car_high))
        pygame.draw.rect(screen, colors['WHITE'],
                         (self.posX_wheel1, self.posY_wheel1, self.wheel_width, self.wheel_high))
        pygame.draw.rect(screen, colors['WHITE'],
                         (self.posX_wheel2, self.posY_wheel2, self.wheel_width, self.wheel_high))
        pygame.draw.rect(screen, colors['WHITE'],
                         (self.posX_wheel3, self.posY_wheel3, self.wheel_width, self.wheel_high))
        pygame.draw.rect(screen, colors['WHITE'],
                         (self.posX_wheel4, self.posY_wheel4, self.wheel_width, self.wheel_high))
        pygame.draw.rect(screen, colors['WHITE'],
                         (self.posX_cabin, self.posY_cabin, self.cabin_width, self.cabin_high))

colors = {'BLACK': (0, 0, 0), 'WHITE': (255, 255, 255),
          'RED': (255, 0, 0), 'GREEN': (0, 200, 64), 'BLUE': (0, 0, 255),
          'YELLOW': (225, 225, 0)}  # палитра RGB

screen = pygame.display.set_mode((screen_width, screen_high))
clock = pygame.time.Clock()
font = pygame.font.SysFont('microsottaile', 50)

k = True  # счетчик препятствий

if __name__ == '__main__':
    while True:
        clock.tick(60)
        screen.fill(colors['BLACK'])
        text = font.render('ВЫ ПРОИГРАЛИ', True, colors['BLACK'], colors['RED'])

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and Car.posX_car > 0:  # анимация движения машинки
            Car.posX_wheel1 -= Car.speed
            Car.posX_wheel2 -= Car.speed
            Car.posX_wheel3 -= Car.speed
            Car.posX_wheel4 -= Car.speed
            Car.posX_car -= Car.speed
            Car.posX_cabin -= Car.speed
        if pressed_keys[pygame.K_RIGHT] and Car.posX_car + Car.car_width < screen_width:  # анимация движения машинки
            Car.posX_car += Car.speed
            Car.posX_wheel1 += Car.speed
            Car.posX_wheel2 += Car.speed
            Car.posX_wheel3 += Car.speed
            Car.posX_wheel4 += Car.speed
            Car.posX_cabin += Car.speed

        """рисую препятствия и задаю им движение"""
        if posY_block < screen_high:
            posY_block += speed_for_blocks
            if k:
                pygame.draw.rect(screen, colors['BLUE'],
                                 (posX_block1, posY_block1, block_width, block_high))
                pygame.draw.rect(screen, colors['BLUE'],
                                 (posX_block3, posY_block3, block_width, block_high))
                posY_block1 += speed_for_blocks
                posY_block3 += speed_for_blocks
            elif not k:
                pygame.draw.rect(screen, colors['BLUE'],
                                 (posX_block2, posY_block2, block_width, block_high))
                pygame.draw.rect(screen, colors['BLUE'],
                                 (posX_block4, posY_block4, block_width, block_high))
                posY_block2 += speed_for_blocks
                posY_block4 += speed_for_blocks
        else:
            if k:
                k = False
            else:
                k = True
                posY_block1 = 0
                posY_block3 = 0
                posY_block4 = 0
                posY_block2 = 0
            posY_block = 0

        """проигрыш"""  # через '/' отделен удар о каждое препятствие
        if (
                posX_block1 <= Car.posX_wheel4 <= posX_block1 + block_width or posX_block1 <= Car.posX_wheel1 + Car.wheel_width <= posX_block1 + block_width) and \
                (
                        posY_block1 <= Car.posY_wheel4 <= posY_block1 + block_high or posY_block1 <= Car.posY_wheel3 <= posY_block1 + block_high or posY_block1 <= Car.posY_wheel3 + Car.wheel_high <= posY_block1 + block_high) or \
                (
                        posX_block2 <= Car.posX_wheel4 <= posX_block2 + block_width or posX_block2 <= Car.posX_wheel1 + Car.wheel_width <= posX_block2 + block_width) and \
                (
                        posY_block2 <= Car.posY_wheel4 <= posY_block2 + block_high or posY_block2 <= Car.posY_wheel3 <= posY_block2 + block_high or posY_block2 <= Car.posY_wheel3 + Car.wheel_high <= posY_block2 + block_high) or \
                (
                        posX_block3 <= Car.posX_wheel4 <= posX_block3 + block_width or posX_block3 <= Car.posX_wheel1 + Car.wheel_width <= posX_block3 + block_width) and \
                (
                        posY_block3 <= Car.posY_wheel4 <= posY_block3 + block_high or posY_block3 <= Car.posY_wheel3 <= posY_block3 + block_high or posY_block3 <= Car.posY_wheel3 + Car.wheel_high <= posY_block3 + block_high) or \
                (
                        posX_block4 <= Car.posX_wheel4 <= posX_block4 + block_width or posX_block4 <= Car.posX_wheel1 + Car.wheel_width <= posX_block4 + block_width) and \
                (
                        posY_block4 <= Car.posY_wheel4 <= posY_block4 + block_high or posY_block4 <= Car.posY_wheel3 <= posY_block4 + block_high or posY_block4 <= Car.posY_wheel3 + Car.wheel_high <= posY_block4 + block_high):
            pygame.mixer.music.pause()
            screen.blit(text, (screen_width // 2 - len('ВЫ ПРОИГРАЛИ') // 2 * 25, screen_high // 2))
            pygame.display.update()
            pygame.mixer.music.load('game_over.mp3')
            pygame.mixer.music.play(loops=1)
            pygame.time.wait(11 * 100)
            pygame.quit()
            sys.exit()

        """выход из игры"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        Car().draw()

        pygame.display.update()
