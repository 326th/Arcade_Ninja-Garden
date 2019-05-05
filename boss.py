import arcade
import math
import random
MID_X = 408
MID_Y = 300
BOSS_BODY = ['images/boss/boss_body1.png',
             'images/boss/boss_body2.png',
             'images/boss/boss_body3.png',
             'images/boss/boss_body4.png',
             'images/boss/boss_body3.png']
BOSS_RIGHT = ['images/boss/boss_right1.png',
             'images/boss/boss_right2.png',
             'images/boss/boss_right3.png',
             'images/boss/boss_right2.png']
BOSS_LEFT = ['images/boss/boss_left1.png',
             'images/boss/boss_left2.png',
             'images/boss/boss_left3.png',
             'images/boss/boss_left4.png',
             'images/boss/boss_left5.png',
             'images/boss/boss_left6.png',
             'images/boss/boss_left5.png',
             'images/boss/boss_left4.png',
             'images/boss/boss_left3.png',
             'images/boss/boss_left2.png']
BOSS_DOWN = ['images/boss/boss_down1.png',
             'images/boss/boss_down2.png',
             'images/boss/boss_down3.png',
             'images/boss/boss_down4.png',
             'images/boss/boss_down5.png']
DOWN_ATTACK = ['images/boss/boss_down_attack4.png',
             'images/boss/boss_down_attack4.png',
             'images/boss/boss_down_attack4.png',
             'images/boss/boss_down_attack3.png',
             'images/boss/boss_down_attack2.png',
             'images/boss/boss_down_attack1.png']
DOWN_SPIKE = ['images/boss/boss_down_spike6.png',
             'images/boss/boss_down_spike5.png',
             'images/boss/boss_down_spike4.png',
             'images/boss/boss_down_spike3.png',
             'images/boss/boss_down_spike2.png',
             'images/boss/boss_down_spike1.png']
class Boss:
    def __init__(self,world):
        self.body = 0
        self.world = world
        self.timer = 100
        self.top_angle = 0
        self.cycle = 0
        self.top = arcade.Sprite('images/boss/boss_top.png')
        self.timer = 0
        self.down_attack = 0
        self.spike_x = 0
        self.spike = 0
    def draw(self):
        self.body = arcade.Sprite(BOSS_BODY[self.cycle%5])
        self.left = arcade.Sprite(BOSS_LEFT[self.cycle%10])
        self.right = arcade.Sprite(BOSS_RIGHT[self.cycle%4])
        self.down = arcade.Sprite(BOSS_DOWN[self.cycle%5])
        if self.down_attack > 0:
            self.down = arcade.Sprite(DOWN_ATTACK[(self.down_attack%6)-1])
        if self.spike > 0:
            self.down = arcade.Sprite(DOWN_SPIKE[(self.spike//5)-1])
        self.body.set_position(MID_X,MID_Y)
        self.left.set_position(MID_X,MID_Y)
        self.right.set_position(MID_X,MID_Y)
        self.down.set_position(MID_X,MID_Y)
        if self.spike > 0:
            self.down.set_position(self.spike_x,MID_Y)
        self.top.set_position(MID_X + (math.sin(math.radians(self.top_angle)))*2+1,MID_Y + (math.cos(math.radians(self.top_angle))*10)+ 10)

        self.down.draw()
        self.body.draw()
        self.left.draw()
        self.right.draw()
        self.top.draw()
        if self.spike > 0:
            self.down.draw()
    def update(self):
        if self.spike > 0:
            self.tracking_x()
            self.spike -= 1
        self.top_angle += 4
        if self.top_angle == 1440:
            self.top_angle = 0
        self.timer += 1
        if self.timer == 5:
            if self.down_attack > 0:
                self.down_attack -= 1
        if self.timer == 10:
            self.timer = 0
            self.cycle += 1
            if self.cycle%4 == 0:
                self.random_attack_down()
            if self.down_attack > 1:
                self.down_attack -= 1
                if self.down_attack in [1,2]:
                    self.spike = 29
    def random_attack_down(self):
        if random.randint(0,5) == 0:
            if self.down_attack == 0 and self.spike == 0:
                self.down_attack = 7
    def tracking_x(self):
        self.spike_x = self.world.player.x
##    def random_attack_left(self):
##    def random_attack_right(self):
##    def update(self):
##    def spawn(self):
##    def hurts(self,damage):
##    def die(self):
