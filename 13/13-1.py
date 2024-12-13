import numpy as np
from queue import PriorityQueue

def calculate_cost(a_x : int, a_y : int, b_x : int, b_y : int , p_x : int , p_y : int ): 
    a_v = np.array([a_x, a_y])
    b_v = np.array([b_x, b_y])
    p_v = np.array([p_x, p_y])
    s = np.array([[a_x, a_y], [b_x, b_y]])
    s_inv = np.linalg.inv(s)
    
    for i in range(100): 
        for j in range(100): 
            if (i*a_x + j*b_x == p_x) and (i*a_y + j*b_y == p_y):
                return (i,j) 
    
    return(-1,-1)

sum = 0

input = open("input", "r").readlines()

for i in range(len(input)//4 + 1): 
    button_a_str = input[i * 4].strip("Button A: X+") 
    a_x, a_y = map(int, button_a_str.split(", Y+"))
    button_b_str = input[i * 4 + 1].strip("Button B: X+") 
    b_x, b_y = map(int, button_b_str.split(", Y+"))
    p_x, p_y = map(int, input[i * 4 + 2].strip("Prize: X=").split(", Y="))


    (num_a, num_b) = calculate_cost(a_x,a_y, b_x, b_y, p_x, p_y)
    if num_a == -1 and num_b == -1: 
        continue
    sum += (num_a * 3 + num_b)
    
print(sum)



