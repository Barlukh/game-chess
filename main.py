""" Main execution module of the game. """

import pygame
import classes
import coordinates

pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('graphics/pieces/b_king.png')
pygame.display.set_caption('Chess')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
board_matrix = coordinates.create_matrix()
starting_positions = coordinates.create_positions()

def draw_pieces():
    """ Draw all the pieces on the chessboard. """
    pieces = pygame.sprite.Group()
    for key, values in starting_positions.items():  
        for value in values:
            x = board_matrix[value][0]
            y = board_matrix[value][1]
            pieces.add(classes.Piece(x, y, key))
    pieces.draw(screen)

def draw_board():
    """ Draw all the squares of the chessboard. """
    squares = pygame.sprite.Group()
    for value in board_matrix.values():  
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
    draw_pieces()

    pygame.display.update()
    clock.tick(60)