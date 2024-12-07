import math

input = open("input", "r").readlines()


def concat(right, left): 
    return right * 10**(int(math.log10(left)) + 1) + left

print(concat(123, 456))

def is_valid_line(total, current, list :list): 
    if list == []: 
        return total == current; 
    list_copy = list.copy() 
    head = list_copy.pop(0)
    is_posible = is_valid_line(total, current + head, list_copy) or is_valid_line(total, current * head, list_copy) or is_valid_line(total, concat(current, head), list_copy)
    return is_posible

sum = 0

for row in input: 
    total, terms = row.split(":")
    total = int(total)
    terms = list(map(int, terms.strip().split(" ")))
    if (is_valid_line(total, 0, terms)): 
        sum += total
print(sum)