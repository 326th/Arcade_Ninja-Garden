import model
def find_map(directory):
    return list(reversed(open(directory,'r').read().split('\n')))
def read_map(directory,unit_size):
    half_size = unit_size / 2
    lst = find_map(directory)
    world = model.World()
    for string in range(len(lst)):
        line = lst[string]
        y =  int(((string-1)*unit_size) + half_size)
        if line[0:5] == 'Enemy':
            component = line.split(',') # get [Enemy, str(x), ...
            component = list(map(lambda x:int((int(x)*unit_size) + half_size), component[1:]))
            world.create_enemy(component[0],component[1],component[2])
        if line[0:7] == 'S_Enemy':
            component = line.split(',') # get [S_Enemy, str(x), ...
            component = list(map(lambda x:int((int(x)*unit_size) + half_size), component[1:]))
            world.create_s_enemy(component[0],component[1])
##        elif line[0:3] == 'Map':
##            component = line.split(',') # get [Warp, str(x), ...
##            #generate warp - Warp(world,startx,starty,width,heigth,mapdirectory
        else:
            for symbol in range(len(line)):
                x =  int((symbol*unit_size) + half_size)
                if line[symbol] == 'M':
                    world.create_ground(x,y)
                elif line[symbol] == 'X':
                    world.create_block(x,y)
                elif line[symbol] == 'P':
                    world.create_player(x,y)
    return world

