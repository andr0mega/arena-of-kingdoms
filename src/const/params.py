import json

# GUI
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



GAME_SETTINGS = json.dumps(
    {"player_amount": 4, "start_balance": 20, "board_width": 32, "board_height": 32}
)

KING = json.dumps(
    {
        "display_name": "King",
        "name": "king",
        "cost": 0,
        "health": 50,
        "offense": 3,
        "defense": 3,
        "speed": 1,
        "upkeep": 0,
        "attack_range": 1,
    }
)

TROOPS = json.dumps(
    [
        {
            "display_name": "Warrior",
            "name": "warrior",
            "cost": 20,
            "health": 20,
            "offense": 10,
            "defense": 5,
            "speed": 1,
            "upkeep": 3,
            "attack_range": 1,
            "description": "Slow but powerful offensive unit",
            
        }
    ]
)

BUILDINGS = json.dumps(
    [
        {
            "display_name": "Goldmine",
            "name": "goldmine",
            "cost": 20,
            "health": 10,
            "blocking": False,
            "production": 3,
            "description": "Building to generate passive income",
        }
    ]
)
