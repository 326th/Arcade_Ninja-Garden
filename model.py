import arcade.key
import world_load
from collision_detection import new_pos_x, new_pos_y
class Player:
    MAX_X = 6
    MAX_Y = 20
    GRAVITY = -0.5
    JUMP_SPEED = 12
    DASH_ACC = 1
    FRICTION = MAX_X/5
    MAX_STOP_CHARGE = 20
    def __init__(self,world,x,y):
        self.jump_charge = 0
        self.stop_charge = Player.MAX_STOP_CHARGE
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.right = 0
        Player.GRAVITY = (Player.GRAVITY * self.world.scale)//1
        Player.JUMP_SPEED = (Player.JUMP_SPEED * self.world.scale)//1
        Player.DASH_ACC = (Player.DASH_ACC * self.world.scale)//1
        Player.FRICTION = (Player.FRICTION * self.world.scale)//1
        Player.MAX_X = (Player.MAX_X * self.world.scale)//1
        Player.MAX_Y = (Player.MAX_Y * self.world.scale)//1
    def update(self,delta):
        if self.stop_charge >0:
            self.stop_charge -= 1
            return
        on_air = False
        g_spike = self.world.get_ground_at_player_same_x()
        for g in self.world.ground + self.world.block:
            if self.y == g.y + self.world.unit_size:
                if self.jump_charge == 0:
                    self.jump_charge = 2
                on_air = True
        if on_air:
            if self.jump_charge == 2:
                    self.jump_charge = 1
        if self.world.hold_RIGHT == True:
            if self.vx <0:
                self.vx = -self.vx
            self.vx += Player.DASH_ACC
        elif self.world.hold_LEFT == True:
            if self.vx >0:
                self.vx = -self.vx
            self.vx -= Player.DASH_ACC
        else:
            if self.vx >0:
                self.vx -= Player.FRICTION
                if self.vx<0:
                    self.vx = 0
            else:
                self.vx += Player.FRICTION
                if self.vx>0:
                    self.vx = 0
        self.vy += Player.GRAVITY
        if self.vx > Player.MAX_X:
            self.vx = Player.MAX_X
        elif self.vx < -Player.MAX_X:
            self.vx = -Player.MAX_X
        if self.vy > Player.MAX_Y:
            self.vy = Player.MAX_Y
        elif self.vy < -Player.MAX_Y:
            self.vy = -Player.MAX_Y
        self.x, stop_x =  new_pos_x(self,self.world.get_ground_at_player_same_y(),self.world.unit_size)
        if stop_x:
            self.vx = 0
        self.y, stop_y =  new_pos_y(self,self.world.get_ground_at_player_same_x(),self.world.unit_size)
        if stop_y:
            self.vy = 0
        if self.vx >0:
            self.right = 0
        if self.vx<0:
            self.right = 1
    def jump(self):
        if self.jump_charge > 0:
            self.jump_charge -= 1
            self.vy = Player.JUMP_SPEED
    def slash(self,direction):
        if self.stop_charge >0:
            return
        DASH_RANGE = (4*self.world.unit_size) + 20
        if direction == [0,1]:
            ground = self.world.get_only_ground_at_player_same_x()
            new_y = self.y + DASH_RANGE
            for g in ground:
                if (self.y < g.y < self.y + DASH_RANGE):
                    if g.y < new_y:
                        new_y = g.y
            self.stop_charge = Player.MAX_STOP_CHARGE
            killable = self.world.enemy + self.world.s_enemy + self.world.block
            for target in killable:
                if (target.x - (self.world.unit_size/2) < self.x < target.x + (self.world.unit_size/2)):
                    if (self.y - ((self.world.unit_size/2)//1) < target.y < new_y - ((self.world.unit_size/2)//1)):
                       target.die()
            self.y = new_y - self.world.unit_size
        if direction == [0,-1]:
            ground = self.world.get_only_ground_at_player_same_x()
            new_y = self.y - DASH_RANGE
            for g in ground:
                if (self.y > g.y > self.y - DASH_RANGE):
                    if g.y > new_y:
                        new_y = g.y
            self.stop_charge = Player.MAX_STOP_CHARGE
            killable = self.world.enemy + self.world.s_enemy + self.world.block
            for target in killable:
                if (target.x - (self.world.unit_size/2) < self.x < target.x + (self.world.unit_size/2)):
                    if (self.y + ((self.world.unit_size/2)//1) > target.y > new_y + ((self.world.unit_size/2)//1)):
                       target.die()
            self.y = new_y + self.world.unit_size
        if direction == [1,0]:
            self.right = 0
            ground = self.world.get_only_ground_at_player_same_y()
            new_x = self.x + DASH_RANGE
            for g in ground:
                if (self.x < g.x < self.x + DASH_RANGE):
                    if g.x < new_x:
                        new_x = g.x
            self.stop_charge = Player.MAX_STOP_CHARGE
            killable = self.world.enemy + self.world.s_enemy + self.world.block
            for target in killable:
                if (target.y - (self.world.unit_size/2) < self.y < target.y + (self.world.unit_size/2)):
                    if (self.x - ((self.world.unit_size/2)//1) < target.x < new_x - ((self.world.unit_size/2)//1)):
                       target.die()
            self.x = new_x - self.world.unit_size
        if direction == [-1,0]:
            self.right = 1
            ground = self.world.get_only_ground_at_player_same_y()
            new_x = self.x - DASH_RANGE
            for g in ground:
                if (self.x > g.x > self.x - DASH_RANGE):
                    if g.x > new_x:
                        new_x = g.x
            self.stop_charge = Player.MAX_STOP_CHARGE
            killable = self.world.enemy + self.world.s_enemy + self.world.block
            for target in killable:
                if (target.y - (self.world.unit_size/2) < self.y < target.y + (self.world.unit_size/2)):
                    if (self.x + ((self.world.unit_size/2)//1) > target.x > new_x + ((self.world.unit_size/2)//1)):
                       target.die()
            self.x = new_x + self.world.unit_size
        self.vx = 0
        self.vy = 0
    def die(self):
        self.world.load(self.world.directory)
class S_Enemy:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
    def die(self):
        self.world.s_enemy.remove(self)
class Enemy:
    MOVE_SPEED = 3
    def __init__(self,world,start_x,end_x,y):
        self.world = world
        self.x = start_x
        self.start_x = start_x
        self.end_x = end_x
        self.y = y
        self.face_right = -1 #1 right, -1 left
    def die(self):
        self.world.enemy.remove(self)
    def update(self,delta):
        if self.face_right == 1 and self.x >= self.end_x:
            self.face_right = -1
        if self.face_right == -1 and self.x <= self.start_x:
            self.face_right = 1
        self.x += Enemy.MOVE_SPEED * self.face_right
class Ground:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
class Block:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
    def die(self):
        self.world.block.remove(self)
class Spike:
    def __init__(self,world,x,y,rotation):
        self.world = world
        self.x = x
        self.y = y
        self.rotation = rotation
##class Warp:
##    def __init__(self,world,x,y,width,heigth,mapdirectory):
##        self.world = world
##        self.x = range(x,x + width)
##        self.y = range(y,y + height)
##        self.directory = mapdirectory
##    def check_player_in(self):
##        #check if player in it
##    def warp(self):
##        self.world.warp(self.directory)
class World:
    def __init__(self,camera,unit_size,scale):
        self.camera = camera
        self.scale = scale
        self.unit_size = unit_size
        self.block = []
        self.ground = []
        self.s_enemy = []
        self.enemy = []
        self.spike = []
        self.player = None
        self.hold_LEFT = False
        self.hold_RIGHT = False
    def update(self,delta):
        self.player.update(delta)
        for enemy in self.enemy:
            enemy.update(delta)
##    def warp(self,directory):
##        #stop update world
##        #loading screen
##        #clear everything in world then load new world
##        #remove loading screen
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.hold_LEFT = True
        if key == arcade.key.RIGHT:
            self.hold_RIGHT = True
        if key == arcade.key.UP:
            self.player.jump()
        if key == arcade.key.W:
            self.player.slash([0,1])
        if key == arcade.key.S:
            self.player.slash([0,-1])
        if key == arcade.key.D:
            self.player.slash([1,0])
        if key == arcade.key.A:
            self.player.slash([-1,0])
        if key == arcade.key.E:
            self.player.die()
    def on_key_release(self,key,key_modifiers):
        if key == arcade.key.LEFT:
            self.hold_LEFT = False
        if key == arcade.key.RIGHT:
            self.hold_RIGHT = False
    def get_only_ground_at_player_same_y(self):
        g = []
        for s in self.spike:
            if (s.y - (self.unit_size) < self.player.y < s.y + (self.unit_size)):
                if s.rotation in (0,2):
                    g.append(s)
        for ground in self.ground:
            if (ground.y - (self.unit_size) < self.player.y < ground.y + (self.unit_size)):
                g.append(ground)
        return g
    def get_only_ground_at_player_same_x(self):
        g = []
        for s in self.spike:
            if (s.x - (self.unit_size) < self.player.x < s.x + (self.unit_size)):
                if s.rotation in (1,3):
                    g.append(s)
        for ground in self.ground:
            if (ground.x - (self.unit_size) < self.player.x < ground.x + (self.unit_size)):
                g.append(ground)
        return g
    def get_ground_at_player_same_y(self):
        g = []
        for s in self.spike:
            if (s.y - (self.unit_size) < self.player.y < s.y + (self.unit_size)):
                if s.rotation in (0,2):
                    g.append(s)
        for ground in self.ground+self.block:
            if (ground.y - (self.unit_size) < self.player.y < ground.y + (self.unit_size)):
                g.append(ground)
        return g
    def get_ground_at_player_same_x(self):
        g = []
        for s in self.spike:
            if (s.x - (self.unit_size) < self.player.x < s.x + (self.unit_size)):
                if s.rotation in (1,3):
                    g.append(s)
        for ground in self.ground+self.block:
            if (ground.x - (self.unit_size) < self.player.x < ground.x + (self.unit_size)):
                g.append(ground)
        return g
    def create_player(self,x,y):
        self.player = Player(self,x,y)
    def create_block(self,x,y):
        self.block.append(Block(self,x,y))
    def create_ground(self,x,y):
        self.ground.append(Ground(self,x,y))
    def create_s_enemy(self,x,y):
        self.s_enemy.append(S_Enemy(self,x,y))
    def create_enemy(self,start_x,end_x,y):
        self.enemy.append(Enemy(self,start_x,end_x,y))
    def create_spike(self,x,y,angle):
        self.spike.append(Spike(self,x,y,angle))
    def set_current_directory(self,directory):
        self.directory = directory
    def player_pos(self,x,y):
        self.player.jump_charge = 0
        self.player.stop_charge = Player.MAX_STOP_CHARGE
        self.player.x = x
        self.player.y = y
        self.player.vx = 0
        self.player.vy = 0
        self.player.right = 0
    def enemy_pos(self,pos_lst):
        if len(self.enemy) > len(pos_lst):
            self.enemy = self.enemy[:len(pos_lst)]
        need_to_create = len(pos_lst) - len(self.enemy)
        for times in range(need_to_create):
            self.create_enemy(0,0,0)
        for pos in range(len(self.enemy)):
            self.enemy[pos].x = pos_lst[pos][0]
            self.enemy[pos].start_x = pos_lst[pos][0]
            self.enemy[pos].end_x = pos_lst[pos][1]
            self.enemy[pos].y = pos_lst[pos][2]
            self.enemy[pos].face_right = -1
    def s_enemy_pos(self,pos_lst):
        if len(self.s_enemy) > len(pos_lst):
            self.s_enemy = self.s_enemy[:len(pos_lst)]
        need_to_create = len(pos_lst) - len(self.s_enemy)
        for times in range(need_to_create):
            self.create_s_enemy(0,0)
        for pos in range(len(self.s_enemy)):
            self.s_enemy[pos].x = pos_lst[pos][0]
            self.s_enemy[pos].y = pos_lst[pos][1]
    def ground_pos(self,pos_lst):
        if len(self.ground) > len(pos_lst):
            self.ground = self.ground[:len(pos_lst)]
        need_to_create = len(pos_lst) - len(self.ground)
        for times in range(need_to_create):
            self.create_ground(0,0)
        for pos in range(len(self.ground)):
            self.ground[pos].x = pos_lst[pos][0]
            self.ground[pos].y = pos_lst[pos][1]
    def block_pos(self,pos_lst):
        if len(self.block) > len(pos_lst):
            self.block = self.block[:len(pos_lst)]
        need_to_create = len(pos_lst) - len(self.block)
        for times in range(need_to_create):
            self.create_block(0,0)
        for pos in range(len(self.block)):
            self.block[pos].x = pos_lst[pos][0]
            self.block[pos].y = pos_lst[pos][1]
    def spike_pos(self,pos_lst):
        if len(self.spike) > len(pos_lst):
            self.spike = self.spike[:len(pos_lst)]
        need_to_create = len(pos_lst) - len(self.spike)
        for times in range(need_to_create):
            self.create_spike(0,0)
        for pos in range(len(self.spike)):
            self.spike[pos].x = pos_lst[pos][0]
            self.spike[pos].y = pos_lst[pos][1]
            self.spike[pos].rotation = pos_lst[pos][2]
    def load(self,directory):
        world_load.set_up(self,directory)
