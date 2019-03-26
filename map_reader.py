import model
UNIT_SIZE = 64
HALF_SIZE = UNIT_SIZE/2
def find_map(directory):
    return list(reversed(open(directory,'r').read().split('\n')))
def read_map(directory,width,height):
    lst = find_map(directory)
    world = model.World(width,height)
    for string in range(len(lst)):
        line = lst[string]
        y =  int(((string-1)*UNIT_SIZE) + HALF_SIZE)
        if line[0:5] == 'Enemy':
            component = line.split(',') # get [Enemy, str(x), ...
            component = list(map(lambda x:int((int(x)*UNIT_SIZE) + HALF_SIZE), component[1:]))
            world.create_enemy(component[0],component[1],component[2])
        if line[0:7] == 'S_Enemy':
            component = line.split(',') # get [S_Enemy, str(x), ...
            component = list(map(lambda x:int((int(x)*UNIT_SIZE) + HALF_SIZE), component[1:]))
            world.create_s_enemy(component[0],component[1])
##        elif line[0:3] == 'Map':
##            component = line.split(',') # get [Warp, str(x), ...
##            #generate warp - Warp(world,startx,starty,width,heigth,mapdirectory
        else:
            for symbol in range(len(line)):
                x =  int((symbol*UNIT_SIZE) + HALF_SIZE)
                if line[symbol] == 'M':
                    world.create_ground(x,y)
                elif line[symbol] == 'X':
                    world.create_block(x,y)
                elif line[symbol] == 'P':
                    world.create_player(x,y)
    return world
