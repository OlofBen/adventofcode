
input = open("input", "r").readlines()


char2tup = {'>': (0, 1), '<': (0, -1),'^': (-1, 0),'v': (1, 0)}
obsticles = {}
robot = (-1,-1)

i = 0
while input[i].strip() != "": 
    row = input[i]
    for j, c in enumerate(row): 
        if c == '#':
            obsticles[(i,j * 2)] = '#'
            obsticles[(i,j * 2 + 1)] = '#'
        if  c == 'O':
            obsticles[(i,j * 2)] = '[' 
            obsticles[(i,j * 2 +1)] = ']'
        if c == '@':
            obsticles[(i,j * 2)] = c
            robot = (i,j * 2)
    i+=1

temp = list(map(lambda x: x.strip(), input[i + 1:]))
dirs = []
for row in temp: 
    for c in row: 
        dirs.append(char2tup[c])

def move_pos(pos, dir): 
    return (pos[0] + dir[0], pos[1] + dir[1])

def can_move(pos, dir, check_sides = True): 
    this_elem = obsticles[pos]
    if this_elem == '#': 
        return False
    if check_sides and (dir == (1, 0) or dir == (-1, 0)): 
        if this_elem == ']' and not can_move((pos[0], pos[1] - 1), dir, check_sides=False):
            return False
        elif this_elem == '[' and not can_move((pos[0], pos[1] + 1), dir, check_sides=False):
            return False
    next = move_pos(pos, dir)
    if next in obsticles and not can_move(next, dir): 
        return False
    return True

def move(pos, dir, check_sides = True): 
    this_elem = obsticles[pos]

    if this_elem == '#': 
        return False
    if check_sides and (dir == (1, 0) or dir == (-1, 0)): 
        if this_elem == ']' and not move((pos[0], pos[1] - 1), dir, check_sides=False):
            return False
        elif this_elem == '[' and not move((pos[0], pos[1] + 1), dir, check_sides=False):
            return False
    next = move_pos(pos, dir)
    if next in obsticles and not move(next, dir): 
        return False
    # do the move 
    elm = obsticles.pop(pos)
    obsticles[next] = elm
    return True

def print_board():
    for j in range(7):
        row = []
        for i in range(14):
            if (j, i) in obsticles: 
                row.append(obsticles[(j,i)])
            else: 
                row.append(".")
        print(row)

    

for dir in dirs: 
    if can_move(robot, dir): 
        move(robot, dir)
        robot = move_pos(robot, dir)

score = 0 
for pos, elm in obsticles.items(): 
    if elm == '[': 
        score += 100 * pos[0] + pos[1]

print(score)

