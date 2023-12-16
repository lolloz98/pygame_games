from enum import Enum

screen_size = (300, 600)

tile_basic_size = (50, 10)
tile_basic_color = '#00FF00'

character_size = (20, 20)
jump_force = 550
character_init_pos = (150, 500)
character_color = '#FFFF00'
character_x_vel = 300
character_image = './assets/dodo.png'

gravity = 1000
max_fps = 60

lift_screen_height = 400

moving_tile_vel = (100, 100)
tile_offset_to_die = 400

basic_enemy_dims = (40, 40)


class Dir(Enum):
    LEFT = -1
    RIGHT = 1
    NONE = 0

