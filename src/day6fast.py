import time
import sys

class Day6:
    def __init__(self, filename):
        with open(filename) as f:
            self.map = f.read().split('\n')
            for i in range(len(self.map)):
                self.map[i] = list(self.map[i])
        self.obstacles = []
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == '#':
                    self.obstacles.append((i,j))
                if self.map[i][j] == '^':
                    self.guard_start = (i,j)
        self.h = len(self.map)
        self.w = len(self.map[0])
    
    def part1(self):
        positions = set()
        actual_pos = self.guard_start
        actual_dir = '^'
        while new_guard_in_map(self.h, self.w, actual_pos):
            nearest_obs = search_nearest_obstacle(self.h, self.w, self.obstacles, actual_pos, actual_dir)
            walked_pos = count_positions(nearest_obs, actual_pos)
            actual_pos, actual_dir = reposition(self.h, self.w, nearest_obs, actual_dir)
            for p in walked_pos:
                positions.add(p)
        self.path = positions
        print(len(positions))

    
    def part2(self):
        count = 0
        zz = 0
        for pos in self.path:
            if pos == self.guard_start:
                continue

            actual_pos = self.guard_start
            actual_dir = '^'
            self.obstacles.append(pos)
            looped = False
            bonks = []
            while not looped:
                nearest_obs = search_nearest_obstacle(self.h, self.w, self.obstacles, actual_pos, actual_dir)
                actual_pos, actual_dir = reposition(self.h, self.w ,nearest_obs, actual_dir)
                if not new_guard_in_map(self.h, self.w, actual_pos):
                    break
                if (actual_pos,actual_dir) not in bonks:
                    bonks.append((actual_pos,actual_dir))
                else: looped = True
            self.obstacles.remove(pos)
            count += 1 if looped else 0
            zz += 1
        print(count)

def search_nearest_obstacle(h, w, obs, pos, dir):
    i, j = pos
    nearest_obs = (0,0)
    if dir == '^':
        obs_in_dir = [o for o in obs if o[1]==j and o[0]<i]
        nearest_obs = (-1,j)
        for o in obs_in_dir:
            if abs(i-o[0]) < abs(i-nearest_obs[0]):
                nearest_obs = o
    elif dir == '>':
        obs_in_dir = [o for o in obs if o[0]==i and o[1]>j]
        nearest_obs = (i,w)
        for o in obs_in_dir:
            if abs(j-o[1]) < abs(j-nearest_obs[1]):
                nearest_obs = o
    elif dir == 'v':
        obs_in_dir = [o for o in obs if o[1]==j and o[0]>i]
        nearest_obs = (h,j)
        for o in obs_in_dir:
            if abs(i-o[0]) < abs(i-nearest_obs[0]):
                nearest_obs = o
    elif dir == '<':
        obs_in_dir = [o for o in obs if o[0]==i and o[1]<j]
        nearest_obs = (i,-1)
        for o in obs_in_dir:
            if abs(j-o[1]) < abs(j-nearest_obs[1]):
                nearest_obs = o
    return nearest_obs

def count_positions(obs, pos):
    list_pos = []
    if obs[0] == pos[0] and obs[1] < pos[1]:
        for i in range(pos[1], obs[1],-1):
            list_pos.append((pos[0],i))
    if obs[0] == pos[0] and obs[1] > pos[1]:
        for i in range(pos[1], obs[1]):
            list_pos.append((pos[0],i))
    if obs[1] == pos[1] and obs[0] < pos[0]:
        for i in range(pos[0], obs[0],-1):
            list_pos.append((i,pos[1]))
    if obs[1] == pos[1] and obs[0] > pos[0]:
        for i in range(pos[0], obs[0]):
            list_pos.append((i,pos[1]))
    return list_pos


def reposition(h, w, obs, dir):
    i, j = obs
    if dir == '^':
        pos = (i+1,j) if i > -1 else obs
        new_dir = '>' if i > -1 else dir
    elif dir == '>':
        pos = (i,j-1) if j < w else obs
        new_dir = 'v' if j < w else dir
    elif dir == 'v':
        pos = (i-1,j) if i < h else obs
        new_dir = '<' if i < h else dir
    elif dir == '<':
        pos = (i,j+1) if j > -1 else obs
        new_dir = '^' if j > -1 else dir
    return pos, new_dir

def new_guard_in_map(h, w, pos):
    i, j = pos
    return 0 <= i < h and 0 <= j < w

start = time.time()
puzzle = Day6('inputs/day6.txt')
puzzle.part1()
puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s', file=sys.stderr)