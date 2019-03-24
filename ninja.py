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

STAND_ENEMY = ['images/s_enemy/s_enemy0000.png',
               'images/s_enemy/s_enemy0001.png',
               'images/s_enemy/s_enemy0002.png',
               'images/s_enemy/s_enemy0003.png']
#load sprite
class NinjaSprite:
    DELAY = 6
    def __init__(self):
        self.cycle = 0
        self.delay = 0
        self.ninja_sprite = arcade.Sprite(STAND_NINJA[self.cycle],scale = 2)
 
    def draw(self):
        self.ninja_sprite = arcade.Sprite(STAND_NINJA[self.cycle],scale = 2)
        self.ninja_sprite.set_position(192,128)
        self.ninja_sprite.draw()

    def update(self):
        self.delay += 1
        if self.delay == NinjaSprite.DELAY:
            self.delay = 0
            if self.cycle != 7:
                self.cycle += 1
            else:
                self.cycle = 0
        
class BlockSprite:
    def __init__(self):
        self.block_sprite = arcade.Sprite('images/block/block0000.png',scale = 2)
        self.ground_sprite = arcade.Sprite('images/dirt/Dirt0000.png',scale = 2)
    def draw(self,block_lst,ground_lst):
        for block in block_lst:
            self.block_sprite.set_position(block[0],block[1]) #replace with block.x,block.y
            self.block_sprite.draw()
        for ground in ground_lst:
            self.ground_sprite.set_position(ground[0],ground[1]) #replace with ground.x,ground.y
            self.ground_sprite.draw()

class Enemy:
    DELAY = 10
    def __init__(self):
        self.cycle = 0
        self.delay = 0
        self.enemy_sprite = arcade.Sprite(STAND_ENEMY[self.cycle],scale = 2)
 
    def draw(self):
        self.enemy_sprite = arcade.Sprite(STAND_ENEMY[self.cycle],scale = 2)
        self.enemy_sprite.set_position(64,128)
        self.enemy_sprite.draw()

    def update(self):
        self.delay += 1
        if self.delay == Enemy.DELAY:
            self.delay = 0
            if self.cycle != 3:
                self.cycle += 1
            else:
                self.cycle = 0    
            
class NinjaWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)

        arcade.set_background_color(arcade.color.WHITE)
#        self.camera = Camera(SCREEN_WIDTH,SCREEN_HEIGHT)
        
        self.ninja = NinjaSprite()
        self.block = BlockSprite()
        self.enemy = Enemy()
        
    def on_draw(self):
        arcade.start_render()

        self.ninja.draw()
        self.block.draw([(0,64),(64,64),(128,64),(192,64)],[(0,0),(64,0),(128,0),(192,0)])
        self.enemy.draw()
    def update(self, delta):
        self.ninja.update()
        self.enemy.update()
def main():
    window = NinjaWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__== '__main__':
    main()
