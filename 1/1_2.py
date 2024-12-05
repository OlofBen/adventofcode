from collections import Counter

left = [] 
right = []

input = open("input.csv", "r") 

for line in input.readlines(): 
    splited = line.split(' ')
    left.append(int(splited[0]))
    right.append(int(splited[3]))

left.sort() 
c = Counter(right) 

score = [l * c[l] for l, r in zip(left, right)]
print(sum(score))