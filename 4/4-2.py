
input = [line for line in open("input", "r").readlines()]



def is_inside(matrix, row : int, col : int): 
    return row >= 0 and row<len(matrix) and col >= 0 and col < len(matrix[row])

def is_inside_and_letter(matrix, row, col, letter): 
    return is_inside(matrix, row, col) and (matrix[row][col] == letter)

def is_mas(matrix, row, col, direction):
    row_dir, col_dir = direction
    return (
        is_inside_and_letter(matrix, row + row_dir * -1, col + col_dir * -1, 'M') and 
        is_inside_and_letter(matrix, row + row_dir *  0, col + col_dir *  0, 'A') and 
        is_inside_and_letter(matrix, row + row_dir *  1, col + col_dir *  1, 'S'))


def is_x_mas(matrix, row, col): 
    if (matrix[row][col] != 'A'):
        return 0
    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
    mases = [is_mas(matrix, row, col, direction) for direction in directions]
    return sum(mases) > 1




num_xmas = 0

for row in range(len(input)): 
    for col in range(len(input[row])): 
        num_xmas += is_x_mas(input, row, col)
                
            
print(num_xmas)