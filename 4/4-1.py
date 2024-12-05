
input = [line for line in open("input", "r").readlines()]

def is_inside(matrix, row : int, col : int): 
    return row >= 0 and row<len(matrix) and col >= 0 and col < len(matrix[row])

def is_inside_and_letter(matrix, row, col, letter): 
    return is_inside(matrix, row, col) and (matrix[row][col] == letter)

directions = [(1,0), (1,1), (1,-1), (-1,0), (-1,1), (-1,-1), (0,1), (0,-1)]

num_xmas = 0

for row in range(len(input)): 
    for col in range(len(input[row])): 
        for row_dir, col_dir in directions: 
            if (
                is_inside_and_letter(input, row + row_dir * 0, col + col_dir* 0,'X') &
                is_inside_and_letter(input, row + row_dir * 1, col + col_dir* 1,'M') &
                is_inside_and_letter(input, row + row_dir * 2, col + col_dir* 2,'A') &
                is_inside_and_letter(input, row + row_dir * 3, col + col_dir* 3,'S')
            ): 
                num_xmas+=1
                
            
print(num_xmas)