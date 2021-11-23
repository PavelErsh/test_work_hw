import arcade
import random
# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 1200

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Шаблон"

class Rectangle(arcade.Sprite):
    def update(self):
        pass

class Text:
    pass

class OurGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.rectangles = arcade.SpriteList()
        self.text = Text()


    # начальные значения
    def setup(self):
        self.rand_numbers = []
        self.text.center_x = []
        self.text.center_y = []
        self.text.change_x = 0
        for i in range(20):
            rectange = Rectangle("square.png", 0.2)
            rectange.center_x = (50 * i+ 110) + 30
            self.text.center_x.append(rectange.center_x-6)
            rectange.center_y = SCREEN_HEIGHT / 2
            self.text.center_y.append(rectange.center_y-4)
            self.rectangles.append(rectange)

        for j in range(20):
            self.rand_numbers.append(random.randint(1, 10))
    # отрисовка объектов
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        self.rectangles.draw()
        for i in range(20):
            arcade.draw_text(f"{self.rand_numbers[i]}",self.text.center_x[i], self.text.center_y[i], arcade.color.BLACK, 20 )

    # логика
    def update(self, delta_time):
        pass
        #self.text.center_y += self.text.change_x

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        pass

    # отпустить клавишу
    def on_key_release(self, key, modifiers):
        pass


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
