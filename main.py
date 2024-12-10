""" Main execution module of the game. """

import pygame
import classes
import coordinates
import copy

pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('graphics/pieces/b_king.png')
pygame.display.set_caption('Chess')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

def check_overlap():
    """ Check for a collision of pieces. Return bool. """
    overlap = False
    for piece in pieces:
        if piece.rect.colliderect(selected.sprite.rect):
            overlap = True
    return overlap

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
selected = pygame.sprite.GroupSingle()
create_board()
create_pieces()

chessboard = pygame.image.load('graphics/squares/chessboard.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece in pieces:
                if piece.rect.collidepoint(get_mouse()):
                    piece.remove(pieces)
                    piece.add(selected)
                    original = copy.copy(piece)
        
        if event.type == pygame.MOUSEBUTTONUP:
            if check_overlap() == True:
                selected.sprite.rect.center = original.rect.center
                selected.sprite.add(pieces)
                selected.sprite.remove(selected)
            else:
                for square in squares:
                    if square.rect.collidepoint(get_mouse()):
                        selected.sprite.rect.center = square.rect.center
                        selected.sprite.add(pieces)
                        selected.sprite.remove(selected)
    
    if len(selected) != 0:
        selected.sprite.rect = selected.sprite.image.get_rect(center = (get_mouse()))
    
    screen.blit(chessboard, (0, 0))
    pieces.draw(screen)
    selected.draw(screen)

    pygame.display.update()
    clock.tick(60)