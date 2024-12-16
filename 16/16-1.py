from queue import PriorityQueue

maze = open("input", "r").readlines()
visited = {} # pos and score of vissited pos
q = PriorityQueue()

start = (-1,-1)
end = (-1,-1)
def move_pos(pos, dir): 
    return (pos[0] + dir[0], pos[1] + dir[1])

# find start and end 
for i, row in enumerate(maze): 
    for j, c in enumerate(row):
        if c == 'S': 
            start = (i,j)
        if c == 'E': 
            end = (i,j)
            
def dirs(): 
    return[(1, 0), (0,1), (-1, 0), (0, -1)]

def move_pos(pos, dir): 
    return (pos[0] + dir[0], pos[1] + dir[1])

            
def visit(pos, dir, score):
    if maze[pos[0]][pos[1]] == '#': return
    if pos in visited: return
    visited[pos] = score
    # dir is the direction in which we are moving  
    for new_dir in dirs(): 
        new_pos = move_pos(pos, new_dir)
        new_score = score
        if dir == new_dir: 
            new_score += 1
        else: 
            new_score += 1001
        q.put((new_score, new_pos, new_dir))
        
q.put((0, start, (0,1)))

while not q.empty(): 
    score, pos, dir = q.get()
    if pos == end: 
        print(score)
        break
    visit(pos, dir, score) 
            
