
input = open("input", "r").readlines()

conditions = []

updates = []

for row in input: 
    row = row.strip()
    if "|" in row: 
        first, second = row.split("|")
        conditions.append((int(first), int(second)))
    elif "," in row: 
        updates.append(list(map(int, row.split(","))))

conditions_map = {}

for (first, second) in conditions: 
    if second in conditions_map: 
        conditions_map[second].append(first)
    else: 
        conditions_map[second] = [first]

sum = 0

def is_valid_number(number : int, update: list) : 
    if number in conditions_map: 
        others = conditions_map[number]
        for other in others:
            if other in update and update.index(other) > update.index(number): 
                return False
    return True

def is_valid_update(line): 
    for i in update:
        if not is_valid_number(i, line): 
            return False
    return True


for update in updates: 
    if is_valid_update(update): 
        print(update[len(update) // 2])
        sum += update[len(update) // 2]



print(conditions_map)
print(sum)
