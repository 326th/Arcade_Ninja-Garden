import arcade
from camera import Camera
SCALE = 1.5
UNIT_SIZE = 32
SCREEN_WIDTH = UNIT_SIZE * (25)
SCREEN_HEIGHT = UNIT_SIZE * (19)
SCREEN_WIDTH = 32 * (25)
SCREEN_HEIGHT = 32 * (19)
SPIKE = ['images/spike/spike0000.png',
         'images/spike/spike0001.png',
         'images/spike/spike0002.png',
         'images/spike/spike0003.png']

STAND_NINJA = ['images/ninja/Idle0000.png',
               'images/ninja/Idle0001.png',
               'images/ninja/Idle0002.png',
               'images/ninja/Idle0003.png',
               'images/ninja/Idle0004.png',
               'images/ninja/Idle0005.png',
               'images/ninja/Idle0006.png',
               'images/ninja/Idle0007.png',
               'images/ninja/Idle_flip0000.png',
               'images/ninja/Idle_flip0001.png',
               'images/ninja/Idle_flip0002.png',
               'images/ninja/Idle_flip0003.png',
               'images/ninja/Idle_flip0004.png',
               'images/ninja/Idle_flip0005.png',
               'images/ninja/Idle_flip0006.png',
               'images/ninja/Idle_flip0007.png']

RUN_NINJA = ['images/ninja/run0000.png',
               'images/ninja/run0001.png',
               'images/ninja/run0002.png',
               'images/ninja/run0003.png',
               'images/ninja/run0004.png',
               'images/ninja/run0005.png',
               'images/ninja/run0006.png',
               'images/ninja/run0007.png',
               'images/ninja/run_flip0000.png',
               'images/ninja/run_flip0001.png',
               'images/ninja/run_flip0002.png',
               'images/ninja/run_flip0003.png',
               'images/ninja/run_flip0004.png',
               'images/ninja/run_flip0005.png',
               'images/ninja/run_flip0006.png',
               'images/ninja/run_flip0007.png']

JUMP_NINJA = ['images/ninja/jump_up0000.png',
               'images/ninja/jump_up0001.png',
               'images/ninja/jump_up0002.png',
               'images/ninja/jump_up_flip0000.png',
               'images/ninja/jump_up_flip0001.png',
               'images/ninja/jump_up_flip0002.png']

FALL_NINJA = ['images/ninja/fall_down0000.png',
               'images/ninja/fall_down0001.png',
               'images/ninja/fall_down_flip0000.png',
               'images/ninja/fall_down_flip0001.png']

STAND_ENEMY = ['images/s_enemy/s_enemy0000.png',
               'images/s_enemy/s_enemy0001.png',
               'images/s_enemy/s_enemy0002.png',
               'images/s_enemy/s_enemy0003.png']

WALK_ENEMY = ['images/enemy/enemy0000.png',
               'images/enemy/enemy0001.png',
               'images/enemy/enemy0002.png',
               'images/enemy/enemy0003.png',
               'images/enemy/enemy_flip0000.png',
               'images/enemy/enemy_flip0001.png',
               'images/enemy/enemy_flip0002.png',
               'images/enemy/enemy_flip0003.png']
#load sprite
class NinjaSprite:
    DELAY = 6
    RUN_DELAY = 4
    JUMP_DELAY = 2 #and fall
    def __init__(self,game):
        self.ninja = game.camera.world.player
        self.cycle = 0
        self.delay = 0
        self.run_delay = 0
        self.run_cycle = 0
        self.jump_delay = 0
        self.jump_cycle = 0
        self.fall_cycle = 0
    def draw(self,x,y):
        if self.ninja.vy > 0:
            self.right = int((self.ninja.right*int(len(JUMP_NINJA)))/2)
            self.ninja_sprite = arcade.Sprite(JUMP_NINJA[self.jump_cycle + self.right],scale = SCALE)
            self.ninja_sprite.set_position(self.ninja.x+x,self.ninja.y+y)
            self.ninja_sprite.draw()
            return
        if self.ninja.vy < 0:
            self.right = int((self.ninja.right*int(len(FALL_NINJA)))/2)
            self.ninja_sprite = arcade.Sprite(FALL_NINJA[self.fall_cycle + self.right],scale = SCALE)
            self.ninja_sprite.set_position(self.ninja.x+x,self.ninja.y+y)
            self.ninja_sprite.draw()
            return
        if self.ninja.vx !=0:
            self.right = int((self.ninja.right*int(len(RUN_NINJA)))/2)
            self.ninja_sprite = arcade.Sprite(RUN_NINJA[self.run_cycle + self.right],scale = SCALE)
            self.ninja_sprite.set_position(self.ninja.x+x,self.ninja.y+y)
            self.ninja_sprite.draw()
            return
        self.right = int((self.ninja.right*int(len(STAND_NINJA)))/2)
        self.ninja_sprite = arcade.Sprite(STAND_NINJA[self.cycle + self.right],scale = SCALE)
        self.ninja_sprite.set_position(self.ninja.x+x,self.ninja.y+y)
        self.ninja_sprite.draw()

    def update(self):
        if self.ninja.stop_charge > 0:
            return
        self.delay += 1
        self.run_delay += 1
        self.jump_delay += 1
        if self.delay == NinjaSprite.DELAY:
            self.delay = 0
            if self.cycle != int((len(STAND_NINJA)/2)-1):
                self.cycle += 1
            else:
                self.cycle = 0
        if self.run_delay == NinjaSprite.RUN_DELAY:
            self.run_delay = 0
            if self.run_cycle != int((len(RUN_NINJA)/2)-1):
                self.run_cycle += 1
            else:
                self.run_cycle = 0
        if self.jump_delay == NinjaSprite.JUMP_DELAY:
            self.jump_delay = 0
            if self.jump_cycle != int((len(JUMP_NINJA)/2)-1):
                self.jump_cycle += 1
            else:
                self.jump_cycle = 0

            if self.fall_cycle != int((len(FALL_NINJA)/2)-1):
                self.fall_cycle += 1
            else:
                self.fall_cycle = 0
        
class BlockSprite:
    def __init__(self,game):
        self.block = game.camera.world.block
        self.ground = game.camera.world.ground
        self.spike = game.camera.world.spike
        self.block_sprite = arcade.Sprite('images/block/block0000.png',scale = SCALE)
        self.ground_sprite = arcade.Sprite('images/dirt/Dirt0000.png',scale = SCALE)
    def draw(self,x,y):
        for block in self.block:
            self.block_sprite.set_position(block.x+x,block.y+y)
            self.block_sprite.draw()
        for ground in self.ground:
            self.ground_sprite.set_position(ground.x+x,ground.y+y)
            self.ground_sprite.draw()
        for spike in self.spike:
            spike_sprite = arcade.Sprite(SPIKE[spike.rotation],scale = SCALE)
            spike_sprite.set_position(spike.x+x,spike.y+y)
            spike_sprite.draw()
class S_Enemy:
    DELAY = 10
    def __init__(self,game):
        self.s_enemy = game.camera.world.s_enemy
        self.cycle = 0
        self.delay = 0

    def draw(self,x,y):
        self.enemy_sprite = arcade.Sprite(STAND_ENEMY[self.cycle],scale = SCALE)
        for s_enemy in self.s_enemy:
            self.enemy_sprite.set_position(s_enemy.x+x,s_enemy.y+y)
            self.enemy_sprite.draw()

    def update(self):
        self.delay += 1
        if self.delay == S_Enemy.DELAY:
            self.delay = 0
            if self.cycle != int(len(STAND_ENEMY)-1):
                self.cycle += 1
            else:
                self.cycle = 0    
class Enemy:
    DELAY = 6
    def __init__(self,game):
        self.enemy = game.camera.world.enemy
        self.cycle = 0
        self.delay = 0
 
    def draw(self,x,y):
        for enemy in self.enemy:
            self.face_right = int((enemy.face_right*int(len(WALK_ENEMY)))/2)
            if enemy.face_right == -1:
                self.face_right = 0
            self.enemy_sprite = arcade.Sprite(WALK_ENEMY[self.cycle + self.face_right],scale = SCALE)
            self.enemy_sprite.set_position(enemy.x + x,enemy.y + y)
            self.enemy_sprite.draw()

    def update(self):
        self.delay += 1
        if self.delay == Enemy.DELAY:
            self.delay = 0
            if self.cycle != int((len(WALK_ENEMY)/2)-1):
                self.cycle += 1
            else:
                self.cycle = 0
class NinjaWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)
 
        arcade.set_background_color(arcade.color.AZURE_MIST)
        self.camera = Camera(self,UNIT_SIZE*SCALE,SCALE)

        self.enemy = Enemy(self)
        self.s_enemy = S_Enemy(self)
        self.block = BlockSprite(self)
        self.ninja = NinjaSprite(self)

    def on_draw(self):
        arcade.start_render()
        self.camera.get_positon_displace()
        x,y = self.camera.displace_x,self.camera.displace_y
        self.block.draw(x,y)
        self.s_enemy.draw(x,y)
        self.enemy.draw(x,y)
        self.ninja.draw(x,y)
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
    
