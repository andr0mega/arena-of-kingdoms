def valid_king_position(gameHandler, coordinate):
    board = gameHandler.board
    x = coordinate.x
    y = coordinate.y
    for c_x in range(coordinate.x-1, coordinate.x+2):
        for c_y in range(coordinate.y-1, coordinate.y+2):
            if c_x < 0 or c_y < 0:
                return False
            elif len(board.fields) <= c_x or len(board.fields[c_x]) <= c_y:
                return False
            field = board.fields[c_x][c_y]
            if(field.owner != None):
                return False
    return True

def is_valid_turn(gameHandler):
    player = gameHandler.get_current_player()
    fields = gameHandler.board.fields
    for row in fields:
        for field in row:
            if(field.troop != None and field.troop.name == "king" and field.owner == player):
                return True
    return False