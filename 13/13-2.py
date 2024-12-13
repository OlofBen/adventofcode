import numpy as np
import scipy as sp
import math
from tqdm import tqdm

def calculate_cost(a_x : int, a_y : int, b_x : int, b_y : int , p_x : int , p_y : int ): 
    
    p_v = np.array([p_x, p_y])
    s = np.array([[a_x, b_x], [a_y, b_y]])

    res = np.linalg.solve(s, p_v)
    res = np.round(res, decimals=0)
    

    if (a_x * (res[0]) + b_x * (res[1]) == p_x ) and (a_y * (res[0]) + b_y * (res[1]) == p_y): 
        if ((res[0])  < 0 or (res[1]) < 0): 
            print("FUUUUUUUUUUUUUUCK")
        return (res[0], res[1])
    
    return(0,0)

sum = 0

input = open("input", "r").readlines()

for i in tqdm(range(len(input)//4 + 1)): 
    button_a_str = input[i * 4].strip("Button A: X+") 
    a_x, a_y = map(int, button_a_str.split(", Y+"))
    button_b_str = input[i * 4 + 1].strip("Button B: X+") 
    b_x, b_y = map(int, button_b_str.split(", Y+"))
    p_x, p_y = map(int, input[i * 4 + 2].strip("Prize: X=").split(", Y="))


    (num_a, num_b) = calculate_cost(a_x,a_y, b_x, b_y, p_x + 10000000000000, p_y + 10000000000000)
    # (num_a, num_b) = calculate_cost(a_x,a_y, b_x, b_y, p_x , p_y )

    sum += (num_a * 3 + num_b)
    
print(sum)



