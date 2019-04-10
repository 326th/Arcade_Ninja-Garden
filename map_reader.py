import model
def find_map(directory):
    return list(reversed(open(directory,'r').read().split('\n')))
def read_map(camera,directory,unit_size,scale):
    half_size = unit_size / 2
    lst = find_map(directory)
    world = model.World(camera,unit_size,scale)
    world.set_current_directory(directory)
    for string in range(len(lst)):
        line = lst[string]
        y =  int(((string-1)*unit_size) + half_size)
        component = line.split(',') # get [S_Enemy, str(x), ...
        component = list(map(lambda x:int((int(x)*unit_size) + half_size), component[1:]))
        if line[0:5] == 'Enemy':
            world.create_enemy(component[0],component[1],component[2])
        if line[0:7] == 'S_Enemy':
            world.create_s_enemy(component[0],component[1])
        elif line[0:6] == 'Player':
            world.create_player(component[0],component[1])
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
                elif line[symbol] == 'W':
                    world.create_spike(x,y,0)
                elif line[symbol] == 'D':
                    world.create_spike(x,y,1)
                elif line[symbol] == 'S':
                    world.create_spike(x,y,2)
                elif line[symbol] == 'A':
                    world.create_spike(x,y,3)
    return world

