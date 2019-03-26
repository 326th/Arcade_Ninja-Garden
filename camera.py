import model
import map_reader
START_DIRECTORY = 'maps/start.txt'
class Camera:
    def __init__(self,width,height):
        self.world = map_reader.read_map(START_DIRECTORY,width,height)
##    def get_positon_displace(self):
##        #return all object in camera(based on player)
