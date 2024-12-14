import time
from PIL import Image
import numpy as np
from copy import deepcopy

class Day14:
    def __init__(self, filename):
        self.h = 103
        self.w = 101
        self.bots = []
        self.speeds = []
        with open(filename) as f:
            data = f.read().split('\n')
            for line in data:
                bot, speed = line.split()
                x, y = bot[2:].split(',')
                v_x, v_y = speed[2:].split(',')
                self.bots.append((int(x),int(y)))
                self.speeds.append((int(v_x),int(v_y)))

    def part1(self, h=None, w=None):
        safety_factor = 0
        self.h = h if h is not None else self.h
        self.w = w if w is not None else self.w
        robots = deepcopy(self.bots)
        secs = 100
        for i in range(len(robots)):
            bot = robots[i]
            speed = self.speeds[i]
            new_x = (bot[0] + secs * speed[0]) % self.w
            new_y = (bot[1] + secs * speed[1]) % self.h
            robots[i] = (new_x, new_y)
        ul_sf = 0
        ur_sf = 0
        lr_sf = 0
        ll_sf = 0
        ignored_x, ignored_y = np.floor(self.w/2), np.floor(self.h/2)
        for bot in robots:
            x, y = bot
            if x == ignored_x or y == ignored_y:
                continue
            if x < ignored_x and y < ignored_y:
                ul_sf += 1
            elif x < ignored_x and y > ignored_y:
                ur_sf += 1
            elif x > ignored_x and y < ignored_y:
                ll_sf += 1
            elif x > ignored_x and y > ignored_y:
                lr_sf += 1
        print(ul_sf * ur_sf * lr_sf * ll_sf)
    
    def part2(self):
        robots = deepcopy(self.bots)
        for n in range(100):
            for i in range(len(robots)):
                bot = robots[i]
                speed = self.speeds[i]
                new_x = (bot[0] + speed[0]) % self.w
                new_y = (bot[1] + speed[1]) % self.h
                robots[i] = (new_x, new_y)
            generate_image(n, robots, self.h, self.w)

    def both_parts(self):
        robots = deepcopy(self.bots)
        secs = 100
        for i in range(len(robots)):
            bot = robots[i]
            speed = self.speeds[i]
            new_x = (bot[0] + secs * speed[0]) % self.w
            new_y = (bot[1] + secs * speed[1]) % self.h
            robots[i] = (new_x, new_y)
        ul_sf = 0
        ur_sf = 0
        lr_sf = 0
        ll_sf = 0
        ignored_x, ignored_y = np.floor(self.w/2), np.floor(self.h/2)
        for bot in robots:
            x, y = bot
            if x == ignored_x or y == ignored_y:
                continue
            if x < ignored_x and y < ignored_y:
                ul_sf += 1
            elif x < ignored_x and y > ignored_y:
                ur_sf += 1
            elif x > ignored_x and y < ignored_y:
                ll_sf += 1
            elif x > ignored_x and y > ignored_y:
                lr_sf += 1
        print(ul_sf * ur_sf * lr_sf * ll_sf)
        for i in range(len(robots)):
            bot = robots[i]
            speed = self.speeds[i]
            new_x = (bot[0] + (7520-secs) * speed[0]) % self.w
            new_y = (bot[1] + (7520-secs) * speed[1]) % self.h
            robots[i] = (new_x, new_y)
        generate_image(0, robots, self.h, self.w)

# 7520 was obtained by generating a truck load of images, figuring out that a vertical cluster formed every 101 seconds 
# starting at 45 and a horizontal cluster every 103 second starting at 0, and then calculating x such that x ≡ 0 (103) 
# and x ≡ 45 (101) using the Chinese Remainder Theorem (then adding 1 because image numbers started counting at 0 lol)

def generate_image(n, mapping, h, w):
    arr = np.zeros(shape=(h,w,3),dtype=np.uint8)
    for r in mapping:
        j, i = r
        arr[i][j] = [128,0,128]
    im = Image.fromarray(arr, 'RGB')
    # im.show()
    im.save(f"robots_tree.png")


start = time.time()
puzzle = Day14("inputs/day14.txt")
#puzzle.part1()
#puzzle.part2()
puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')