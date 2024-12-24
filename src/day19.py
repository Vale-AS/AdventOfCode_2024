'''import time
import re

class Day19:
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().split('\n\n')
            self.towels = data[0].split(', ')
            self.designs = data[1].split()

    def part1(self):
        #p = '|'.join(self.towels)
        p = '('+'|'.join(self.towels)+')+'
        possible_designs = 0
        for d in self.designs:
            does_match = re.fullmatch(p, d) is not None
            if does_match:
                possible_designs += 1
        print(possible_designs)

start = time.time()
puzzle = Day19("inputs/day19.txt")
puzzle.part1()
#puzzle.part2()
#puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')'''

from functools import cache

P, _, *D = open('inputs/day19.txt').read().splitlines()

@cache
def count(d):
    return d == '' or sum(count(d.removeprefix(p))
        for p in P.split(', ') if d.startswith(p))

for type in bool, int:
    print(sum(map(type, map(count, D))))