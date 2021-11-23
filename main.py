import arcade
import random
# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 1400

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
            self.margin = 30
            self.position = 400
            rectange = Rectangle("square.png", 0.1)
            rectange.center_x = self.margin * i + self.position
            self.text.center_x.append(rectange.center_x-6)
            rectange.center_y = 540
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
            arcade.draw_text(f"{self.rand_numbers[i]}",self.text.center_x[i], self.text.center_y[i], arcade.color.BLACK, 10 )

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
