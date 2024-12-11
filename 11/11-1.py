import functools
from math import log10
from tqdm import tqdm


input = open("input", "r").read().strip().split(" ")

stones = list(map(int, input))

unique_numbers = set()

@functools.lru_cache(maxsize=1000, typed=False)
def evolve(stone : int):
    unique_numbers.add(stone)
    if stone == 0: 
        return [1]
    
    lenght = int(log10(stone) + 1)
    if (lenght % 2 == 0): 
        split = lenght/2
        return [stone // 10**(split), stone % 10**(split)]
    
    else: 
        return [stone * 2024]
    
def flatten(xss):
    return [x for xs in xss for x in xs]

def blink(stones : list): 
    next_it = [evolve(stone) for stone in stones]
    return flatten(next_it)

for _ in tqdm(range(75)): 
    stones = blink(stones)
    print(len(unique_numbers))


print(len(stones))