""" Create dictionaries of starting coordinates for chessboard squares and pieces. """

def alternate():
    """ Alternate between integers 0 and 1 and yield the result. """
    while True:
        yield 0
        yield 1
    
def create_matrix():
    """ Create positional matrix of the chessboard, return a dictionary. """
    values = {}
    y = -20
    colour_change = alternate()
    
    for number in '87654321':
        colour = next(colour_change)
        x = 152
        y += 71
        for letter in 'abcdefgh':
            values[letter + number] = (x, y, colour)
            colour = next(colour_change)
            x += 71
    return values

def create_positions():
    """ Create starting positions for all pieces, return a dictionary. """
    values = {}
    b_bishop = ('b_bishop', 'c8', 'f8')
    b_king = ('b_king', 'e8')
    b_knight = ('b_knight', 'b8', 'g8')
    b_pawn = ('b_pawn', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7')
    b_queen = ('b_queen', 'd8')
    b_rook = ('b_rook', 'a8', 'h8')
    w_bishop = ('w_bishop', 'c1', 'f1')
    w_king = ('w_king', 'e1')
    w_knight = ('w_knight', "b1", 'g1')
    w_pawn = ('w_pawn', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2')
    w_queen = ('w_queen', 'd1')
    w_rook = ('w_rook', 'a1', 'h1')
    pieces = (b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook, w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook)

    for piece in pieces:
        values[piece[0]] = []
        for i in range(len(piece) - 1):
            values[piece[0]].append(piece[i + 1])
    return values 