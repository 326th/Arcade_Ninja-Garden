from map_reader import read_map
class Player:
    GRAVITY = 1
    JUMP_SPEED = 15
    AFTER_DASH_SPEED = 5
    FRICTION = 3
    MAX_X = 20
    MAX_Y = 20
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    def update(self,delta):
        #speed
    def jump(self):
        self.vy = Player.JUMP_SPEED
    def slash(self,direction):
        #hit all enemy in path
    def die(self):
        #respawn`
class S_Enemy:
    def __init__(self,world,x,y,number):
        self.world = world
        self.x = x
        self.y = y
        self.number = number
    def hit(self):
        #die
class Enemy:
    def __init__(self,world,x,start_y,end_y,number):
        self.world = world
        self.x = x
        self.y = start_y
        self.start_y = start_y
        self.end_y = end_y
        self.number = number
    def hit(self):
        #die
    def update(self):
        #move back and forth
class Ground:
    GROUND_SIZE = 32
    def __init__(self,world,x,y):
        self.world = world
        self.x = range(x - GROUND_SIZE, x + GROUND_SIZE)
        self.y = range(y - GROUND_SIZE, y + GROUND_SIZE)
class Block:
    BLOCK_SIZE = 32
    def __init__(self,world,x,y):
        self.world = world
        self.x = range(x - BLOCK_SIZE, x + GROUND_SIZE)
        self.y = range(y - BLOCK_SIZE, y + GROUND_SIZE)
class Warp:
    def __init__(self,world,x,y,width,heigth,mapdirectory):
        self.world = world
        self.x = range(x,x + width)
        self.y = range(y,y + height)
        self.directory = mapdirectory
    def check_player_in(self):
        #check if player in it
    def warp(self):
        self.world.warp(self.directory)
class World:
    def __init__(self,width,heigth):
        self.width = width
        self.height = height
        self.block = []
        self.ground = []
        self.enemy = []
    def update(self,delta):
        #update
    def warp(self,directory):
        #stop update world
        #loading screen
        #clear everything in world then load new world
        #remove loading screen
    def on_key_press(self, key, key_modifiers):
        #
    def create_player(self,x,y):
        self.player = Player(self,x,y)
    def create_block(self,x,y):
        self.block.append(Block(self,x,y))
    def create_ground(self,x,y):
        self.ground.append(Ground(self,x,y))
    def create_s_enemy(self,x,y):
        sef.enemy.append(S_Enemy(self,x,y))
    
