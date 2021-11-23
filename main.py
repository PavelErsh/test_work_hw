import arcade
import random
# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 1200

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Шаблон"

class Rectangle(arcade.Sprite):
    def update(self):
        pass


class OurGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.rectangles = arcade.SpriteList()


    # начальные значения
    def setup(self):
        for i in range(20):
            rectange = Rectangle("square.png", 0.2)
            rectange.center_x = (50 * i+ 110) + 30
            rectange.center_y = SCREEN_HEIGHT / 2
            self.rectangles.append(rectange)

    # отрисовка объектов
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        self.rectangles.draw()

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
