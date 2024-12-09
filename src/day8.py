import time
from itertools import combinations

class Day8():
    def __init__(self, filename):
        self.map = []
        with open(filename) as f:
            data = f.read().split('\n')
            for line in data:
                self.map.append(list(line))
        self.h = len(self.map)
        self.w = len(self.map[0])
        self.antennas = {}
        for i in range(self.h):
            for j in range(self.w):
                a = self.map[i][j]
                if a != '.':
                    if a not in self.antennas.keys():
                        self.antennas[a] = [(i,j)]
                    else:
                        self.antennas[a].append((i,j))

    
    def part1(self):
        antinode_count = 0
        for symbol in self.antennas.keys():
            combs = list(combinations(self.antennas[symbol], r=2))
            for c in combs:
                c1, c2 = c
                an1, an2 = find_antinodes(c1, c2)
                i,j = an1
                k,l = an2
                if 0<=i<self.h and 0<=j<self.w:
                    if self.map[i][j] != '#':
                        antinode_count += 1
                        if self.map[i][j] == '.':
                            self.map[i][j] = '#'
                if 0<=k<self.h and 0<=l<self.w:
                    if self.map[k][l] != '#':
                        antinode_count += 1
                        if self.map[k][l] == '.':
                            self.map[k][l] = '#'
        #for e in range(self.h):
        #    self.map[e] = ''.join(self.map[e])
        print(antinode_count)
    
    def part2(self):
        reset_map(self.map)
        antinode_count = 0
        for symbol in self.antennas.keys():
            combs = list(combinations(self.antennas[symbol], r=2))
            for c in combs:
                c1, c2 = c
                ants = find_all_antinodes(c1, c2, self.h, self.w)
                for at in ants:
                    i,j = at
                    if self.map[i][j] != '#':
                        self.map[i][j] = '#'
                        antinode_count += 1
        #for e in range(self.h):
        #    self.map[e] = ''.join(self.map[e])
        print(antinode_count)
    
    def both_parts(self):
        reset_map(self.map)
        an1 = set()
        an2 = set()
        antinode_count1 = 0
        antinode_count2 = 0
        for symbol in self.antennas.keys():
            combs = list(combinations(self.antennas[symbol], r=2))
            for c in combs:
                c1, c2 = c
                ants_up, ants_down = better_find_all_antinodes(c1,c2,self.h,self.w)
                a1 = ants_up[1] if len(ants_up) > 1 else None
                a2 = ants_down[1] if len(ants_down) > 1 else None
                if a1 is not None: an1.add(a1)
                if a2 is not None: an1.add(a2)
                for a in ants_up: an2.add(a)
                for a in ants_down: an2.add(a)
        print(f'part 1 result is: {len(an1)} and part 2 result is: {len(an2)}')



def find_antinodes(c1: tuple[int, int], c2: tuple[int, int]):
    i,j = c1
    k,l = c2
    dist_y = abs(i-k)
    dist_x = abs(j-l)
    if i<k and j<l:
        an1 = (i-dist_y,j-dist_x)
        an2 = (k+dist_y,l+dist_x)
    if i<k and j>l:
        an1 = (i-dist_y,j+dist_x)
        an2 = (k+dist_y,l-dist_x)
    if i>k and j<l:
        an1 = (i+dist_y,j-dist_x)
        an2 = (k-dist_y,l+dist_x)
    if i>k and j>l:
        an1 = (i+dist_y,j+dist_x)
        an2 = (k-dist_y,l-dist_x)
    return an1, an2

def find_all_antinodes(c1: tuple[int, int], c2: tuple[int, int], h, w):
    i,j = c1
    k,l = c2
    dist_y = abs(i-k)
    dist_x = abs(j-l)
    ans = []
    if i<k and j<l:
        edgiest = (i,j)
        while in_range(edgiest, h, w):
            old_edgiest = edgiest
            edgiest = (old_edgiest[0]-dist_y,old_edgiest[1]-dist_x)
        while in_range(old_edgiest, h, w):
            ans.append(old_edgiest)
            old_edgiest = (old_edgiest[0]+dist_y,old_edgiest[1]+dist_x)
    if i<k and j>l:
        edgiest = (i,j)
        while in_range(edgiest, h , w):
            old_edgiest = edgiest
            edgiest = (old_edgiest[0]-dist_y,old_edgiest[1]+dist_x)
        while in_range(old_edgiest, h, w):
            ans.append(old_edgiest)
            old_edgiest = (old_edgiest[0]+dist_y,old_edgiest[1]-dist_x)
    if i>k and j<l:
        edgiest = (i,j)
        while in_range(edgiest, h , w):
            old_edgiest = edgiest
            edgiest = (old_edgiest[0]+dist_y,old_edgiest[1]-dist_x)
        while in_range(old_edgiest, h, w):
            ans.append(old_edgiest)
            old_edgiest = (old_edgiest[0]-dist_y,old_edgiest[1]+dist_x)
    if i>k and j>l:
        edgiest = (i,j)
        while in_range(edgiest, h , w):
            old_edgiest = edgiest
            edgiest = (old_edgiest[0]+dist_y,old_edgiest[1]+dist_x)
        while in_range(old_edgiest, h, w):
            ans.append(old_edgiest)
            old_edgiest = (old_edgiest[0]-dist_y,old_edgiest[1]-dist_x)
    return ans

def better_find_all_antinodes(c1, c2, h, w):
    i,j = c1
    k,l = c2
    ants_up = [c1 if i<k else c2]
    ants_down = [c1 if i>k else c2]
    dist_y = abs(i-k)
    dist_x = abs(j-l)
    at = ants_up[0]
    while in_range(at,h,w):
        if at != c1 and at != c2: ants_up.append(at)
        at = (at[0]-dist_y,at[1]-dist_x) if ants_up[0][1]<ants_down[0][1] else (at[0]-dist_y,at[1]+dist_x)
    at = ants_down[0]
    while in_range(at,h,w):
        if at != c1 and at != c2: ants_down.append(at)
        at = (at[0]+dist_y,at[1]-dist_x) if ants_down[0][1]<ants_up[0][1] else (at[0]+dist_y,at[1]+dist_x)
    return ants_up, ants_down


def in_range(pos, h, w):
    i,j = pos
    return 0<=i<h and 0<=j<w

def reset_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '#':
                map[i][j] = '.'

start = time.time()
puzzle = Day8("inputs/day8.txt")
#puzzle.part1()
#puzzle.part2()
puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')