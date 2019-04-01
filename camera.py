import model
import map_reader
START_DIRECTORY = 'maps/start.txt'
class Camera:
    def __init__(self,unit_size,scale):
        self.world = map_reader.read_map(START_DIRECTORY,unit_size,scale)
        self.unit_size = unit_size
    def update(self,delta):
        self.world.update(delta)
    def on_key_press(self,key,key_modifiers):
        self.world.on_key_press(key,key_modifiers)
    def on_key_release(self,key,key_modifiers):
        self.world.on_key_release(key,key_modifiers)
    def get_positon_displace(self):
        displace_x = -(self.world.player.x - (5*self.unit_size))
        displace_y = -(self.world.player.y - (5*self.unit_size))
        if displace_x > 0:
            displace_x = 0
        if displace_y > 0:
            displace_y = 0
        return [displace_x,displace_y]
        
