
input = open("input", "r").readlines()
input = [row.strip() for row in input]

def is_inside(matrix, row : int, col : int): 
    return row >= 0 and row<len(matrix) and col >= 0 and col < len(matrix[row])

def neightbours(row : int, col : int): 
    return[(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]

def is_same(matrix, row, col, c):
    return is_inside(matrix, row, col) and matrix[row][col] == c

def num_corners(matrix, row, col, c): 
    neigh = neightbours(row, col)
    neightbours_sifted = neigh[1:] + [neigh[0]]
    corner = 0
    for (row1, col1), (row2, col2) in zip(neigh, neightbours_sifted): 
        diagonal = is_same(matrix, row2, col1, c) and is_same(matrix, row1, col2, c) # one of these is the node it self

        if (is_same(matrix, row1, col1, c) and is_same(matrix, row2, col2, c) and not diagonal) or (not is_same(matrix, row1, col1, c) and not is_same(matrix, row2, col2, c)): 

            corner += 1
    return corner


def vissit(matrix, row, col, vissited : set, c): 
    vissited.add((row, col))

    area = 1
    corners = num_corners(matrix, row, col, c)
    for n_row, n_col in neightbours(row, col): 
        if is_inside(matrix, n_row, n_col) and matrix[n_row][n_col] == c:
            if  (n_row, n_col) not in vissited: 
                n_araea, n_corners = vissit(matrix, n_row, n_col, vissited, c)
                area += n_araea
                corners += n_corners
        
    return (area, corners)


cost = 0
vissited = set()
for row, list in enumerate(input): 
    for col, value in enumerate(list): 
        if  (row, col) not in vissited: 
            area, corners = vissit(input, row, col, vissited, value)
            cost += area * (corners)
print(cost)