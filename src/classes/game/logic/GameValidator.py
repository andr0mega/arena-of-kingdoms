from copy import copy, deepcopy
from classes.game.logic.GameBoard import GameBoard
from classes.game.logic.GamePlayer import GamePlayer


def valid_king_position(gameHandler, coordinate):
    board = gameHandler.board
    x = coordinate.x
    y = coordinate.y
    for c_x in range(coordinate.x - 1, coordinate.x + 2):
        for c_y in range(coordinate.y - 1, coordinate.y + 2):
            if c_x < 0 or c_y < 0:
                return False
            elif len(board.fields) <= c_x or len(board.fields[c_x]) <= c_y:
                return False
            field = board.fields[c_x][c_y]
            if field.owner != None:
                return False
    return True


def is_valid_turn(gameHandler):
    player = gameHandler.get_current_player()
    fields = gameHandler.board.fields
    for row in fields:
        for field in row:
            if (
                field.troop != None
                and field.troop.name == "king"
                and field.troop in player.units
            ):
                return True
    return False


def __write_fields_recursive(
    board, remaining_mov: int, current, current_track, possible_fields
):
    cField = board[current[0]][current[1]]
    if cField in current_track:
        return
    if len(current_track) > 0 and (
        cField.troop != None or (cField.building != None and cField.building.blocking)
    ):
        return
    if not len(current_track) == 0:
        possible_fields.append(current)
    current_track.append(cField)
    if remaining_mov == 0:
        return
    remaining_mov -= 1
    history = copy(current_track)
    for x in range(current[0] - 1, current[0] + 2):
        for y in range(current[1] - 1, current[1] + 2):
            if x >= 0 and y >= 0 and len(board) > x and len(board[x]) > y:
                current_track = copy(history)
                __write_fields_recursive(
                    board, remaining_mov, tuple([x, y]), current_track, possible_fields
                )


def possible_move_positions(movement: int, board, start_coordinates):
    current = tuple([start_coordinates.x, start_coordinates.y])
    possibleFields = []
    __write_fields_recursive(board, movement, current, [], possibleFields)
    return possibleFields

def possible_attack_positions(attack_range, board: GameBoard, start_coordinates, current_player: GamePlayer):
    #Has to  be changed, as soon as blocking constructs enter the game
    attackable_fields = []
    for x in range(start_coordinates.x - attack_range, start_coordinates.x + attack_range + 1):
        for y in range(start_coordinates.y - attack_range, start_coordinates.y + attack_range + 1):
            if(x < 0 or y < 0 or x >= len(board.fields) or y >= len(board.fields[x])):
                continue
            fieldTroop = board.fields[x][y].troop
            if(fieldTroop != None and not fieldTroop in current_player.units):
                attackable_fields.append(tuple([x, y]))
    return attackable_fields