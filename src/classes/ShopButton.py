from classes.ScreenElement import ScreenElement
from const.colors import *


class ShopButton(ScreenElement):
    def __init__(self, canvas):
      super().__init__(canvas, COLOR_SHOP_ICON, hoverable=True)

      self.width = 150
      self.height = 60
      
      self.isopen = False
      self.hover = False

    def set_dimensions(self):
        self.top = self.margin_top
        self.left = self.width_canvas - self.margin_right - self.width
        
    def draw_self(self):
        super().draw_self()
        
        shop_icon_text = "Shop"

        if self.isopen:
            shop_icon_text = "Back"

        render_text = self.font.render(shop_icon_text, True, COLOR_SHOP_TEXT)
        text_left = self.icon_left + (self.icon_width - render_text.get_width()) / 2
        text_top = self.icon_top + (self.icon_height - render_text.get_rect()[3]) / 2
        self.canvas.blit(render_text, (text_left, text_top))

    def open_shop(self):
        self.isopen = True
    
    def close_shop(self):
        self.isopen = False
