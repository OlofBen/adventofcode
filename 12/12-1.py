
input = open("input", "r").readlines()
input = [row.strip() for row in input]

def is_inside(matrix, row : int, col : int): 
    return row >= 0 and row<len(matrix) and col >= 0 and col < len(matrix[row])

def neightbours(row : int, col : int): 
    return[(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]


def vissit(matrix, row, col, vissited : set, c): 
    vissited.add((row, col))

    area = 1
    perimeter = 0
    for n_row, n_col in neightbours(row, col): 
        if is_inside(matrix, n_row, n_col) and matrix[n_row][n_col] == c:
            if  (n_row, n_col) not in vissited: 
                n_araea, n_perimeter = vissit(matrix, n_row, n_col, vissited, c)
                area += n_araea
                perimeter += n_perimeter
        else:
            perimeter += 1
    return (area, perimeter)


cost = 0
vissited = set()
for row, list in enumerate(input): 
    for col, value in enumerate(list): 
        if  (row, col) not in vissited: 
            area, perimeter = vissit(input, row, col, vissited, value)
            cost += area * perimeter

print(cost)