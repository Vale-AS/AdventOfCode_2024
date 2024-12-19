import time
from copy import deepcopy

class Day15:
    def __init__(self, filename):
        with open(filename) as f:
            map, moves = f.read().split('\n\n')
            self.map = []
            map = map.split('\n')
            for line in map:
                self.map.append(list(line))
            self.moves = ''.join(moves.split('\n'))
        
    def part1(self):
        dirs = {'^': (-1, 0), 
                '>': ( 0, 1), 
                'v': ( 1, 0), 
                '<': ( 0,-1)}
        map = deepcopy(self.map)
        coordinate_sum = 0
        pos = find_char(map, '@')
        for m in self.moves:
            dir = dirs[m]
            map, pos = move_robot(map, dir, pos)
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'O':
                    coordinate_sum += 100 * i + j
        print(coordinate_sum)
    
    def part2(self):
        dirs = {'^': (-1, 0), 
                '>': ( 0, 1), 
                'v': ( 1, 0), 
                '<': ( 0,-1)}
        map = widen_map(deepcopy(self.map))
        coordinate_sum = 0
        pos = find_char(map, '@')
        for m in self.moves:
            dir = dirs[m]
            map, pos = move_robot(map, dir, pos)
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'L':
                    coordinate_sum += 100 * i + j
        print(coordinate_sum)

def find_char(map, chr):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == chr:
                return (i,j)
    return (-1,-1)

def move_robot(map, d, p):
    i, j = tuple([item1 + item2 for item1, item2 in zip(p, d)])
    k, l = p
    if map[i][j] == '#':
        return map, p
    
    elif map[i][j] == '.':
        map[i][j] = '@'
        map[k][l] = '.'
        return map, (i,j)
    
    elif map[i][j] == 'O':
        o_i, o_j = i, j
        while map[o_i][o_j] == 'O':
            o_i, o_j = (o_i + d[0], o_j + d[1])
        if map[o_i][o_j] == '#':
            return map, p
        elif map[o_i][o_j] == '.':
            map[o_i][o_j] = 'O'
            map[i][j] = '@'
            map[k][l] = '.'
            return map, (i,j)
    
    elif map[i][j] == 'R':
        if d[0] == 0:
            l_i, l_j = i, j-2
            count = 1
            while map[l_i][l_j] == 'R':
                count += 1
                l_j -= 2
            if map[l_i][l_j] == '#':
                return map, p
            elif map[l_i][l_j] == '.':
                while count > 0:
                    map[l_i][l_j] = 'L'
                    l_j += 1
                    map[l_i][l_j] = 'R'
                    l_j += 1
                    count -= 1
            map[i][j] = '@'
            map[k][l] = '.'
            return map, (i,j)
        else:
            aff_obs = affected_obstacles(map, d, (i,j), 'R')
            if aff_obs:
                new_map = deepcopy(map)
                for q in range(len(aff_obs)-1,-1,-1):
                    x,y = aff_obs[q]
                    newx = x+d[0]
                    new_map[newx][y] = map[x][y]
                    new_map[x][y] = '.'
                new_map[i][j] = '@'
                new_map[k][l] = '.'
                return new_map, (i,j)
            else:
                return map, p

    elif map[i][j] == 'L':
        if d[0] == 0:
            l_i, l_j = i, j+2
            count = 1
            while map[l_i][l_j] == 'L':
                count += 1
                l_j += 2
            if map[l_i][l_j] == '#':
                return map, p
            elif map[l_i][l_j] == '.':
                while count > 0:
                    map[l_i][l_j] = 'R'
                    l_j -= 1
                    map[l_i][l_j] = 'L'
                    l_j -= 1
                    count -= 1
            map[i][j] = '@'
            map[k][l] = '.'
            return map, (i,j)
        else:
            aff_obs = affected_obstacles(map, d, (i,j), 'L')
            if aff_obs:
                new_map = deepcopy(map)
                for q in range(len(aff_obs)-1,-1,-1):
                    x,y = aff_obs[q]
                    newx = x+d[0]
                    new_map[newx][y] = map[x][y]
                    new_map[x][y] = '.'
                new_map[i][j] = '@'
                new_map[k][l] = '.'
                return new_map, (i,j)
            else:
                return map, p
        

def widen_map(m: list[list[str]]):
    for i in range(len(m)):
        j = 0
        while j < len(m[i]):
            if m[i][j] == '#':
                m[i].insert(j+1, '#')
                j += 2
            elif m[i][j] == '.':
                m[i].insert(j+1, '.')
                j += 2
            elif m[i][j] == 'O':
                m[i][j] = 'L'
                m[i].insert(j+1, 'R')
                j += 2
            elif m[i][j] == '@':
                m[i].insert(j+1, '.')
                j += 2
    return m

def affected_obstacles(map, d, p, c):
    res = []
    if c == 'R':
        r_i, r_j = p
        l_i, l_j = r_i, r_j-1
    elif c == 'L':
        l_i, l_j = p
        r_i, r_j = l_i, l_j+1
    next_posli, next_poslj = l_i + d[0], l_j
    next_posri, next_posrj = r_i + d[0], r_j
    no_wall = map[next_posli][next_poslj] != '#' and map[next_posri][next_posrj] != '#'
    if not no_wall:
        return res
    else:
        if map[next_posli][next_poslj] == 'L':
            upper_check = affected_obstacles(map,d,(next_posli,next_poslj),'L')
            if not upper_check:
                return res
            else:
                res = [(l_i, l_j),(r_i, r_j)] + upper_check
                return res
        if map[next_posli][next_poslj] == 'R' and map[next_posri][next_posrj] == 'L':
            # posible doble piramide
            left_check = affected_obstacles(map, d, (next_posli, next_poslj), 'R')
            right_check = affected_obstacles(map, d, (next_posri, next_posrj), 'L')
            if left_check and right_check:
                res = [(r_i,r_j),(l_i,l_j)] + left_check + right_check
                return res
            else:
                return res
        elif map[next_posli][next_poslj] == 'R':
            # posible piramide solo por izquierda
            left_check = affected_obstacles(map, d, (next_posli, next_poslj), 'R')
            if left_check:
                res = [(r_i,r_j),(l_i,l_j)] + left_check
                return res
            else:
                return res
        elif map[next_posri][next_posrj] == 'L':
            # posible piramide solo por derecha
            right_check = affected_obstacles(map, d, (next_posri, next_posrj), 'L')
            if right_check:
                res = [(r_i,r_j),(l_i,l_j)] + right_check
                return res
            else:
                return res
        if map[next_posli][next_poslj] == '.' and map[next_posri][next_posrj] == '.':
            res = [(r_i,r_j),(l_i,l_j)]
            return res


start = time.time()
puzzle = Day15("inputs/day15.txt")
puzzle.part1()
puzzle.part2()
#puzzle.both_parts()
end = time.time()
print(f'Elapsed time: {end - start}s')