import regex as re


input = open("input.txt", "r")


muls = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input.read()) 

prod = 0

for mul in muls: 
    print(mul)
    mul=mul.strip("mul(")
    mul = mul.strip(")")
    left, right = mul.split(",")
    print(left, right)
    prod += int(right) * int(left)

print(prod)