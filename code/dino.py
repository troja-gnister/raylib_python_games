from settings import *
from sprites import Sprite


class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME)
        set_target_fps(60)
        self.sprite = Sprite(load_texture(join('assets', 'dino', 'run0.png' )), Vector2(100, 100))

    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)
        draw_line_ex(Vector2(0,FLOOR_LINE + 120), Vector2(WINDOW_WIDTH, FLOOR_LINE + 120), 10, MAIN_COLOR)
        self.sprite.draw()

        end_drawing()

    def run(self):
        while not window_should_close():
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
