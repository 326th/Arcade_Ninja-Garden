import arcade
from camera import Camera
SCALE = 1.5
UNIT_SIZE = 32
SCREEN_WIDTH = UNIT_SIZE * (25)
SCREEN_HEIGHT = UNIT_SIZE * (19)
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

WALK_ENEMY = ['images/enemy/enemy0000.png',
               'images/enemy/enemy0001.png',
               'images/enemy/enemy0002.png',
               'images/enemy/enemy0003.png']
#load sprite
class NinjaSprite:
    DELAY = 6
    def __init__(self):
        self.cycle = 0
        self.delay = 0
        self.ninja_sprite = arcade.Sprite(STAND_NINJA[self.cycle],scale = SCALE)
 
    def draw(self,x,y):
        self.ninja_sprite = arcade.Sprite(STAND_NINJA[self.cycle],scale = SCALE)
        self.ninja_sprite.set_position(x,y)
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
        self.block_sprite = arcade.Sprite('images/block/block0000.png',scale = SCALE)
        self.ground_sprite = arcade.Sprite('images/dirt/Dirt0000.png',scale = SCALE)
    def draw(self,block_lst,ground_lst,displace_x,displace_y):
        for block in block_lst:
            self.block_sprite.set_position(block.x+displace_x,block.y+displace_y)
            self.block_sprite.draw()
        for ground in ground_lst:
            self.ground_sprite.set_position(ground.x+displace_x,ground.y+displace_y)
            self.ground_sprite.draw()

class S_Enemy:
    DELAY = 10
    def __init__(self):
        self.cycle = 0
        self.delay = 0
        self.enemy_sprite = arcade.Sprite(STAND_ENEMY[self.cycle],scale = SCALE)
 
    def draw(self,x,y):
        self.enemy_sprite = arcade.Sprite(STAND_ENEMY[self.cycle],scale = SCALE)
        self.enemy_sprite.set_position(x,y)
        self.enemy_sprite.draw()

    def update(self):
        self.delay += 1
        if self.delay == S_Enemy.DELAY:
            self.delay = 0
            if self.cycle != 3:
                self.cycle += 1
            else:
                self.cycle = 0    
class Enemy:
    DELAY = 10
    def __init__(self):
        self.cycle = 0
        self.delay = 0
        self.enemy_sprite = arcade.Sprite(WALK_ENEMY[self.cycle],scale = SCALE)
 
    def draw(self,x,y):
        self.enemy_sprite = arcade.Sprite(WALK_ENEMY[self.cycle],scale = SCALE)
        self.enemy_sprite.set_position(x,y)
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
        self.camera = Camera(UNIT_SIZE*SCALE,SCALE)

        self.enemy = Enemy()
        self.s_enemy = S_Enemy()
        self.block = BlockSprite()
        self.ninja = NinjaSprite()

    def on_draw(self):
        arcade.start_render()
        self.camera.get_positon_displace()
        x,y = self.camera.displace_x,self.camera.displace_y
        self.ninja.draw(self.camera.world.player.x+x,self.camera.world.player.y+y)
        self.block.draw(self.camera.world.block,self.camera.world.ground,x,y)
        for still_enemy in self.camera.world.s_enemy:
            self.s_enemy.draw(still_enemy.x+x,still_enemy.y+y)
        for walking_enemy in self.camera.world.enemy:
            self.enemy.draw(walking_enemy.x+x,walking_enemy.y+y)
    def update(self, delta):
        self.ninja.update()
        self.s_enemy.update()
        self.enemy.update()
        self.camera.update(delta)
    def on_key_press(self,key,key_modifiers):
        self.camera.on_key_press(key,key_modifiers)
    def on_key_release(self,key,key_modifiers):
        self.camera.on_key_release(key,key_modifiers)
def main():
    window = NinjaWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
if __name__== '__main__':
    main()
    
