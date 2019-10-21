import random
from random import choice
npart=500
side=51  #Should be an odd number
perc=0
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
density=float(input("density"))
maxsteps=10000
perc=0
for ipart in range(npart):
    x = side//2
    y = side//2
    for x in range(side):
        for y in range(side):
            grid[x][y]=random.randint(0,100)
            if grid[x][y] <= (density*100):
                grid[x][y] = 1
            else:
                grid[x][y] = 0
    x = side//2
    y = side//2
    for i in range(maxsteps):
        grid[x][y] = 0
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x<0 or y<0 or x==side or y==side:
            perc += 1
            break
        if grid[x][y] == 1 :
            x -= sx
            y -= sy
        continue
print(perc/npart)