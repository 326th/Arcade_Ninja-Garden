def new_pos_x(player,ground_lst,unit_size):
    in_ground = True
    is_stopped = False
    player_new = player.vx + player.x
    while in_ground:
        in_ground = False
        for ground in ground_lst:
            if (ground.x - (unit_size) < player_new < ground.x + (unit_size)):
                in_ground = True
                is_stopped = True
        if in_ground:
            if player.vx >0:
                player_new -= 1
            elif player.vx <0:
                player_new += 1
    return player_new, is_stopped
def new_pos_y(player,ground_lst,unit_size):
    in_ground = True
    is_stopped = False
    player_new = player.vy + player.y
    while in_ground:
        in_ground = False
        for ground in ground_lst:
            if (ground.y - (unit_size) < player_new < ground.y + (unit_size)):
                in_ground = True
                is_stopped = True
        if in_ground:
            if player.vy >0:
                player_new -= 1
            elif player.vy <0:
                player_new += 1
    return player_new, is_stopped
            
