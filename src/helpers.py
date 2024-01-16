def get_hover_color(color_tuple):
    return tuple(color - 25 for color in color_tuple)

print(get_hover_color((255, 105, 97)))