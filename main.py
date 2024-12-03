""" Main execution module of the game. """

import pygame
import classes

pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('graphics/pieces/b_king.png')
pygame.display.set_caption('Chess')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

def draw_board():
    """ Draw all the squares of the chessboard. """
    matrix = classes.Matrix()
    squares = pygame.sprite.Group()
    for value in matrix.values.values():  
        x = value[0]
        y = value[1]
        colour = value[2]
        squares.add(classes.Square(x, y, colour))

    squares.draw(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    draw_board()

    pygame.display.update()
    clock.tick(60)