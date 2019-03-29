import arcade.key
class Player:
    GRAVITY = -1
    JUMP_SPEED = 15
    DASH_ACC = 2
    FRICTION = 1
    MAX_X = 10
    MAX_Y = 20
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 2
        self.vy = 0
    def update(self,delta):
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
        self.x += self.vx
        self.y += self.vy
        if self.y < 128:
            self.y = 128
    def jump(self):
        self.vy = Player.JUMP_SPEED
##    def slash(self,direction):
##        #hit all enemy in path
##    def die(self):
##        #respawn`
class S_Enemy:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
##    def hit(self):
##        #die
class Enemy:
    def __init__(self,world,start_x,end_x,y):
        self.world = world
        self.x = start_x
        self.start_x = start_x
        self.end_x = end_x
        self.y = y
##    def hit(self):
##        #die
##    def update(self):
##        #move back and forth
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
    def __init__(self,unit_size):
        self.unit_size = unit_size
        self.block = []
        self.ground = []
        self.s_enemy = []
        self.enemy = []
        self.hold_LEFT = False
        self.hold_RIGHT = False
    def update(self,delta):
        self.player.update(delta)
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
    def on_key_release(self,key,key_modifiers):
        if key == arcade.key.LEFT:
            self.hold_LEFT = False
        if key == arcade.key.RIGHT:
            self.hold_RIGHT = False
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
