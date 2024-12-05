def is_save_line(int_line : list): 
    if (int_line[0] == int_line[1]): 
        return False
    increasing = int_line[0] < int_line[1]
    for i, j in zip(int_line, int_line[1:]):
        if (increasing and i>=j) or (not increasing and i<=j): 
            return False
        if (abs(i - j) > 3): 
            return False
    return True 



input = open("input.csv", "r") 
safe = 0

for line in input.readlines(): 
    int_line = [int(c) for c in line.split()]
    has_failed = False
    if (is_save_line(int_line)): 
            safe += 1
            continue
    for index in range(len(int_line)): 
        temp_intline = int_line.copy()
        temp_intline.pop(index)


        if (is_save_line(temp_intline)): 
            safe += 1
            break



print(safe)