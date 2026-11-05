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
cactus_timer = 0
cactus_interval = 3
obstacle_list = []

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
    cactus_timer += 0.02
    if cactus_timer > cactus_interval:
        cactus_timer = 0
        obstacle_list.append(Vector2(1280, floor_line))

    for obstacle_pos in obstacle_list:
        obstacle_pos.x -= 8

    begin_drawing()
    clear_background(RAYWHITE)
    draw_line_ex(Vector2(0, floor_line + 120), Vector2(1280, floor_line + 120), 10, GRAY)
    draw_texture_ex(dino_texture, dino_pos, 0, 5, WHITE)

    for obstacle_pos in obstacle_list:
        draw_texture_ex(cactus_texture, obstacle_pos, 0, 5, WHITE)

    # collision
    dino_rect = Rectangle(dino_pos.x, dino_pos.y, dino_texture.width * 5, dino_texture.height * 5)
    # HINT 1: Lines 46 and 54 show how you visit every obstacle. You need that same
    #         kind of loop here, wrapped around the two lines below.
    # HINT 2: cactus_x_pos is always 1000 and never moves. Which variable holds the
    #         position of the obstacle the loop is currently looking at?
    # HINT 3: That variable is a Vector2, so it has both .x and .y. Use both for the
    #         rectangle instead of hard-coding floor_line.
    # HINT 4: Once you indent cactus_rect and the if-check inside the loop, exit()
    #         runs as soon as ANY obstacle hits the dino.
    cactus_rect = Rectangle(cactus_x_pos, floor_line, cactus_texture.width * 5, cactus_texture.height * 5)
    if check_collision_recs(dino_rect, cactus_rect):
        exit()

    score_string = f'score: {int(get_time())}'
    text_width = measure_text_ex(custom_font, score_string, 40, 1).x
    draw_text_ex(custom_font, score_string, Vector2(640 - text_width / 2, 100), 40, 1, GRAY)

    end_drawing()
