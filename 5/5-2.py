
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
                return (False, other)
    return (True, None)

def is_valid_update(line): 
    for i in update:
        if not is_valid_number(i, line)[0]: 
            return False
    return True

def fix_invalid_update(update : list):
    # fixing via bubble sort 
    is_fixed = False
    while not is_fixed: 
        is_fixed = True
        for index, num in enumerate(update): 
            is_valid, conflict_number = is_valid_number(num, update)
            if not is_valid:
                is_fixed = False
                other_index = update.index(conflict_number)
                temp = update[other_index]
                update[other_index] = update[index]
                update[index] = temp






for update in updates: 
    if not is_valid_update(update): 
        fix_invalid_update(update)
        print(update[len(update) // 2])
        sum += update[len(update) // 2]



print(conditions_map)
print(sum)
