import time

class Day25:
    def __init__(self, filename):
        self.locks = []
        self.keys = []
        with open(filename) as f:
            data = f.read().split('\n\n')
            for scheme in data:
                scheme = scheme.split()
                if scheme[0] == '#####':
                    self.locks.append(scheme)
                elif scheme[-1] == '#####':
                    self.keys.append(scheme)
    
    def part1(self):
        unique_pairs = 0
        for l in self.locks:
            lock_heights = calculate_heights(l, 'lock')
            for k in self.keys:
                key_heights = calculate_heights(k, 'key')
                fits = True
                for i in range(len(key_heights)):
                    if key_heights[i] + lock_heights[i] > 5:
                        fits = False
                        break
                unique_pairs += 1 if fits else 0
        print(f'unique key-lock pairs: {unique_pairs}')

def calculate_heights(scheme, type):
    heights = [0]*5
    if type == 'key':
        for i in range(1,len(scheme)-1):
            for j in range(len(scheme[0])):
                if scheme[i][j] == '#':
                    heights[j] += 1
    elif type == 'lock':
        for i in range(1,len(scheme)-1):
            for j in range(len(scheme[0])):
                if scheme[i][j] == '#':
                    heights[j] += 1
    return heights

start = time.time()
puzzle = Day25("inputs/day25.txt")
puzzle.part1()
end = time.time()
print(f'Elapsed time: {end - start}s')