""" Module containing sprite classes for squares and pieces. """

import pygame

class Square(pygame.sprite.Sprite):
    """ Sprite class for different coloured squares of the chessboard. """
    def __init__(self, x, y, colour):
        super().__init__()       
        
        if colour == 0:
            self.image = pygame.image.load('graphics/squares/square_brown_light.png').convert()
        else:
            self.image = pygame.image.load('graphics/squares/square_brown_dark.png').convert()
        
        self.image = pygame.transform.scale(self.image, (71, 71))
        self.rect = self.image.get_rect(center = (x, y))

class Piece(pygame.sprite.Sprite):
    """ Sprite class for chess pieces. """
    def __init__(self, x, y, key):
        super().__init__()       
        
        self.image = pygame.image.load(f'graphics/pieces/{key}.png').convert_alpha()        
        self.image = pygame.transform.smoothscale(self.image, (51, 51))
        self.rect = self.image.get_rect(center = (x, y))