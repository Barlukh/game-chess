""" Module containing classes. """

import pygame

class Matrix():
    """ Class that creates and stores centered coordinates of the chessboard. """
    def __init__(self):
        self.values = {}
        self.create_matrix()

    def alternate(self):
        """ Alternate between 0 and 1. """
        while True:
          yield 0
          yield 1
       
    def create_matrix(self):
        """ Create the matrix, store as dictionary values. """
        y = -20
        colour_change = self.alternate()
        for number in "87654321":
            colour = next(colour_change)
            x = 152
            y += 71
            for letter in "abcdefgh":
                self.values[letter + number] = (x, y, colour)
                colour = next(colour_change)
                x += 71

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