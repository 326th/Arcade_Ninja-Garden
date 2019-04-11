def set_up(world,directory):
    enemy_pos = []
    s_enemy_pos = []
    ground_pos = []
    block_pos = []
    spike_pos = []
    half_size = world.unit_size/2
    lst = list(reversed(open(directory,'r').read().split('\n')))
    for string in range(len(lst)):
        line = lst[string]
        y =  int(((string-1)*world.unit_size) + half_size)
        component = line.split(',') # get [S_Enemy, str(x), ...
        component = list(map(lambda x:int((int(x)*world.unit_size) + half_size), component[1:]))
        if line[0:5] == 'Enemy':
            enemy_pos.append([component[0],component[1],component[2]])
        if line[0:7] == 'S_Enemy':
            s_enemy_pos.append([component[0],component[1]])
        elif line[0:6] == 'Player':
            world.player_pos(component[0],component[1])
##        elif line[0:3] == 'Map':
##            component = line.split(',') # get [Warp, str(x), ...
##            #generate warp - Warp(world,startx,starty,width,heigth,mapdirectory
        else:
            for symbol in range(len(line)):
                x =  int((symbol*world.unit_size) + half_size)
                if line[symbol] == 'M':
                    ground_pos.append([x,y])
                elif line[symbol] == 'X':
                    block_pos.append([x,y])
                elif line[symbol] == 'W':
                    spike_pos.append([x,y,0])
                elif line[symbol] == 'D':
                    spike_pos.append([x,y,1])
                elif line[symbol] == 'S':
                    spike_pos.append([x,y,2])
                elif line[symbol] == 'A':
                    spike_pos.append([x,y,3])
    world.enemy_pos(enemy_pos)
    world.s_enemy_pos(s_enemy_pos)
    world.ground_pos(ground_pos)
    world.block_pos(block_pos)
    world.spike_pos(spike_pos)
