import arcade
import math
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
class Boss:
    def __init__(self,world):
        self.body = 0
        self.world = world
        self.timer = 100
        self.top_angle = 0
        self.cycle = 0
        self.top = arcade.Sprite('images/boss/boss_top.png')
        self.timer = 0
    def draw(self):
        self.body = arcade.Sprite(BOSS_BODY[self.cycle%5])
        self.body.set_position(MID_X,MID_Y)
        self.left = arcade.Sprite(BOSS_LEFT[self.cycle%10])
        self.left.set_position(MID_X,MID_Y)
        self.right = arcade.Sprite(BOSS_RIGHT[self.cycle%4])
        self.right.set_position(MID_X,MID_Y)
        self.down = arcade.Sprite(BOSS_DOWN[self.cycle%5])
        self.down.set_position(MID_X,MID_Y)
        self.top.set_position(MID_X + (math.sin(math.radians(self.top_angle)))*2+1,MID_Y + (math.cos(math.radians(self.top_angle))*10)+ 10)
        self.down.draw()
        self.body.draw()
        self.left.draw()
        self.right.draw()
        self.top.draw()
    def update(self):
        self.top_angle += 4
        if self.top_angle == 1440:
            self.top_angle = 0
        self.timer += 1
        if self.timer == 15:
            self.timer = 0
            self.cycle += 1
##    def random_attack_down(self):
##    def random_attack_left(self):
##    def random_attack_right(self):
##    def update(self):
##    def spawn(self):
##    def hurts(self,damage):
##    def die(self):
