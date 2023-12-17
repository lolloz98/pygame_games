from enum import Enum

screen_size = (300, 600)
background_img = './assets/background.png'

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
normal_tile = './assets/normal_tile.png'
disappearing_tile = './assets/disappearing_tile.png'
jump_tile = './assets/jump_tile.png'
move_xy_tile = './assets/move_xy_tile.png'
move_x_tile = './assets/move_x_tile.png'


basic_enemy_dims = (40, 40)
wind = './assets/wind.png'

projectile_y_vel = -400
projectile = './assets/grr.png'


wings_active = './assets/wings_active.png'
wings_inactive = './assets/wings_inactive.png'
wings_y_vel = -600
wings_ttl = 2


class Dir(Enum):
    LEFT = -1
    RIGHT = 1
    NONE = 0

