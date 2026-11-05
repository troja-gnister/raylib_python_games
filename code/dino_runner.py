import raylib as rl
from pyray import *
from os.path import join


init_window(1280, 720, 'Dino Runner Basic')
init_audio_device()
set_target_fps(60)


dino_texture = load_texture(join('assets', 'dino', 'run0.png'))
cactus_texture = load_texture(join('assets', 'cactii', 'cactus0.png'))
custom_font = load_font(join('fonts', 'RETRO_SPACE.ttf'))
jump_sound = load_sound(join('audio', 'jump.wav'))
music = load_music_stream(join('audio', 'music.mp3'))
play_music_stream(music)

# game variables 
dino_pos = Vector2(100,300)
velocity = 0
gravity = 0.8
floor_line = 500
cactus_x_pos = 1000

while not window_should_close():
    update_music_stream(music)

    # player movement
    velocity += gravity
    dino_pos.y += velocity
    if dino_pos.y > floor_line:
        dino_pos.y = floor_line
    if is_key_pressed(rl.KEY_SPACE):
        velocity = -28
        play_sound(jump_sound)

    # obstacle logic
    cactus_x_pos -= 8


    begin_drawing()
    clear_background(RAYWHITE)
    draw_line_ex(Vector2(0, floor_line + 120), Vector2(1280, floor_line + 120), 10, GRAY)
    draw_texture_ex(dino_texture, dino_pos, 0, 5, WHITE)
    draw_texture_ex(cactus_texture, Vector2(cactus_x_pos, floor_line), 0, 5, WHITE)

    # collision
    dino_rect = Rectangle(dino_pos.x, dino_pos.y, dino_texture.width * 5, dino_texture.height * 5)
    cactus_rect = Rectangle(cactus_x_pos, floor_line, cactus_texture.width * 5, cactus_texture.height * 5)
    if check_collision_recs(dino_rect, cactus_rect):
        exit()

    score_string = f'score: {int(get_time())}'
    text_width = measure_text_ex(custom_font, score_string, 40, 1).x
    draw_text_ex(custom_font, score_string, Vector2(640 - text_width / 2, 100), 40, 1, GRAY)

    end_drawing()
