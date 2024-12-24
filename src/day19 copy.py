import time
import re
from functools import cache

class Day19:
    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().split('\n\n')
            self.towels = data[0].split(', ')
            self.designs = data[1].split()

    def part1(self):
        '''#p = '|'.join(self.towels)
        p = '('+'|'.join(self.towels)+')+'
        possible_designs = 0
        for d in self.designs:
            does_match = re.fullmatch(p, d) is not None
            if does_match:
                possible_designs += 1
        print(possible_designs)'''
        possible_designs = 0
        for d in self.designs:
            poss = check_match(d, self.towels)
            if poss:
                possible_designs += 1
        print(possible_designs)



start = time.time()
puzzle = Day19("inputs/day19test.txt")
#puzzle.part1()
T = puzzle.towels
@cache
def check_match(d: str):
    match = False
    if not d:
        match = True
    for t in T:
        if d.startswith(t):
            match = check_match(d.removeprefix(t),T)
            if match:
                break
    return match

#puzzle.part2()
#puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')