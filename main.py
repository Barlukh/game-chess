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

def get_mouse():
    """ Get and return a tuple of x and y position of the cursor. """
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    return (mouse_x, mouse_y)

def create_pieces():
    """ Create a sprite.Group for all the pieces with their starting positions. """
    starting_positions = coordinates.create_positions()
    board_matrix = coordinates.create_matrix()
    for key, values in starting_positions.items():  
        for value in values:
            x = board_matrix[value][0]
            y = board_matrix[value][1]
            pieces.add(classes.Piece(x, y, key))

def create_board():
    """ Create a sprite.Group for all the squares of the chessboard and save the image. """
    board_matrix = coordinates.create_matrix()
    for value in board_matrix.values():  
        x = value[0]
        y = value[1]
        colour = value[2]
        squares.add(classes.Square(x, y, colour))
    squares.draw(screen)
    pygame.image.save(screen, 'graphics/squares/chessboard.png')

pieces = pygame.sprite.Group()
squares = pygame.sprite.Group()
create_board()
create_pieces()

chessboard = pygame.image.load('graphics/squares/chessboard.png')

# def get_selected(piece: object):

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece in pieces:
                if piece.rect.collidepoint(get_mouse()):
                    piece.image = pygame.transform.smoothscale(piece.image, (61, 61))
                    piece.rect = piece.image.get_rect(center = (get_mouse()))
    #                 selected = pygame.sprite.GroupSingle()
    #                 selected.add(classes.Piece)

    # # selected.image = pygame.transform.smoothscale(selected.image, (61, 61))
    # # selected.rect = selected.image.get_rect(center = (get_mouse()))
    
    screen.blit(chessboard, (0, 0))
    pieces.draw(screen)

    pygame.display.update()
    clock.tick(60)