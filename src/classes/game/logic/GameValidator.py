from GameHandler import GameHandler
from GameBoard import GameCoordinate

def valid_king_position(gameHandler: GameHandler, coordinate: GameCoordinate):
    board = gameHandler.board
    x = coordinate.x
    y = coordinate.y
    for c_x in range(x-1, x+2):
        for c_y in range(y-1, y+2):
            if c_x < 0 or c_y < 0:
                return False
            elif len(board.fields) <= c_x or len(board.fields[c_x]) <= c_y:
                return False
            field = board.fields[c_x][c_y]
            if(field.owner != None):
                return False
    return True

