import pygame
from classes.ScreenElement import ScreenElement
from classes.game.logic.GameHandler import GameHandler
from const.colors import *
from const.params import *

class PlayerInfobox(ScreenElement):
    def __init__(self, canvas):
        super().__init__(canvas, COLOR_PLAYER_INFOBOX, hoverable=False)
        self.gameHandler = GameHandler.get_instance()

        self.font = pygame.font.SysFont("Rockwell", 18)

    def set_dimensions(self):
        _, height_canvas = super().get_canvas_dimensions()

        self.width = PLAYER_INFO_BOX_WIDTH
        self.height = PLAYER_INFO_BOX_HEIGHT
        self.top = self.margin_top
        self.left = height_canvas

    def draw_self(self):

        border = pygame.rect.Rect(
            self.left - RECT_BORDER,
            self.top - RECT_BORDER,
            self.width + 2 * RECT_BORDER,
            self.height + 2 * RECT_BORDER
        )

        pygame.draw.rect(self.canvas, COLOR_PLAYER_INFOBOX_BORDER, border)

        super().draw_self()

        text = [
            f"Round:  {self.gameHandler.round}",
            f"Phase:  {self.gameHandler.phase.value}",
            f" ",
            f"Current Player:  {self.gameHandler.get_current_player().name}",
            f"Balance:  {self.gameHandler.get_current_player().balance}",
            f"Tiles:  {len(self.gameHandler.get_player_fields(self.gameHandler.get_current_player()))}",
            f"Income:  {len(self.gameHandler.get_player_fields(self.gameHandler.get_current_player()))}"
        ]

        line_break = 0
        for line in text:
            render_line = self.font.render(line, True, COLOR_PLAYER_INFOBOX_TEXT)
            line_left = self.left + 5
            line_top = self.top + 5 + line_break
            line_break += render_line.get_rect()[3] + 2
            self.canvas.blit(render_line, (line_left, line_top))

    def get_color(self):
        return self.gameHandler.get_current_player().color

    def on_click(self, mouse_button):
        pass

class TileInfobox(ScreenElement):
    def __init__(self, canvas):
        super().__init__(canvas, COLOR_TILE_INFOBOX, hoverable=False)
        self.font = pygame.font.SysFont("Rockwell", 18)
        self.gameHandler = GameHandler.get_instance()
        self.hover_tile = None
        self.is_visible = False

    def set_dimensions(self):
        _, height_canvas = super().get_canvas_dimensions()

        self.width = TILE_INFO_BOX_WIDTH
        self.height = TILE_INFO_BOX_HEIGHT
        self.left = pygame.mouse.get_pos()[0] + 20
        self.top = pygame.mouse.get_pos()[1] + 10

    def draw_self(self):
        if not self.is_visible:
            return
        
        self.set_dimensions()

        border = pygame.rect.Rect(
            self.left - RECT_BORDER,
            self.top - RECT_BORDER,
            self.width + 2 * RECT_BORDER,
            self.height + 2 * RECT_BORDER
        )

        pygame.draw.rect(self.canvas, COLOR_PLAYER_INFOBOX_BORDER, border)

        super().draw_self()
        ownerName = getattr(getattr(self.hover_tile, 'owner', None), 'name', "neutral")
        troopName = getattr(getattr(self.hover_tile, 'troop', None), 'name', "")
        troopHealth = getattr(getattr(self.hover_tile, 'troop', None), 'health', "")
        troopOffense = getattr(getattr(self.hover_tile, 'troop', None), 'offense', "")
        troopDefense = getattr(getattr(self.hover_tile, 'troop', None), 'defense', "")
        troopSpeed = getattr(getattr(self.hover_tile, 'troop', None), 'speed', "")
        troopUpkeep = getattr(getattr(self.hover_tile, 'troop', None), 'upkeep', "")
        buildingName = getattr(getattr(self.hover_tile, 'building', None), 'name', "")
        buildingHealth = getattr(getattr(self.hover_tile, 'building', None), 'health', "")

        text = []
        if ownerName:
            text.append(f"Tile Owner:  {ownerName}")
        if troopName:
            text.append(f"Unit Name:  {troopName}")
        if troopHealth:
            text.append(f"Unit Health:  {troopHealth}")
        if troopOffense:
            text.append(f"Unit Offense:  {troopOffense}")
        if troopDefense:
            text.append(f"Unit Defense:  {troopDefense}")
        if troopSpeed:
            text.append(f"Unit Speed:  {troopSpeed}")
        if troopUpkeep:
            text.append(f"Unit Upkeep:  {troopUpkeep}")
        #if buildingName:
        #text.append(f"Building name: {buildingName}")
        #if buildingHealth:
        #text.append(f"Building health: {buildingHealth}")


        line_break = 0
        for line in text:
            render_line = self.font.render(line, True, COLOR_TILE_INFOBOX_TEXT)
            line_left = self.left + 5
            line_top = self.top + 5 + line_break
            line_break += render_line.get_rect()[3] + 2
            self.canvas.blit(render_line, (line_left, line_top))

    def get_color(self):
        color = getattr(getattr(self.hover_tile, 'owner', None), 'color', None)
        if color:
            return color
        else:
            return COLOR_TILE_INFOBOX

    def on_click(self, mouse_button):
        pass

    def on_tile_hover(self, tile_position):
        self.is_visible = True
        self.hover_tile = GameHandler.get_instance().board.fields[tile_position[0]][
            tile_position[1]
        ]
    
    def off_tile_hover(self):
        self.is_visible = False
