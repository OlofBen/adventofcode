

input = open("input", "r").readlines()

input = [row.strip() for row in input]

position_map = {} 
antinodes = set()

for i, row in enumerate(input): 
    for j, c in enumerate(row): 
        if (c =='.'):
            continue
        
        if c in position_map: 
            position_map[c].append((i, j))
        else: 
            position_map[c] = [(i,j)]

def is_inside(matrix, row : int, col : int): 
    return row >= 0 and row<len(matrix) and col >= 0 and col < len(matrix[row])

def opposite(p1, p2): 
    diff = (p2[0] - p1[0],p2[1] - p1[1])
    return (p1[0] - diff[0], p1[1] - diff[1])

for k, positions in position_map.items(): 
    for p1 in positions: 
        for p2 in positions: 
            if p1 == p2:
                continue
            antinode = opposite(p1, p2)
            if (is_inside(input, antinode[0], antinode[1])):
                antinodes.add(antinode)

print(len(antinodes))