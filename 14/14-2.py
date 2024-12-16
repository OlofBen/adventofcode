import numpy as np
np.set_printoptions(threshold=1000000)
input = open("input", "r").readlines()

width = 101
hight = 103

class Robot(): 
    def __init__(self, x : int, y : int , vx : int , vy : int):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self, space_x, space_y): 
        self.x = (self.x + self.vx) % space_x
        self.y = (self.y + self.vy) % space_y

def print_map(robots): 
    map = np.zeros((hight, width))
    for robot in robots:
        map[robot.y, robot.x] += 1
    map = map > 0
    str = np.array_repr(map).replace("\n        ", ' ').replace("False", " ").replace(" True", "X").replace(", ", "").replace("array([[", "").replace("       [", "").replace("],", "").replace("]])", "")
    print(str)

def is_inside(row : int, col : int): 
    return row >= 0 and row<hight and col >= 0 and col < width

def num_has_neighbors(robots): 
    """returns true if the robot has a neighbor """
    map = np.zeros((hight, width))
    for robot in robots:
        map[robot.y, robot.x] += 1
    p = 0
    for robot in robots: 
        neighbours = [(robot.x + 1, robot.y -1), 
                      (robot.x + 1, robot.y),
                      (robot.x +1, robot.y+1 ),
                      (robot.x, robot.y-1),
                      (robot.x, robot.y+1),
                      (robot.x-1, robot.y + 1),
                      (robot.x-1, robot.y),
                      (robot.x-1, robot.y- 1)]
        s = sum([map[y, x] if is_inside(y, x) else 0 for x, y in neighbours])
        if s > 0: 
            p += 1
    return p

robots = [] 

for row in input: 
    ps, vs = row.split(" ")
    x, y = map(int, ps.strip("p=").split(","))
    vx, vy = map(int, vs.strip("v=").split(","))
    robots.append(Robot(x,y,vx,vy))

i = 0
while True: 
    i += 1
    for robot in robots: 
        robot.move(width, hight)
    if(num_has_neighbors(robots) > len(robots) * (3 / 4)):
        break
    
print(i)