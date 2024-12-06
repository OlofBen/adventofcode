
input = open("input", "r").readlines()

obsticle = []
has_bin = set()
guard = (0,0)
dir = (-1, 0)

for index, row in enumerate(input): 
    if '^' in row: 
        guard = (index, row.index('^')) 
    obsticle.append(list(map(lambda x: x == '#', row)))



def is_inside(matrix, row : int, col : int): 
    return row >= 0 and row<len(matrix) and col >= 0 and col < len(matrix[row])


def rotate(dir): 
    match dir: 
        case (1,0): 
            return (0,-1)
        case (0,-1):
            return (-1,0)
        case (-1, 0): 
            return (0,1)
        case (0,1):
            return (1, 0)
        case _: 
            print("Error")
            return (0,0)
        
def next(pos, dir): 
    return (pos[0] + dir[0], pos[1] + dir[1])

def is_obstacle(obsticle, row, col): 
    if not is_inside(obsticle, row, col): 
        return False
    return obsticle[row][col]


while (is_inside(obsticle, guard[0], guard[1])): 
    has_bin.add((guard[0], guard[1]))
    next_row, next_col = next(guard, dir)
    if is_obstacle(obsticle, next_row, next_col): 
        dir = rotate(dir)
    else: 
        guard = (next_row, next_col)

print(has_bin)
print(len(has_bin))
