import time

class Day10:
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().split('\n')
            self.map = []
            for line in data:
                self.map.append([int(e) for e in line])
    
    def both_parts(self):
        sum_score = 0
        rating = 0
        trailheads = find_zeros(self.map)
        for th in trailheads:
            peaks, sc = calc_score(self.map, th)
            sum_score += len(peaks)
            rating += sc
        print(f'part 1 result is: {sum_score} and part 2 result is: {rating}')

def find_zeros(map):
    zeros = []
    for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 0:
                    zeros.append((i,j))
    return zeros

def calc_score(map, th):
    i, j = th
    peaks = set()
    score = 0
    if map[i][j] == 9:
        peaks.add((i,j))
        return peaks, 1
    neighbors = calc_neighbors(map, th)
    for n in neighbors:
        k, l = n
        if map[k][l] == map[i][j]+1:
            ps, sc = calc_score(map, n)
            score += sc
            for p in ps:
                peaks.add(p)
    return peaks, score
            

def calc_neighbors(map, th):
    ns = set()
    i, j = th
    if 0<i:
        ns.add((i-1,j))
    if i+1<len(map):
        ns.add((i+1,j))
    if 0<j:
        ns.add((i,j-1))
    if j+1<len(map[0]):
        ns.add((i,j+1))
    return ns


start = time.time()
puzzle = Day10("inputs/day10.txt")
#puzzle.part1()
#puzzle.part2()
puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')