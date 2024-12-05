import regex as re

prod = 0
def multiply(mul : str): 
    print(mul)
    mul=mul.strip("mul(")
    mul = mul.strip(")")
    left, right = mul.split(",")
    return int(right) * int(left)


input = open("input.txt", "r").read()
enabled = True
index = 0


mul_pattern = r"^mul\([0-9]{1,3},[0-9]{1,3}\)"
do_pattern = r"^do\(\)"
dont_pattern = r"^don't\(\)"
for index in range(len(input)):
    temp_input = input[index:]
    mul_iter = re.findall(mul_pattern, temp_input) # There are far better ways of doing this, but this is good enough
    if(mul_iter != [] and enabled): 
        prod += multiply(mul_iter[0])
        continue
    do_list = re.findall(do_pattern, temp_input)
    if(do_list != []): 
            enabled = True
            continue
    dont_list = re.findall(dont_pattern, temp_input)
    if(dont_list != []): 
            enabled = False
            continue



print(prod)