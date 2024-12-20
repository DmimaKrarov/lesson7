import os
import sys
import random

import pygame

FPS = 60
WHITE = (255, 255, 255)

path = os.path.join(os.path.dirname(__file__), 'data')

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
pygame.display.set_caption('метнулся кабанчиком')
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    filename = os.path.join('data', name)
    try:
        image = pygame.image.load(filename)
    # если файл не существует, то выходим
    except FileNotFoundError:
        print(f"Файл с изображением '{filename}' не найден")
        sys.exit()
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Creature(pygame.sprite.Sprite):
    image_creature = load_image('creature.png')

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.group = group  # доступ к группе спрайтов внутри класса
        self.rect = self.image_creature.get_rect()
        self.image = Creature.image_creature
        self.rect.x = 0
        self.rect.y = 0

    def move(self, duraction):
        if duraction == 'Вверх':
            self.rect.y -= 10
        if duraction == 'Вниз':
            self.rect.y += 10
        if duraction == 'Вправо':
            self.rect.x += 10
        if duraction == 'Влево':
            self.rect.x -= 10


# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()
creature = Creature(all_sprites)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)

    keys = pygame.key.get_pressed()

    # Проверяем, нажаты ли стрелочные клавиши
    if keys[pygame.K_UP]:
        creature.move("Вверх")
    if keys[pygame.K_DOWN]:
        creature.move("Вниз")
    if keys[pygame.K_LEFT]:
        creature.move("Влево")
    if keys[pygame.K_RIGHT]:
        creature.move("Вправо")

    screen.fill(WHITE)

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
