import sys
import math

# Don't run into a player's light trail! Use your helper bots at strategic moments or as a last resort to be the last drone standing!

player_count = int(input())  # the number of at the start of this game
my_id = int(input())  # your bot's id

direction = {'l':"LEFT", 'r':"RIGHT", 'u':"UP", 'd':"DOWN"}
board = [[0 for u in range(30)] for d in range(15)]
enemy_locations=[[0, 0] for u in range(player_count)]
enemy_differences = [[0, 0] for u in range(player_count)]
my_location = []
direction_choice = "LEFT"

def look_ahead(x, y, direction):
    global board
    print(x,y, file=sys.stderr)
    if direction == "LEFT":
        return board[y][getX(x-1)]
    if direction == "RIGHT":
        return board[y][getX(x+1)]
    if direction == "UP":
        return board[getY(y - 1)][x]
    if direction == "DOWN":
        return board[getY(y + 1)][x]
        
# def print_board():
#     global board
#     for i in board:
#         print(board[i], file=sys.stderr)
def getX(x):
    if x < 0:
        return 30 + x
    if x >= 30:
        return x - 30
    return x

def getY(y):
    if y < 0:
        return 15 + y
    if y >= 15:
        return y - 15
    return y

def seek_till(look_distance, seek_value):
    global board, my_location
    x, y = my_location
    print(x,y,getX(x+1),getY(y+1),file=sys.stderr)
    print(board,file=sys.stderr)
    directions_present = set()
    
    for loop_x in range(x + 1, x + look_distance + 1):
        if board[y][getX(loop_x)] in seek_value:
            directions_present.add("RIGHT")
    
    for loop_x in range(x - look_distance, x):
        if board[y][getX(loop_x)] in seek_value:
            directions_present.add("LEFT")
    
    for loop_y in range(y + 1, y + look_distance + 1):
        if board[getY(loop_y)][x] in seek_value:
            directions_present.add("DOWN")
        
    for loop_y in range(y - look_distance, y):
        if board[getY(loop_y)][x] in seek_value:
            directions_present.add("UP")
        
    if board[getY(y+1)][getX(x+1)] in seek_value:
        directions_present.add("RIGHT")
        directions_present.add("DOWN")
    
    if board[getY(y-1)][getX(x+1)] in seek_value:
        directions_present.add("RIGHT")
        directions_present.add("UP")
    
    if board[getY(y+1)][getX(x-1)] in seek_value:
        directions_present.add("LEFT")
        directions_present.add("DOWN")
    
    if board[getY(y-1)][getX(x-1)] in seek_value:
        directions_present.add("LEFT")
        directions_present.add("UP")
    
    return directions_present

def seek_at(from_x, from_y, to_x, to_y):
    global board, my_location
    my_x, my_y = my_location
    from_x, from_y = getX(from_x), getY(from_y)
    return board[getY(from_y + to_y)][getX(from_x + to_x)]
    
    
def deploy_strat():
    print("DEPLOY")
    pass


def move(helper_bots):
    global my_location, direction_choice
    possible_directions = set(direction.values())
    dont_go = seek_till(2, [2])
    moved = False
    print(possible_directions, file=sys.stderr)
    possible_directions = possible_directions - dont_go
    print(dont_go,possible_directions, file=sys.stderr)
    if look_ahead(my_location[0], my_location[1], direction_choice) == 0:
        moved = True
    else:
        possible_directions = possible_directions - set(direction_choice)
        for d in possible_directions:
            if look_ahead(my_location[0], my_location[1], d) == 0:
                direction_choice = d
                moved = True
                break
    if not moved and helper_bots>0:
        deploy_strat()
    else:
        print(direction_choice)
            
# game loop
loop_2 = False
while True:
    if not loop_2:
        loop_2 = True
    else:
        for e in enemy_locations:
            board[e[1]][e[0]] = 1
            
    helper_bots = int(input())  # your number of charges left to deploy helper bots
    for i in range(player_count):
        # x: your bot's coordinates on the grid (0,0) is top-left
        x, y = [int(j) for j in input().split()]
        board[y][x] = 2
        if i == my_id:
            my_location = [x, y]
            # board[y][x] = 0
        enemy_locations[i] = [x,y]
    

    
    move(helper_bots)  
    
                    
    removal_count = int(input())  # the amount walls removed this turn by helper bots
    for i in range(removal_count):
        # remove_x: the coordinates of a wall removed this turn
        remove_x, remove_y = [int(j) for j in input().split()]
        board[remove_y][remove_x] = 0
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # DOWN | LEFT | RIGHT | UP or DEPLOY (to clear walls)
    
    
        
        
        
    # print(random.choice(direction.values()))
