import arcade
#from camera import Camera
SCREEN_WIDTH = 32 * (25)
SCREEN_HEIGHT = 32 * (19)
STAND_NINJA = ['images/ninja/Idle0000.png',
               'images/ninja/Idle0001.png',
               'images/ninja/Idle0002.png',
               'images/ninja/Idle0003.png',
               'images/ninja/Idle0004.png',
               'images/ninja/Idle0005.png',
               'images/ninja/Idle0006.png',
               'images/ninja/Idle0007.png']
#load sprite
class NinjaSprite:
    DELAY = 6
    def __init__(self):
        self.cycle = 0
        self.delay = 0
        self.ninja_sprite = arcade.Sprite(STAND_NINJA[self.cycle],scale = 2)
 
    def draw(self):
        self.ninja_sprite = arcade.Sprite(STAND_NINJA[self.cycle],scale = 2)
        self.ninja_sprite.set_position(100,100)
        self.ninja_sprite.draw()

    def update(self):
        self.delay += 1
        if self.delay == NinjaSprite.DELAY:
            self.delay = 0
            if self.cycle != 7:
                self.cycle += 1
            else:
                self.cycle = 0
        
           
class NinjaWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)

        arcade.set_background_color(arcade.color.WHITE)
#        self.camera = Camera(SCREEN_WIDTH,SCREEN_HEIGHT)
        
        self.ninja_sprite = NinjaSprite()

        
    def on_draw(self):
        arcade.start_render()

        self.ninja_sprite.draw()
        
    def update(self, delta):
        self.ninja_sprite.update()
def main():
    window = NinjaWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__== '__main__':
    main()
