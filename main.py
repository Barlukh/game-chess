""" Main execution module of the game. """

import pygame

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/squares/square_brown_dark.png').convert
        self.rect = self.image.get_rect(topleft = (0, 0))

pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('graphics/pieces/b_king.png')
pygame.display.set_caption('Chess')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

square_dark = pygame.image.load('graphics/squares/square_brown_dark.png')
square_dark = pygame.transform.scale(square_dark, (70, 70))
square_light = pygame.image.load('graphics/squares/square_brown_light.png')
square_light = pygame.transform.scale(square_light, (70, 70))

square_matrix = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    screen.blit(square_dark, (0, 0))

    pygame.display.update()
    clock.tick(60)