import time
import math

class Day11:
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().strip('\n')
            self.stones = [int(e) for e in data.split()]
    
    def new_new_loop(self, times_blink):
        total_length = 0
        apps = dictify(self.stones)
        for t in range(times_blink):
            ks = [] 
            for l in apps.keys():
                if apps[l] > 0:
                    ks.append(l)
            to_add = []
            for k in ks:
                if k == 0:
                    v = apps[k]
                    apps[k] = 0
                    to_add.append((1,v))
                elif digit_count(k) % 2 == 1:
                    new_k = k*2024
                    v = apps[k]
                    apps[k] = 0
                    to_add.append((new_k,v))
                else:
                    di = digit_count(k)/2
                    lst = int(k/(10**di))
                    rst = int(k%(10**di))
                    v = apps[k]
                    apps[k] = 0
                    to_add.append((lst,v))
                    to_add.append((rst,v))
            for e in to_add:
                i, j = e
                try:
                    apps[i] += j
                except KeyError:
                    apps[i] = j
            if t == 24:
                for v in apps.values():
                    total_length += v
                print(total_length)
                total_length = 0
        for v in apps.values():
            total_length += v
        print(total_length)


def dictify(list):
    d = {}
    for e in list:
        if e in d.keys():
            d[e] += 1
        else:
            d[e] = 1
    return d

def digit_count(n):
    if n == 0:
        return 1
    else:
        return int(math.log10(n))+1

start = time.time()
puzzle = Day11("inputs/day11.txt")
#puzzle.new_new_loop(25)
puzzle.new_new_loop(75)
end = time.time()
print(f'Elapsed time: {end - start}s')