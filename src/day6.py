import time
import sys

class Day6:
    def __init__(self, filename):
        with open(filename) as f:
            self.map = f.read().split('\n')
            for i in range(len(self.map)):
                self.map[i] = list(self.map[i])
    
    def part1(self):
        positions = set()
        self.guard_start = search_start_guard(self.map)
        actual_pos = self.guard_start
        positions.add(actual_pos)
        actual_dir = '^'
        while guard_in_map(self.map):
            new_pos, new_dir = move_guard(self.map, actual_pos, actual_dir)
            if new_pos is not None:
                if new_dir == actual_dir:
                    positions.add(new_pos)
                    actual_pos = new_pos
                else:
                    actual_dir = new_dir
            else:
                break
        self.path = positions
        print(len(positions))
    
    def part2(self):
        count = 0
        reset_map(self.map, self.guard_start,self.guard_start)
        zz = 0
        for pos in self.path:
            print(f'\rPositions remaining {len(self.path)-zz}   {zigzag[zz%(len(zigzag))]}', file=sys.stderr)
            #print ("\033[A\033[A", file=sys.stderr)
            if pos == self.guard_start:
                continue
            i, j = pos
            self.map[i][j] = '#'
            looped = check_if_loop(self.map, self.guard_start)
            count += 1 if looped else 0
            reset_map(self.map, self.guard_start, pos)
            zz += 1
        print(count)



def search_start_guard(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                return (i,j)
            
def guard_in_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in ['^','>','v','<']:
                return True
    return False

def move_guard(map, pos, dir):
    i, j = pos
    if dir == '^':
        if i > 0:
            if map[i-1][j] != '#':
                map[i-1][j] = '^'
                map[i][j] = '.'
                return (i-1,j), '^'
            else:
                map[i][j] = '>'
                return (i,j), '>'
        else:
            map[i][j] = '.'
            return None, '^'

    if dir == '>':
        if j < len(map[0])-1:
            if map[i][j+1] != '#':
                map[i][j+1] = '>'
                map[i][j] = '.'
                return (i,j+1), '>'
            else:
                map[i][j] = 'v'
                return (i,j), 'v'
        else:
            map[i][j] = '.'
            return None, '>'
        
    if dir == 'v':
        if i < len(map)-1:
            if map[i+1][j] != '#':
                map[i+1][j] = 'v'
                map[i][j] = '.'
                return (i+1,j), 'v'
            else:
                map[i][j] = '<'
                return (i,j), '<'
        else:
            map[i][j] = '.'
            return None, 'v'

    if dir == '<':
        if j > 0:
            if map[i][j-1] != '#':
                map[i][j-1] = '<'
                map[i][j] = '.'
                return (i,j-1), '<'
            else:
                map[i][j] = '^'
                return (i,j), '^'
        else:
            map[i][j] = '.'
            return None, '<'

def reset_map(map, start, obs):
    i, j = start
    k, l = obs
    map[k][l] = '.'
    map[i][j] = '^'
    

def check_if_loop(map, start):
    new_path = [(start, '^')]
    looped = False
    actual_pos = start
    actual_dir = '^'
    while not looped:
        new_pos, new_dir = move_guard(map, actual_pos, actual_dir)
        if new_pos is None:
            return False
        else:
            new_tuple = (new_pos, new_dir)
            actual_pos = new_pos
            actual_dir = new_dir
            if new_tuple in new_path:
                return True
            else: 
                new_path.append(new_tuple)

zigzag = [
    "<3      ",
    " <3     ",
    "  <3    ",
    "   <3   ",
    "    <3  ",
    "     <3 ",
    "      <3",
    "     <3 ",
    "    <3  ",
    "   <3   ",
    "  <3    ",
    " <3     ",
]

start = time.time()
puzzle = Day6('inputs/day6.txt')
puzzle.part1()
puzzle.part2()
end = time.time()
print(f'Elapsed time: {end - start}s', file=sys.stderr)