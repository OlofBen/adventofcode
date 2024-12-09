
input = open("input", "r").read().strip()

input = list(map(int, input))

empty_indicies = []
non_empty_indicies = []

file = []
for index, i in enumerate(input): 
    if index % 2 == 0: 
        for _ in range(i): 
            non_empty_indicies.append(len(file))
            file.append(index / 2)
    else: 
        for _ in range(i): 
            empty_indicies.append(len(file))
            file.append(".")




while empty_indicies != [] and  empty_indicies[0] < non_empty_indicies[-1]: 
    #print(file)
    empty = empty_indicies.pop(0)
    nonempty = non_empty_indicies.pop()
    file[empty] = file[nonempty]
    file[nonempty] = '.'

#print(file)

file = list(filter(lambda x: x != '.', file))
checksum = [index * num for index, num in enumerate(file)]
#print(checksum)
print(sum(checksum))