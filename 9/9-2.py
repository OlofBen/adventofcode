
input = open("input", "r").read().strip()

input = list(map(int, input))

empty_indicies = []
non_empty_indicies = []

file = []
for index, i in enumerate(input): 
    if index % 2 == 0: 
        non_empty_indicies.append((len(file), i))
        for _ in range(i): 
            file.append(index / 2)
    else: 
        empty_indicies.append((len(file), i))
        for _ in range(i): 
            file.append(".")


non_empty_indicies.reverse()

for non_empty_index, size in non_empty_indicies:
    # print(file)
    i = 0
    while i < len(empty_indicies) and empty_indicies[i][1] < size: 
        i += 1 # setting i to be on the right one
    if i == len(empty_indicies): 

        continue

    index, empty_sapce = empty_indicies[i]

    if index > non_empty_index: 
        continue
    for j in range(size): # copy the string 
        file[index + j] = file[non_empty_index + j]
        file[non_empty_index + j] = '.'
    if empty_sapce == size: 
        empty_indicies.pop(i)
    else: 
        empty_indicies[i] = (index + size, empty_sapce - size)


file = list(map(lambda x: 0 if  x == '.' else x, file))
checksum = [index * num for index, num in enumerate(file)]
print(checksum)

print(sum(checksum))