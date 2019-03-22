from model import World
class Camera:
    def __init__(self,width,heigth):
        self.world = World(width,heigth)
        self.player = []
        self.ground = []
        self.enemy = []
        self.block = []
    def object_in_camera(self):
        #return all object in camera(based on player)
