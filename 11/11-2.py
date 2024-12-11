import functools
from math import log10
from tqdm import tqdm

input = open("input", "r").read().strip().split(" ")

stones = list(map(lambda x: (int(x), 1), input))


def evolve(stone : int, number_of_stones):
    if stone == 0: 
        return [(1, number_of_stones)]
    
    lenght = int(log10(stone) + 1)
    if (lenght % 2 == 0): 
        split = lenght/2
        return [(stone // 10**(split), number_of_stones), (stone % 10**(split), number_of_stones)]
    
    else: 
        return [(stone * 2024, number_of_stones)]
    
def flatten(xss):
    return [x for xs in xss for x in xs]

def blink(stones : list): 
    next_it = [evolve(stone, num) for stone, num in stones]
    combined = {}
    for (i, number_of_stones) in flatten(next_it): 
        if i in combined: 
            combined[i] += number_of_stones
        else: 
            combined[i] = number_of_stones
    return combined
        
        

for _ in tqdm(range(25)): 
    stones = blink(stones).items()

sum = 0
for _, num in stones: 
    sum += num
    
print(sum)
    