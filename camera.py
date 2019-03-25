from map_reader import read_map
START_DIRECTORY = #start map
class Camera:
    def __init__(self,width,heigth):
        self.world = World(width,heigth)
        self.player = []
        self.ground = []
        self.enemy = []
        self.block = []
    def get_positon_displace(self):
        #return all object in camera(based on player)
