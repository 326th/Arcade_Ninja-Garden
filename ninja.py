import arcade
from camera import Camera
SCREEN_WIDTH = 32 * (25)
SCREEN_HEIGHT = 32 * (19)

#draw sprite

class NinjaWindow(arcade.window):
    def __init__(self,width,height):
        super().__init__(width,height)

        arcade.set_background_color(arcade.color.WHITE)
        self.camera = Camera(SCREEN_WIDTH,SCREEN_HEIGHT)
    def on_draw(self):
        arcade.start_render()

def main():
    window = NinjaWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__== '__main__':
    main()
