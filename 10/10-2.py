
input = open("input", "r").readlines()
input = [list(map(int, row.strip())) for row in input]

def is_inside(matrix, row : int, col : int): 
    return row >= 0 and row<len(matrix) and col >= 0 and col < len(matrix[row])

def neightbours(row : int, col : int): 
    return[(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]


def vissit(matrix, row, col): 
    current_hight = matrix[row][col]
    if current_hight == 9: 
        return 1
    sum = 0
    for n_row, n_col in neightbours(row, col): 
        if is_inside(matrix, n_row, n_col) and matrix[n_row][n_col] == current_hight + 1: 
            sum += vissit(matrix, n_row, n_col)
    
    return sum


trailheads_sum = 0
for row, list in enumerate(input): 
    for col, value in enumerate(list): 
        if value == 0: 
            trailheads_sum += vissit(input, row, col)


print(trailheads_sum)