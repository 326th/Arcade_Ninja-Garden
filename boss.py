import arcade
import math
import random
MID_X = 408
MID_Y = 300
warn_pos_ver = list(range(13))
warn_pos_ver = list(map(lambda x: x*48 + 24, warn_pos_ver))
warn_pos_ho = list(range(17))
warn_pos_ho = list(map(lambda x: x*48 + 24, warn_pos_ho))
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
RIGHT_SPIKE = ['images/boss/boss_right_spike6.png',
             'images/boss/boss_right_spike5.png',
             'images/boss/boss_right_spike4.png',
             'images/boss/boss_right_spike3.png',
             'images/boss/boss_right_spike2.png',
             'images/boss/boss_right_spike1.png']
LEFT_SPIKE = ['images/boss/boss_left_spike6.png',
             'images/boss/boss_left_spike5.png',
             'images/boss/boss_left_spike4.png',
             'images/boss/boss_left_spike3.png',
             'images/boss/boss_left_spike2.png',
             'images/boss/boss_left_spike1.png']
class Boss:
    def __init__(self,world):
        self.body = 0
        self.world = world
        self.survive = 100
        self.top_angle = 0
        self.cycle = 0
        self.top = arcade.Sprite('images/boss/boss_top.png')
        self.timer = 0
        self.down_attack = 0
        self.spike_x = 0
        self.spike_ver = 0
        self.left_attack = 0
        self.right_attack = 0
        self.spike_y = 0
        self.spike_ho_left = 0
        self.spike_ho_right = 0
        self.enemy_delay = 0
        self.enemy_x = 0
        self.enemy_timer = 0
        self.warn = arcade.Sprite('images/boss/warning.png',scale = 1.5)
    def draw(self):
        self.body = arcade.Sprite(BOSS_BODY[self.cycle%5])
        self.left = arcade.Sprite(BOSS_LEFT[self.cycle%10])
        self.right = arcade.Sprite(BOSS_RIGHT[self.cycle%4])
        self.down = arcade.Sprite(BOSS_DOWN[self.cycle%5])
        if self.down_attack > 0:
            self.down = arcade.Sprite(DOWN_ATTACK[(self.down_attack%6)-1])
        if self.spike_ver > 0:
            self.down = arcade.Sprite(DOWN_SPIKE[(self.spike_ver//10)])
        if self.spike_ho_left > 0:
            self.left = arcade.Sprite(LEFT_SPIKE[(self.spike_ho_left//10)])
        if self.spike_ho_right > 0:
            self.right = arcade.Sprite(RIGHT_SPIKE[(self.spike_ho_right//10)])
        self.body.set_position(MID_X,MID_Y)
        self.left.set_position(MID_X,MID_Y)
        self.right.set_position(MID_X,MID_Y)
        self.down.set_position(MID_X,MID_Y)
        if self.spike_ver > 0:
            self.down.set_position(self.spike_x,MID_Y+ 48)
        if self.spike_ho_left > 0:
            self.left.set_position(MID_X+48,self.spike_y)
        if self.spike_ho_right > 0:
            self.right.set_position(MID_X-48,self.spike_y)
        self.top.set_position(MID_X + (math.sin(math.radians(self.top_angle)))*2+1,MID_Y + (math.cos(math.radians(self.top_angle))*10)+ 10)

        self.down.draw()
        self.body.draw()
        self.left.draw()
        self.right.draw()
        self.top.draw()
        arcade.draw_text(f'Time:{math.ceil(self.survive)}',68,580,arcade.color.BLACK,20)
        if self.spike_ver > 0:
            self.down.draw()
            for y in warn_pos_ver:
                self.warn.set_position(self.spike_x,y)
                self.warn.draw()
        if self.spike_ho_left > 0:
            self.left.draw()
            for x in warn_pos_ho:
                self.warn.set_position(x,self.spike_y)
                self.warn.draw()
        if self.spike_ho_right > 0:
            self.right.draw()
            for x in warn_pos_ho:
                self.warn.set_position(x,self.spike_y)
                self.warn.draw()
        if self.enemy_delay > 0:
            self.warn.set_position(self.enemy_x,72)
            self.warn.draw()
    def update(self):
        if self.enemy_delay > 0:
            self.enemy_delay -=1
            if self.enemy_delay == 0:
                self.world.create_s_enemy(self.enemy_x,72)
        self.enemy_timer += 1
        if self.enemy_timer == 16:
            self.enemy_timer = 0
            self.spawn()
        if self.spike_ver > 0:
            self.tracking_x()
            self.spike_ver -= 1
        if self.spike_ho_left > 0:
            self.tracking_y()
            self.spike_ho_left -= 1
        if self.spike_ho_right > 0:
            self.tracking_y()
            self.spike_ho_right -= 1
        self.top_angle += 4
        if self.top_angle == 1440:
            self.top_angle = 0
        self.timer += 1
        if self.timer == 5:
            if self.down_attack > 0:
                self.down_attack -= 1
            if self.left_attack > 0:
                self.left_attack -= 1
            if self.right_attack > 0:
                self.right_attack -= 1
        if self.timer == 10:
            self.survive -= 0.5
            self.timer = 0
            self.cycle += 1
            if self.cycle%5 == 4:
                self.random_attack_down()
                a = random.randint(0,1)
                if a:
                    self.random_attack_left()
                if not a:
                    self.random_attack_right()
            if self.down_attack > 1:
                self.down_attack -= 1
                if self.down_attack in [1,2]:
                    self.spike_ver = 59
                    self.spike_x = self.world.player.x
            if self.left_attack > 1:
                self.left_attack -= 1
                if self.left_attack in [1,2]:
                    self.spike_ho_left = 59
                    self.spike_y = self.world.player.y
            if self.right_attack > 1:
                self.right_attack -= 1
                if self.right_attack in [1,2]:
                    self.spike_ho_right = 59
                    self.spike_y = self.world.player.y
    def random_attack_down(self):
        if random.randint(0,4) == 0:
            if self.down_attack == 0 and self.spike_ver == 0:
                self.down_attack = 7
    def tracking_x(self):
        if self.spike_x == self.world.player.x:
            return
        self.spike_x += int((self.world.player.x-self.spike_x)/abs(self.world.player.x-self.spike_x)*2)
    def random_attack_left(self):
        if random.randint(0,6) == 0:
            if self.left_attack == 0 and self.spike_ho_left == 0 and self.spike_ho_right == 0 and self.right_attack == 0:
                self.left_attack = 7
    def random_attack_right(self):
        if random.randint(0,6) == 0:
            if self.left_attack == 0 and self.spike_ho_right == 0 and self.spike_ho_left == 0 and self.right_attack == 0:
                self.right_attack = 7
    def tracking_y(self):
        if self.spike_y == self.world.player.y:
            return
        self.spike_y += int((self.world.player.y-self.spike_y)/abs(self.world.player.y-self.spike_y)*2)    
    def spawn(self):
        if len(self.world.s_enemy) < 1 and self.enemy_delay == 0:

            if random.randint(0,9) == 0:
                self.enemy_delay = 60
                self.enemy_x = random.randint(72,528)
##    def hurts(self,damage):
##    def die(self):
##        if self.survive == 0:
##            dead animation
