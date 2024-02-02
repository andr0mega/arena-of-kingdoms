import json

#GUI
MARGIN_TOP = 30
MARGIN_LEFT = 30
MARGIN_RIGHT = 30
MARGIN_BOTTOM = 30

RECT_BORDER = 1

SHOP_BUTTON_WIDTH = 150
SHOP_BUTTON_HEIGHT = 60
END_TURN_BUTTON_WIDTH = 150
END_TURN_BUTTON_HEIGHT = 50
PLAYER_INFO_BOX_WIDTH = 300
PLAYER_INFO_BOX_HEIGHT = 180
TILE_INFO_BOX_WIDTH = 300
TILE_INFO_BOX_HEIGHT = 180
SPACING_INFO_BOXES_HEIGHT = 20

#GAME SETTINGS
PLAYER_AMOUNT = 4
START_BALANCE = 20

GAME_SETTINGS = json.dumps([{
    "player_amount": 4,
    "start_balance": 20,
    "board_width": 16,
    "board_height": 16
}])

#ELEMENTS
KING_HEALTH = 50
KING_OFF = 3
KING_DEFF = 3
KING_SPEED = 1
KING_UPKEEP = 0
KING_DESCRIPTION = "The most important unit, do not let it die"

WARRIOR_COST = 20
WARRIOR_HEALTH = 20
WARRIOR_OFF = 10
WARRIOR_DEFF = 5
WARRIOR_SPEED = 1
WARRIOR_UPKEEP = 3
WARRIOR_DESCRIPTION = "Slow but powerful offensive unit"

GOLDMINE_COST = 25
GOLDMINE_HEALTH = 10
GOLDMINE_BLOCKING = False
GOLDMINE_PRODUCTION = 3
GOLDMINE_DESCRIPTION = "Building to generate passive income"

KING = json.dumps({
    "display_name":"King",
    "name":"king",
    "cost": 0,
    "health": 50,
    "offense": 3,
    "defense": 3,
    "speed": 1,
    "upkeep": 0 })

TROOPS = json.dumps([{
    "display_name": "Warrior",
    "name": "warrior",
    "cost": 20,
    "health": 20,
    "offense": 10,
    "defense": 5,
    "speed": 1,
    "upkeep": 3,
    "description": "Slow but powerful offensive unit"
}])

BUILDINGS = json.dumps([{
    "display_name": "Goldmine",
    "name": "goldmine",
    "cost": 20,
    "health": 10,
    "blocking": False,
    "production": 3,
    "description": "Building to generate passive income"
}])

