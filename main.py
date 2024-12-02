""" Main execution module of the game. """

import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.squares = []
        self.matrix = {}
    
    def alternate(self):
        while True:
          yield 1
          yield 0

    def draw_matrix(self):
        y = -50
        colour_change = self.alternate()
        for number in "87654321":
            colour = next(colour_change)
            x = 120
            y += 70
            for letter in "abcdefgh":
                rectangle = self.squares[colour].get_rect(topleft = (x, y))
                self.matrix[letter + number] = (rectangle, colour)
                screen.blit(self.squares[colour], (x, y))
                colour = next(colour_change)
                x += 70
    
    def load_squares(self):
        for name in ['square_brown_dark.png', 'square_brown_light.png']:
            square = pygame.image.load(f'graphics/squares/{name}').convert()
            square = pygame.transform.scale(square, (70, 70))
            self.squares.append(square)

    def draw_board(self):
        self.load_squares()
        self.draw_matrix()

pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('graphics/pieces/b_king.png')
pygame.display.set_caption('Chess')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

chessboard = Board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    chessboard.draw_board()

    pygame.display.update()
    clock.tick(60)