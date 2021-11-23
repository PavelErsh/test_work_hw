import arcade

# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 600

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Шаблон"


class OurGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    # начальные значения
    def setup(self):
        pass

    # отрисовка объектов
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)

    # логика
    def update(self, delta_time):
        pass

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        pass

    # отпустить клавишу
    def on_key_release(self, key, modifiers):
        pass


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
