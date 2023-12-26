# Chess Dictionary Validator

def isValidChessBoard(board: dict) -> bool:
    '''
    Indicates if the dictionary <board> is a valid chess board.
    A valid chess board has exactly one black king and one white king.
    Each player can have at most 16 pieces, at most 8 pawns, and all
    pieces must be on a valid space from '1a' to '8h'.
    The piece names begin with either 'w' or 'b' to represent white
    or black, followed by 'pawn', 'knight', 'bishop', 'rook',
    'queen' or 'king'.
    '''
    pieces = {}
    for k,v in board.items():
        if len(k) != 2 or \
                not ('1' <= k[0] <= '8') or \
                not ('a' <= k[1] <= 'h'):
            return False  # Improper key name.

        if type(v) != str:
            return False  # Invalid value (not a string).
        elif len(v) > 0:
            if v[0] == 'w' or v[0] == 'b':
                pieces.setdefault(v[0] + 'Pieces', 0)
                pieces[v[0] + 'Pieces'] += 1
            else:
                return False  # Missing color (white or black).

            if v[1:] in ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king'):
                pieces.setdefault(v, 0)
                pieces[v] += 1
            else:
                return False  # Invalid piece name.

    # Now count the proper pieces from the board.
    for color in ('w', 'b'):
        if pieces.get(color + 'king', 0) != 1:
            return False  # Needs exactly one king.
        if pieces.get(color + 'Pieces', 0) > 16:
            return False  # Needs at most 16 pieces per player
        if pieces.get(color + 'pawn', 0) > 8:
            return False  # Needs at most 8 pawns

    return True

# And now some tests:
boards = [{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'},
            {'1z': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'},
            {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'gking'},
            {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen'},
            {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4c': 'wpawn'}]
for board in boards:
    print(f'This board {board} is valid? {isValidChessBoard(board)}')
