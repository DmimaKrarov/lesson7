
import os
import sys
import random

import pygame

FPS = 60
WHITE = (255, 255, 255)

path = os.path.join(os.path.dirname(__file__), 'data')

size = width, height = 600, 95
pygame.display.set_caption('метнулся кабанчиком 2')
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    filename = os.path.join('data', name)
    try:
        image = pygame.image.load(filename)
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


class Car(pygame.sprite.Sprite):
    image_creature = load_image('car2.png')

    def __init__(self, group):
        super().__init__(group)
        self.group = group
        self.rect = self.image_creature.get_rect()
        self.image = Car.image_creature
        self.rect.x = 0
        self.rect.y = 0
        self.duraction = 5

    def move(self):
        if self.duraction > 0 and self.rect.x + self.rect.width < size[0] or self.duraction < 0 and self.rect.x > 0:
            self.rect.x += self.duraction
        else:
            self.image = pygame.transform.flip(self.image, True, False)
            self.duraction *= -1


all_sprites = pygame.sprite.Group()
creature = Car(all_sprites)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)

    screen.fill(WHITE)
    creature.move()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
