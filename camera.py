import model
import map_reader
START_DIRECTORY = 'maps/map1.txt'
class Camera:
    def __init__(self,ninjawindow,unit_size,scale):
        self.ninjawindow = ninjawindow
        self.unit_size = unit_size
        self.scale = scale
        self.world = map_reader.read_map(self,START_DIRECTORY,unit_size,scale)
        self.unit_size = unit_size
        self.displace_x = 0
        self.displace_y = 0
    def update(self,delta):
        self.world.update(delta)
    def on_key_press(self,key,key_modifiers):
        self.world.on_key_press(key,key_modifiers)
    def on_key_release(self,key,key_modifiers):
        self.world.on_key_release(key,key_modifiers)
    def get_positon_displace(self):
        if self.world.player.stop_charge>0:
            return
        self.displace_x = -(self.world.player.x - (5*self.unit_size))
        self.displace_y = -(self.world.player.y - (5*self.unit_size))
        if self.displace_x > 0:
            self.displace_x = 0
        if self.displace_y > 0:
            self.displace_y = 0
