from model import Player,S_Enemy,Enemy,Ground,Block,Warp,World
def find_map(directory):
    return open(directory,'r').read().split('\n')
def read_map(directory,world):
    lst = find_map(directory)
    for y in range(len(lst)):
        line = lst[y]
        if line[0:5] == 'Enemy':
            line.split(',') # get [Enemy, str(x), ...
            #generate enemy - Enemy(world,x,starty,x,returny)
        elif line[0:7] == 'S_Enemy':
            #generate enemy - S_Enemy(world,x,y)
        elif line[0:3] == 'Map':
            #generate warp - Warp(world,startx,starty,width,heigth,mapdirectory
        else:
            for x in range(line):
                if line[num] == 'M':
                    #create Ground(world,x,y)
                elif line[num] == 'X':
                    #create Block(world,x,y)
                elif line[num] == 'P':
                    #create PlayerSpawn(world,x,y)
