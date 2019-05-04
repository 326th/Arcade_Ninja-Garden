import arcade
import math
MID_X = 408
MID_Y = 300
BOSS_BODY = ['images/boss/boss_body1.png',
             'images/boss/boss_body2.png',
             'images/boss/boss_body3.png',
             'images/boss/boss_body4.png',
             'images/boss/boss_body3.png',
             'images/boss/boss_body2.png',
             'images/boss/boss_body1.png',]
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
        self.body = arcade.Sprite(BOSS_BODY[self.cycle%7])
        self.body.set_position(MID_X,MID_Y)
        self.top.set_position(MID_X + (math.sin(math.radians(self.top_angle)))*10,MID_Y + (math.cos(math.radians(self.top_angle))*20)+ 20)
        self.body.draw()
        self.top.draw()
    def update(self):
        self.top_angle += 6
        self.timer += 1
        if self.timer == 7:
            self.timer = 0
            self.cycle += 1
            print(self.cycle)
##    def random_attack_down(self):
##    def random_attack_left(self):
##    def random_attack_right(self):
##    def update(self):
##    def spawn(self):
##    def hurts(self,damage):
##    def die(self):
