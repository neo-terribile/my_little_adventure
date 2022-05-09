import os
import rpg.sprites.view
import rpg.maps.map

from pygame.locals import Rect
from rpg.sprites.view import north, east, south, west

tiles_folder = "tiles"
maps_folder = "maps"
SPECIAL_LEVEL = "S"
DOWN_LEVEL = "D"
VERTICAL_MASK = "V"
open_sq_bracket = "["
close_sq_bracket = "]"
colon = ":"
comma = ","
dash = "-"
sprite = "sprite"
event = "event"
music = "music"


map_cache = {}



