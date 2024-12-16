
input = open("input", "r").readlines()


char2tup = {'>': (0, 1), '<': (0, -1),'^': (-1, 0),'v': (1, 0)}
obsticles = {}
robot = (-1,-1)

i = 0
while input[i].strip() != "": 
    row = input[i]
    for j, c in enumerate(row): 
        if (c == '#' or c == 'O'):
            obsticles[(i,j)] = c 
        if c == '@':
            obsticles[(i,j)] = c
            robot = (i,j)
    i+=1

temp = list(map(lambda x: x.strip(), input[i + 1:]))
dirs = []
for row in temp: 
    for c in row: 
        dirs.append(char2tup[c])

def move_pos(pos, dir): 
    return (pos[0] + dir[0], pos[1] + dir[1])

def move(pos, dir): 
    if obsticles[pos] == '#': 
        return False
    next = move_pos(pos, dir)
    if next in obsticles and not move(next, dir): 
        return False
    # do the move 
    elm = obsticles.pop(pos)
    obsticles[next] = elm
    return True
    
print(dirs)

for dir in dirs: 
    if move(robot, dir): 
        robot = move_pos(robot, dir)

score = 0 
for pos, elm in obsticles.items(): 
    if elm == 'O': 
        score += 100 * pos[0] + pos[1]

print(score)

