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
    MAX_STOP_CHARGE = 5
    def __init__(self,world,x,y):
        self.jump_charge = 0
        self.stop_charge = 0
        self.dash_charge = 0
        self.world = world
        self.x = x
        self.y = y
        self.target_x = 0
        self.target_y = 0
        self.vx = 0
        self.vy = 0
        self.right = 0
        Player.GRAVITY = (Player.GRAVITY * self.world.scale)//1
        Player.JUMP_SPEED = (Player.JUMP_SPEED * self.world.scale)//1
        Player.DASH_ACC = (Player.DASH_ACC * self.world.scale)//1
        Player.FRICTION = (Player.FRICTION * self.world.scale)//1
        Player.MAX_X = (Player.MAX_X * self.world.scale)//1
        Player.MAX_Y = (Player.MAX_Y * self.world.scale)//1
        self.last_dir = 0
    def update(self,delta):
        
        if self.stop_charge >0:
            if self.target_x != self.x:
                self.x += (self.target_x - self.x)/self.stop_charge
            if self.target_y != self.y:
                self.y += (self.target_y - self.y)/self.stop_charge
            self.stop_charge -= 1
            return
        on_air = False
        g_spike = self.world.get_ground_at_player_same_x()
        for g in self.world.ground + self.world.block:
            if self.y == g.y + self.world.unit_size:
                if g.x - self.world.unit_size/2 < self.x <g.x + self.world.unit_size/2: 
                    self.jump_charge = 2
                    self.dash_charge = 1
                    on_air = True
        if on_air:
            if self.jump_charge == 2:
                    self.jump_charge = 1
        if self.world.hold_RIGHT and self.world.hold_LEFT:
            if self.last_dir == 1:
                if self.vx >0:
                    self.vx = -self.vx
                self.vx -= Player.DASH_ACC
            elif self.last_dir == -1:
                if self.vx <0:
                    self.vx = -self.vx
                self.vx += Player.DASH_ACC
        elif self.world.hold_RIGHT:
            if self.vx <0:
                self.vx = -self.vx
            self.vx += Player.DASH_ACC
            self.last_dir = 1
        elif self.world.hold_LEFT:
            if self.vx >0:
                self.vx = -self.vx
            self.vx -= Player.DASH_ACC
            self.last_dir = -1
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
        self.y, stop_y =  new_pos_y(self,self.world.get_ground_at_player_same_x(),self.world.unit_size)
        self.detect_spike()
        if stop_x:
            self.vx = 0
        if stop_y:
            self.vy = 0
        if self.vx >0:
            self.right = 0
        if self.vx<0:
            self.right = 1
        self.detect_death()
    def jump(self):
        if self.stop_charge >0:
            return
        if self.jump_charge > 0:
            self.jump_charge -= 1
            self.vy = Player.JUMP_SPEED
    def slash(self,direction):
        if self.stop_charge >0:
            return
        if not self.dash_charge:
            return
        self.dash_charge = 0
        DASH_RANGE = (4*self.world.unit_size) + 20
        if direction == [0,1]:
            ground = self.world.get_only_ground_at_player_same_x()
            new_y = self.y + DASH_RANGE
            for g in ground:
                if (self.y < g.y < self.y + DASH_RANGE):
                    if g.y < new_y:
                        new_y = g.y
            killable = self.world.enemy + self.world.s_enemy + self.world.block
            for target in killable:
                if (target.x - (self.world.unit_size/2) < self.x < target.x + (self.world.unit_size/2)):
                    if (self.y - ((self.world.unit_size/2)//1) < target.y < new_y ):
                       target.die()
            self.target_y = new_y - self.world.unit_size
            self.target_x = self.x
        if direction == [0,-1]:
            ground = self.world.get_only_ground_at_player_same_x()
            new_y = self.y - DASH_RANGE
            for g in ground:
                if (self.y > g.y > self.y - DASH_RANGE):
                    if g.y > new_y:
                        new_y = g.y
            killable = self.world.enemy + self.world.s_enemy + self.world.block
            for target in killable:
                if (target.x - (self.world.unit_size/2) < self.x < target.x + (self.world.unit_size/2)):
                    if (self.y + ((self.world.unit_size/2)//1) > target.y > new_y ):
                       target.die()
            self.target_y = new_y + self.world.unit_size
            self.target_x = self.x
        if direction == [1,0]:
            self.right = 0
            ground = self.world.get_only_ground_at_player_same_y()
            new_x = self.x + DASH_RANGE
            for g in ground:
                if (self.x < g.x < self.x + DASH_RANGE):
                    if g.x < new_x:
                        new_x = g.x
            killable = self.world.enemy + self.world.s_enemy + self.world.block
            for target in killable:
                if (target.y - (self.world.unit_size/2) < self.y < target.y + (self.world.unit_size/2)):
                    if (self.x - ((self.world.unit_size/2)//1) < target.x < new_x ):
                       target.die()
            self.target_x = new_x - self.world.unit_size
            self.target_y = self.y
        if direction == [-1,0]:
            self.right = 1
            ground = self.world.get_only_ground_at_player_same_y()
            new_x = self.x - DASH_RANGE
            for g in ground:
                if (self.x > g.x > self.x - DASH_RANGE):
                    if g.x > new_x:
                        new_x = g.x
            killable = self.world.enemy + self.world.s_enemy + self.world.block
            for target in killable:
                if (target.y - (self.world.unit_size/2) < self.y < target.y + (self.world.unit_size/2)):
                    if (self.x + ((self.world.unit_size/2)//1) > target.x > new_x ):
                       target.die()
            self.target_x = new_x + self.world.unit_size
            self.target_y = self.y
        self.stop_charge = Player.MAX_STOP_CHARGE
        self.vx = 0
        self.vy = 0
    def die(self):
        self.world.load(self.world.directory)
    def detect_death(self):
        all_enemy = self.world.enemy + self.world.s_enemy
        for enemy in all_enemy:
            if enemy.y - int(self.world.unit_size*3/8) <= self.y <= enemy.y + int(self.world.unit_size*3/8):
                if enemy.x - int(self.world.unit_size*3/8) <= self.x <= enemy.x + int(self.world.unit_size*3/8):
                    self.die()
    def detect_spike(self):
        for spike in self.world.spike:
            if spike.y - int(self.world.unit_size-1) <= self.y <= spike.y + int(self.world.unit_size-1):
                if spike.x - int(self.world.unit_size-1) <= self.x <= spike.x + int(self.world.unit_size-1):
                    self.die()
class S_Enemy:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
    def die(self):
        self.world.create_d_enemy(self.x,self.y,1)
        self.world.s_enemy.remove(self)
class Enemy:
    MOVE_SPEED = 3
    def __init__(self,world,start_x,end_x,y):
        self.world = world
        self.x = start_x
        self.start_x = start_x
        self.end_x = end_x
        self.y = y
        self.face_right = 1 #1 right, -1 left
    def die(self):
        self.world.create_d_enemy(self.x,self.y,-self.face_right)
        self.world.enemy.remove(self)
    def update(self,delta):
        if self.face_right == 1 and self.x >= self.end_x:
            self.face_right = -1
        if self.face_right == -1 and self.x <= self.start_x:
            self.face_right = 1
        self.x += Enemy.MOVE_SPEED * self.face_right
class D_Enemy:
    def __init__(self,world,x,y,face):
        self.x = x
        self.y = y
        self.world = world
        self.face = face
        self.stage = 0
        self.delay = 0
        self.cycle = 0
    def die(self):
        self.world.d_enemy.remove(self)
class Ground:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.image = 0
    def die(self):
        self.world.ground.remove(self)
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
    def die(self):
        self.world.spike.remove(self)
class Warp:
    def __init__(self,world,x,y,width,height,mapdirectory,half_size):
        self.world = world
        self.x = range(int(x-half_size),int(x + width))
        self.y = range(int(y-half_size),int(y + height))
        self.directory = mapdirectory
    def check_player_in(self):
        if self.world.player.x in self.x:
            if self.world.player.y in self.y:
               self.world.load(self.directory)
    def die(self):
        self.world.warp.remove(self)
class World:
    def __init__(self,camera,unit_size,scale):
        self.camera = camera
        self.scale = scale
        self.unit_size = unit_size
        self.block = []
        self.ground = []
        self.s_enemy = []
        self.d_enemy = []
        self.enemy = []
        self.spike = []
        self.warp = []
        self.player = None
        self.hold_LEFT = False
        self.hold_RIGHT = False
    def update(self,delta):
        self.player.update(delta)
        if self.player.stop_charge == 0:
            for enemy in self.enemy:
                enemy.update(delta)
        for warp in self.warp:
            warp.check_player_in()
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
        for ground in self.ground+self.block:
            if (ground.y - (self.unit_size) < self.player.y < ground.y + (self.unit_size)):
                g.append(ground)
        return g
    def get_ground_at_player_same_x(self):
        g = []
        for ground in self.ground+self.block:
            if (ground.x - (self.unit_size) < self.player.x < ground.x + (self.unit_size)):
                g.append(ground)
        return g
    def create_warp(self,x,y,width,height,mapdirectory,half_size):
        self.warp.append(Warp(self,x,y,width,height,mapdirectory,half_size))
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
    def create_d_enemy(self,x,y,face):
        self.d_enemy.append(D_Enemy(self,x,y,face))
    def set_current_directory(self,directory):
        self.directory = directory
    def player_pos(self,x,y):
        self.player.jump_charge = 0
        self.player.stop_charge = 0
        self.player.x = x
        self.player.y = y
        self.player.vx = 0
        self.player.vy = 0
        self.player.right = 0
    def enemy_pos(self,pos_lst):
        if len(self.enemy) > len(pos_lst):
            for times in range(len(self.enemy) - len(pos_lst)):
                self.enemy[0].die()
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
            for times in range(len(self.s_enemy) - len(pos_lst)):
                self.s_enemy[0].die()
        need_to_create = len(pos_lst) - len(self.s_enemy)
        for times in range(need_to_create):
            self.create_s_enemy(0,0)
        for pos in range(len(self.s_enemy)):
            self.s_enemy[pos].x = pos_lst[pos][0]
            self.s_enemy[pos].y = pos_lst[pos][1]
    def ground_pos(self,pos_lst):
        if len(self.ground) > len(pos_lst):
            for times in range(len(self.ground) - len(pos_lst)):
                self.ground[0].die()
        need_to_create = len(pos_lst) - len(self.ground)
        for times in range(need_to_create):
            self.create_ground(0,0)
        for pos in range(len(self.ground)):
            self.ground[pos].x = pos_lst[pos][0]
            self.ground[pos].y = pos_lst[pos][1]
    def block_pos(self,pos_lst):
        if len(self.block) > len(pos_lst):
            for times in range(len(self.block) - len(pos_lst)):
                self.block[0].die()
        need_to_create = len(pos_lst) - len(self.block)
        for times in range(need_to_create):
            self.create_block(0,0)
        for pos in range(len(self.block)):
            self.block[pos].x = pos_lst[pos][0]
            self.block[pos].y = pos_lst[pos][1]
    def spike_pos(self,pos_lst):
        if len(self.spike) > len(pos_lst):
            for times in range(len(self.spike) - len(pos_lst)):
                self.spike[0].die()
        need_to_create = len(pos_lst) - len(self.spike)
        for times in range(need_to_create):
            self.create_spike(0,0,0)
        for pos in range(len(self.spike)):
            self.spike[pos].x = pos_lst[pos][0]
            self.spike[pos].y = pos_lst[pos][1]
            self.spike[pos].rotation = pos_lst[pos][2]
    def warp_pos(self,pos_lst):
        if len(self.warp) > len(pos_lst):
            for times in range(len(self.warp) - len(pos_lst)):
                self.wrap[0].die()
        need_to_create = len(pos_lst) - len(self.warp)
        for times in range(need_to_create):
            self.create_warp(0,0,0,0,'',0)
        for pos in range(len(self.warp)):      
            self.warp[pos].x = range(int(pos_lst[pos][0]-pos_lst[pos][5]),int(pos_lst[pos][0] + pos_lst[pos][2]))
            self.warp[pos].y = range(int(pos_lst[pos][1]-pos_lst[pos][5]),int(pos_lst[pos][1] + pos_lst[pos][3]))
            self.warp[pos].directory = pos_lst[pos][4]
    def load(self,directory):
        world_load.set_up(self,directory)
        self.directory = directory
        for d_enemy in self.d_enemy:
            d_enemy.die()
    def update_ground(self,grass_top = True):
        grass_top = -1
        if grass_top:
            for ground in self.ground:
                if grass_top < ground.y:
                    grass_top = ground.y
        for ground in self.ground:
            if ground.y != grass_top:
                other_ground = []
                for ground2 in self.ground:
                    if ground2.x == ground.x:
                        other_ground.append(ground2.y-self.unit_size)
                if ground.y not in (other_ground):
                    ground.image = 1
                
