import numpy as np
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
    print(map)

robots = [] 

for row in input: 
    print(row)
    ps, vs = row.split(" ")
    x, y = map(int, ps.strip("p=").split(","))
    vx, vy = map(int, vs.strip("v=").split(","))
    robots.append(Robot(x,y,vx,vy))
print_map(robots)

for _ in range(100): 
    for robot in robots: 
        robot.move(width, hight)
    print_map(robots)

quadrants = [0,0,0,0]
for robot in robots: 
    quadrant = 0
    print(robot.x, robot.y, width // 2, hight // 2)
    if robot.x == width // 2: 
        continue
    if robot.y == hight // 2: 
        continue
    if robot.x > width // 2: 
        quadrant += 1
    if robot.y > hight // 2: 
        quadrant += 2
    quadrants[quadrant] += 1
sum = 1
for q in quadrants: 
    sum *= q
print(sum)