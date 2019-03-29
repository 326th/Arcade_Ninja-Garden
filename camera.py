import model
import map_reader
START_DIRECTORY = 'maps/start.txt'
class Camera:
    def __init__(self,unit_size):
        self.world = map_reader.read_map(START_DIRECTORY,unit_size)
    def update(self,delta):
        self.world.update(delta)
    def on_key_press(self,key,key_modifiers):
        self.world.on_key_press(key,key_modifiers)
    def on_key_release(self,key,key_modifiers):
        self.world.on_key_release(key,key_modifiers)
##    def get_positon_displace(self):
##        #return all object in camera(based on player)
        
