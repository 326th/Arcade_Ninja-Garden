from model import World
def find_map(directory):
    return list(reversed(open(directory,'r').read().split('\n')))
def read_map(directory,width,heigth):
    lst = find_map(directory)
    world = World(width,heigth)
    for y in range(len(lst)):
        line = lst[y]
        if line[0:5] == 'Enemy':
            line.split(',') # get [Enemy, str(x), ...
            #generate enemy - Enemy(world,x,starty,x,returny)
        elif line[0:7] == 'S_Enemy':
            world.create_s_enemy(x,y)
        elif line[0:3] == 'Map':
            #generate warp - Warp(world,startx,starty,width,heigth,mapdirectory
        else:
            for x in range(len(line)):
                if line[x] == 'M':
                    world.create_ground(x,y)
                elif line[x] == 'X':
                    world.create_block(x,y)
                elif line[x] == 'P':
                    world.create_player(x,y)
